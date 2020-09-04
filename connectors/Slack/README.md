# Slack connector for Google Workflows
Open source connector for Slack. 

<h3>Overview</h3>

It supports pushing messages to a specific Slack channel in one of two ways:
- using a key stored in Google Cloud Secret Manager
- using a key passed as a variable

We recommend using the version that reads a Slack key from Secret Manager as it's the most secure and convenient at the same time.

Use the version with a key passed as a variable only when making high number of Slack calls using the same key in the same workflow. In this case, make an explicit call to Secret Manager first to retrieve the secret and store in a Workflow variable, and use this key in all subsequent calls to Slack. 

<h3>Usage</h3>
**Slack**
1. Create an incoming webhook in Slack for a specific channel using these instructions: https://api.slack.com/messaging/webhooks#getting_started
2. Temporarily save the key you got, in a format of T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX

**Google Cloud**
1. Create new or edit Service Account that you will use when deploying your workflow. Assign it a "Secret Manager Secret Accessor" role.
2. Create a new Secret in Secret Manager to store the secret you got in step 2 of Slack part
3. Copy and paste one of the subworkflows from slack.yaml (the using Secret Manager or variable with a key) at the end of your workflow source code
4. Make a call to it this way (MySlackKey is the name of the secret we created in Secret Manager):

```yaml
main:
    steps:
      - sendHelloWorld:
          call: slackPushWithSecretManager
          args:
              message: "Hello world"
              secret: "MySlackKey"
          result: slackResponse

slackPushWithSecretManager:
    # the rest of the subworkflow source code from this repo goes here...
```