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

1. Create a Service Account that has read/write permissions to Firestore/Datastore and invoker privileges for Workflows
2. C

**Note:** _Source code available in this repository is delivered under no guarantee or formal support from Google. Regardless, Google Workflows product team will keep contributing to this repo and community on an best effort basis._