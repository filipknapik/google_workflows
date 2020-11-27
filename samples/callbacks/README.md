# Callbacks for Google Workflows
This model allows workflows to wait and block execution until an external system makes an HTTP callback to preagreed URL. This model allows for integration of workflows with long running jobs or user-triggered callbacks. 

**Design**
Workflows doesn't support callbacks out of the box today. To address the need, solution in this repo does the following:
+ creates a Cloud Function that will wait for all callbacks in a given project. Once the function gets a callback, its contents is saved to a Firestore database (NoSQL)
+ Workflow uses a subworkflow (available in this repo) that checks periodically in Firestore if the response is avialable in the database. The subworkflow is blocking execution until the response is received. Once the response is receveived, the contents of the callback call is available in Workflow variables. The workflow is also deleting the entry from the database.
+ Another subworkflow (avialable in this repo) can be used to generate a deterministic callback URL that can be then sent to the system that will be making the callback
+ At this point, the workflow requires a unique runID runtime attribute to distinguish individual executions. We will enable usage of unique Execution ID in the near future, which will remove the need for external generation of a unique identifier. User can also use a Cloud Function for unique ID generation in the meantime.  

# Sample deployment
**1. Cloud Function Deployment**
+ Go to Cloud Functions in Cloud Console and hit Create Function in the same project as your workflow
+ Pick any name you want, use the same region as your workflow
+ Use HTTP trigger and "Allow unauthenticated invocations". Use "Require authentication" only if the systems that are making callbacks would have IAM access tokens. Note that every callback will have unique URL paramater anyway 
+ Go to Next page, set Runtime to Python 3.8 and "processEntry" as Entry point
+ use requirements.txt and main.py from the "function" subfolder of this repo and deploy the function

**2. Workflow Deployment**
+ Create a new workflow in the same location as the function. It requires no special IAM permissions
+ Use the source code from the "workflow" subfolder

**3. Enable Firestore API**
+ Go to Cloud Console and enable Firestore API. Use "native mode". No need to create anything in the database

# Sample testing
+ In Cloud Console

Contact knapik@google.com with questions. 

**1. Cloud Function Deployment**