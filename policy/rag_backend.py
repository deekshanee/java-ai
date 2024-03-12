import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms.bedrock import Bedrock
def main():
     #load data source
    #data_load = PyPDFLoader('https://www.indiacode.nic.in/bitstream/123456789/9460/1/a1988-59.pdf')
    data_load = PyPDFLoader('https://www.tutorialspoint.com/java/java_tutorial.pdf')
    #split thr text based character , token etc
    data_split = RecursiveCharacterTextSplitter(separators=["\n\n","\n"," ",""],chunk_size=100,chunk_overlap=10)
    #embedding -client connection
    data_embeddings = BedrockEmbeddings(credentials_profile_name='default',
                                        model_id='amazon.titan-embed-text-v1',  
                                        )
    print(data_embeddings)
    #create vector db and create index
    data_index = VectorstoreIndexCreator(
        text_splitter=data_split,
        embedding= data_embeddings,
        vectorstore_cls=FAISS
    )
    #CREATE INDEX FOR POLICY DOC
    db_index = data_index.from_loaders([data_load])
    print(db_index)
    return db_index


def hr_llm():
    llm = Bedrock(credentials_profile_name='default',model_id='anthropic.claude-v2',model_kwargs={"max_tokens_to_sample":3000,"temperature":0.,"top_p":0.9})
    return llm

#searches user prompt here and send both vector db and send tollm

def hr_rag_response(index,question):
    
    reg_llm = hr_llm()
    hr_rag_query=index.query(question=question,llm=reg_llm)
    return hr_rag_query
