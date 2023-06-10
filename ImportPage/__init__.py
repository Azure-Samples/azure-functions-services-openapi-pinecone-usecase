import os
import logging
import pinecone
from dotenv import load_dotenv
import azure.functions as func
from langchain.vectorstores import Pinecone
from langchain.document_loaders import UnstructuredURLLoader, DirectoryLoader, JSONLoader, TextLoader, CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document

index_name = 'functions'

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV")
)

def main(req: func.HttpRequest) -> func.HttpResponse:
    load_dotenv()
    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        content = req_body.get('content')
    if content:
        import os

        file_path = "jsons/emails.json"

        if os.path.exists(file_path):
            logging.info("File exists!")
        else:
            logging.info("File does not exist.")

        loader = CSVLoader(file_path="jsons/workitems.csv")
        documents = loader.load()
        # documents = [Document(page_content=content)]
        logging.info(f"Retrieved {len(documents)} documents")
        logging.info(f"Retrieved {documents}")
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        logging.info(f"Split into {len(docs)} chunks")
        embeddings = OpenAIEmbeddings(
            deployment="text-embedding-ada-002",
            model="text-embedding-ada-002",
            openai_api_base=os.getenv("OPENAI_API_BASE"),
            openai_api_type=os.getenv("OPENAI_API_TYPE")
        )

        embeddings.openai_api_key = os.getenv("OPENAI_API_KEY")
        embeddings.openai_api_version = os.getenv("OPENAI_API_VERSION")

        logging.info(f"Embeddings initialized {os.getenv('OPENAI_API_BASE')}")
        for doc in docs:
            Pinecone.from_documents(
                [doc], embeddings, index_name=index_name)
        logging.info(f"Indexed {len(docs)} chunks")
        index_description = pinecone.describe_index(index_name)
        logging.info(index_description)

        return func.HttpResponse(f"Indexed {len(docs)} chunks", status_code=200)
    else:
        return func.HttpResponse(
            "Pass a json object with a url property",
            status_code=400
        )
