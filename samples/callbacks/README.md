# Callbacks for Google Workflows
This model allows workflows to wait and block execution until an external system makes an HTTP callback to predetermined URL. This model allows for integration of workflows with long running jobs or user-triggered callbacks. 

**Design**

Workflows doesn't support callbacks out of the box today. To address the need, solution recommended in this repo does the following:
+ creates a Cloud Function that will wait for all workflow callbacks in a given project. Once the function gets a callback, its contents is saved to a Firestore database (NoSQL)
+ Workflow uses a subworkflow (available in this repo) that checks periodically in Firestore if the response is available in the database. The subworkflow is blocking execution until the response is received. Once the callback is made, its contents is made available in Workflow as a result of the subworkflow that was waiting for it. The workflow is also deleting the entry from the database.
+ Another subworkflow (avialable in this repo) can be used to generate a deterministic callback URL that can be then sent to the system that will be making the callback
+ At this point, the workflow requires a unique runID runtime attribute to distinguish individual executions from one another. We will enable usage of unique Execution ID in the near future, which will remove the need for external generation of a unique identifier. User can also use a Cloud Function for unique ID generation in the meantime.
+ As both Cloud Functions and Firestsores are fully serverless, it generates no cost when not in use. As both products have free tiers, many practical implementations may incur no cost although respective pricing models still apply.  

# Deploying the sample
**1. Cloud Function Deployment**
+ Go to Cloud Functions in Cloud Console and hit Create Function in the same project as your workflow
+ Use "callbackFnc" as a function name (if you use another name, you will need to modify the workflow). Use the same region as your workflow
+ Use HTTP trigger and "Allow unauthenticated invocations". Use "Require authentication" only if the systems that are making callbacks would have IAM access tokens. Note that every callback will have unique URL paramater anyway 
+ Go to Next page, set Runtime to Python 3.8 and "processEntry" as Entry point
+ use requirements.txt and main.py from the "function" subfolder of this repo and deploy the function

**2. Workflow Deployment**
+ Create a new workflow in the same location as the function. It requires no special IAM permissions
+ Use the source code from the "workflow" subfolder

**3. Enable Firestore API**
+ Go to Cloud Console and enable Firestore API. Use "native mode". No need to create anything in the database

# Testing the sample
+ In Cloud Console, execute the workflow and place {"runID":"run123"} in the input window
+ Go to the Logs tab of the workflow in Cloud Console and see the callback URL produced
+ You can wait a minute or two to see that workflow execution is still active
+ Paste the callback URL in a browser window and observe that workflow execution is over
+ The model also supports callbacks that pass some data back. To pass data as part of the callback, add "&value=Hello%20World" at the end of the URL when executing it in the browser. You will "Hello World" in the workflow output

# Other considerations
+ The subworkflow that is doing the blocking performs periodic polling to Firestore. The default interval is set to 30 seconds. To modify this value, add e.g. "backoff: 240" to the args in the call to waitForResponse subworkflow
+ In the week of Nov 30, 2020, we will make a change to connectors to Firestore (that are not yet formally launched). You will need to replace ${callbackResult.body} with ${callbackResult} (body will be removed)

Contact knapik@google.com in case of any questions. 