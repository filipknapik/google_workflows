# Twilio connector for Google Workflows
Open source connector for Twilio. 

<h3>Overview</h3>

It supports sending Twilio SMS in one of two ways:
- using an Account ID and Auth Token stored in Google Cloud Secret Manager
- using an Account ID and Auth Token passed as a variable

We recommend using the version that reads secrets from Secret Manager as it's the most secure and convenient at the same time.

Use the version with a secrets passed as a variable only when making high number of Twilio API calls using the same account in the same workflow. In this case, make an explicit call to Secret Manager first to retrieve the secrets and store in Workflow variables, and use this key in all subsequent calls to Twilio. 

<h3>Usage</h3>

**Twilio**

1. Create an account in Twilio and get an Account SID and Auth Token. Refer to Twilio documentation for details 

**Google Cloud**

1. Create new or edit Service Account that you will use when deploying your workflow. Assign it a "Secret Manager Secret Accessor" role.
2. Create two secrets in Secret Manager; one to store Twilio Account SID and one to store Auth Token. 
3. Copy and paste one of the subworkflows from twilio.yaml (the using Secret Manager or variables with secrets) at the end of your workflow source code
4. Make a call to it this way (replacing the names of the secrets with the ones you used in Secret Manager):

```yaml
main:
    steps:
      - sendHelloWorld:
          call: twilioSendSMSWithSecretManager
          args:
              twilioAccountSIDSecret: "MyAccountSID"
              twilioAuthTokenSecret: "MyAuthToken"
              from: "+1234567890"
              to: "+987654321"
              message: "Hello World!"
          result: twilioResponse

twilioSendSMSWithSecretManager:
    # the rest of the subworkflow source code from this repo goes here...
```