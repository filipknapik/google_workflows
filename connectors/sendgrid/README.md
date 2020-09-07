# SendGrid connector for Google Workflows
Open source connector for SendGrid. 

<h3>Overview</h3>

This connectors supports sending emails using SendGrid API. 

<h3>Usage</h3>

**SendGrid**

1. Create an account in SendGrid
2. Create an API Key for SendGrid email API (https://app.sendgrid.com/settings/api_keys)

**Google Cloud**

1. Create new or edit Service Account that you will use when deploying your workflow. Assign it a "Secret Manager Secret Accessor" role.
2. Create a new Secret in Secret Manager to store the secret you got in step 2 of SendGrid part
3. Copy and paste the subworkflow from sendgrid.yaml at the end of your workflow source code
4. Make a call to it this way (MySendGrid is the name of the secret we created in Secret Manager, and from/to are respective email addresses):

```yaml
main:
    steps:
      - step1:
          call: sendGridSend
          args:
              secret: MySendGrid
              from: ...
              to: ...
              subject: "This is a test"
              content: "Hello world!"
              contentType: "text/plain"
          result: callResult
      - step2:
          return: ${callResult}

sendGridSend:
    # the rest of the subworkflow source code from this repo goes here...
```