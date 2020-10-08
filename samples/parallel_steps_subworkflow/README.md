# Parallel Tasks example for Google Workflows

Google Workflows team is working on a native support for execution of parallel tasks in a Workflow.
Customers that need to use this capability now, can use the guidelines in this repository to run their tasks in parallel already now. 

## How does it work?
The solution takes an array of task definitions, with array items containing
- url - URL of the task to be triggered (mandatory)
- method - HTTP method to be used (mandatory)
- body - dictionary with body parameters (optional)
- query - dictionary with query parameters (optional)
- auth - can be skipped or "OAuth2" or "OIDC" (optional)

## Usage instruction

All steps below should 
1. In a project of your Create a Service Account that has read/write permissions to Firestore/Datastore and invoker privileges for Workflows
2. Create a new workflow using Service Account above, based on source code from "caller_subwf.yaml" file with "caller_subwf" name. 
3. Paste the contents of "parallel.yaml" file at the end of the source code of the workflow where you want to run parallel tasks
4. Run your tasks 

```yaml
main:
      - createMyTasks:
          assign:
            - tasks:
                - url: "..."
                  method: "GET"
                - url: "..."
                  method: "GET"
                  query:
                      name: Anna
                - url: "..."
                  method: "POST"
                  body: 
                      name: David
      - runTasks:
          call: parallelTasks
          args:
              tasks: ${tasks}
          result: taskResult
      - lastStep:
          return: ${taskResult}

# the contents of parallel.yaml file goes here....
```
## Result
parallelTasks subworkflows blocks the execution until all tasks from the array are completed (successfully or not). While waiting, it is doing periodic polling for results. The frequence of polling can be controlled with optional polling parameter that can be passed to parallelTasks call (the value of polling is interpreted as number of seconds in between polling attempts). It defaults to 30. 

The result of parallel tasks execution is a dictionary:
```json
"status": "success|failure",
"tasks":
    [
        {
            "status": "success|failure"
            "result": HTTP_response_of_the_task
            "id": task_id
        },
        ...
    ]
```

The overall status is "success" if all tasks are successful, it's "failure" otherwise. 

**Note 1:**: Temporarily, the name of the project is hardcoded in both workflows under 'project' variable, please replace with a project ID that you deploy it to. This will be replaced with an environment variable once it's available. 

**Note 2:** _Source code available in this repository is delivered under no guarantee or formal support from Google. Regardless, Google Workflows product team will keep contributing to this repo and community on an best effort basis._