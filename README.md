
# AI Personal Assitant

## Features

This project framework provides the following features:

* Feature 1
* Feature 2
* ...

## Getting Started

### Prerequisites

(ideally very short, if any)

- Python 3.10
- Appsettings:
```json
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "<You WebJobsStorage Connection String>",
    "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
    "OPENAI_API_TYPE": "azure",
    "OPENAI_API_KEY": "<Your OPENAI_API_KEY>",
    "OPENAI_API_BASE": "<Your OPENAI_API_BASE>",
    "OPENAI_API_VERSION": "<Corret OPENAI_API_VERSION>", 
    "PINECONE_API_KEY": "<Your PINECONE_API_KEY>",
    "PINECONE_ENV": "<Your PINECONE_ENV>"
  }
```

### Installation

(ideally very short)

- Install latest azure functions core tools
- func start
- ...

### Quickstart
(Add steps to get up and running quickly)

1. git clone https://github.com/Azure-Samples/azure-functions-services-openapi-pinecone-usecase.git
2. cd folder `azure-functions-services-openapi-pinecone-usecase`
3. run `func start`


## Demo

A demo app is included to show how to use the project.

To run the demo, follow these steps:

(Add steps to start up the demo)

1.
2.
3.

## Resources

(Any additional resources or related projects)

- [LangChain](https://github.com/hwchase17/langchain)
- [Pinecone](https://www.pinecone.io/)
- [Azure Functions Python](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview?pivots=programming-language-python)
