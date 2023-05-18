import os
import logging
import pinecone
import azure.functions as func
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain import OpenAI
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA

# pinecone.init(
#     api_key=os.getenv('PINECONE_API_KEY'),  # find at app.pinecone.io
#     environment=os.getenv('PINECONE_ENV')  # next to api key in console
# )

index_name = 'functions'
embeddings = OpenAIEmbeddings()
docsearch = Pinecone.from_existing_index(index_name, embeddings)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        question = req_body.get('question')            

    if question:
        result = qa.run(question)

        return func.HttpResponse(f"Answer: {result}", status_code=200)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
