# AIfred: The AI Personal Assitant for your work

**Introducing AIfred: The AI Personal Assistant Tailored for Professionals**

Meet AIfred, your dedicated AI assistant designed to keep professionals, especially engineers, at the peak of productivity. AIfred employs AI to combine disparate information sources and present a streamlined view of your tasks and commitments. 

![image](https://github.com/Azure-Samples/azure-functions-services-openapi-pinecone-usecase/assets/1047040/962366d2-159f-4ad5-bbb7-2242cbc3c270)


**Key Features:**

- **Unified Data View**: AIfred gathers data from multiple platforms such as emails, Azure DevOps, GitHub, ICM, etc., providing a comprehensive overview of your projects and tasks. 
- **Data Standardization**: Using OpenAI's Ada-003 model, incoming data is converted into embeddings, standardizing it for efficient storage and retrieval.
- **Vector Database Integration**: AIfred stores data embeddings in Pinecone, a cutting-edge vector database. [Pinecone]([#](https://www.pinecone.io/)) 
- **Active Polling**: Regular polling ensures your data stays up-to-date and accurate.
- **Intelligent Query Resolution**: Leveraging [LangChain's Retrieval QA](https://python.langchain.com/en/latest/modules/chains/index_examples/vector_db_qa.html) mechanism, AIfred can fetch and prompt responses to user queries.
- **Intuitive UI**: AIfred uses [Streamlit](https://streamlit.io/) for a user-friendly, easily consumable interface.

**Uniqueness (USP):**

- **Simplify and Streamline**: AIfred transforms the mundane task of managing emails and other data sources, offering a convenient first pass on incoming information.
- **Personalized Experience**: AIfred can be tailored to your needs through frameworks like Logic Apps' connector ecosystem and adding more connections.
- **Cloud-Optimized**: AIfred seamlessly integrates with Azure Functions, with the backend and UI running in separate apps. The backend is responsible for data ingestion, embedding, vector DB management, and API provision, while the Streamlit-based UI utilizes a custom handler mechanism. 

Experience a new standard in task management with AIfred - designed for professionals powered by AI.

## Screenshots

### The welcome UI
<img width="1031" alt="image" src="https://github.com/Azure-Samples/azure-functions-services-openapi-pinecone-usecase/assets/1047040/eebc8157-becc-47b2-ac63-e41ede1c044c">

### Asking questions to AIFred
<img width="1098" alt="image" src="https://github.com/Azure-Samples/azure-functions-services-openapi-pinecone-usecase/assets/1047040/7dd5cb71-51ed-4507-ac38-8f54486d8987">

<img width="1504" alt="image" src="https://github.com/Azure-Samples/azure-functions-services-openapi-pinecone-usecase/assets/1047040/27f3d2f9-0cb1-498b-84cd-5a260199b2aa">

<img width="982" alt="image" src="https://github.com/Azure-Samples/azure-functions-services-openapi-pinecone-usecase/assets/1047040/741df9b8-3248-4d7b-8bb3-f66e232a82b7">

### Prerequisites

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

- Install latest azure functions core tools
- Install Python dependencies
  - `python -m pip install -r requirements.txt`
- func start
- ...

### Quickstart
(Add steps to get up and running quickly)

1. Start backend Server
    - git clone https://github.com/Azure-Samples/azure-functions-services-openapi-pinecone-usecase.git
    - cd folder `azure-functions-services-openapi-pinecone-usecase/ai-personal-assistant/`
    - run `func start` to start the backend service

2. Start UI Server

## Resources

(Any additional resources or related projects)

- [LangChain](https://github.com/hwchase17/langchain)
- [Pinecone](https://www.pinecone.io/)
- [Azure Functions Python](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview?pivots=programming-language-python)
