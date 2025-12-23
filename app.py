from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_core.runnables import RunnableLambda, RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import os
from pathlib import Path
import uuid
from dotenv import load_dotenv

# load the .env variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

BASE_DIR = Path(__file__).resolve().parent
VECTOR_DB_DIR = os.path.join(BASE_DIR, "vector_stores")

## emmeding model
def emed_model():
    model = OpenAIEmbeddings(model="text-embedding-3-small")
    return model

## llm model 
def llm_model():
    llm= ChatOpenAI(model='gpt-3.5-turbo',temperature=0)
    return llm

## data load from youtube link and that url is taken from the user
def data_loader(yt_url):
    loader = YoutubeLoader.from_youtube_url(youtube_url=yt_url)
    doc = loader.load()
    return doc

def get_db_path(db_id:str):
    return os.path.join(VECTOR_DB_DIR,db_id)

## data preprocessing, split into chunks save into vector store with unique ids and return that that ids
## remove the vector store file after the chat ends 
def prepared_data(yt_url:str):

    # 1. Create unique ID and persistent path
    db_id = str(uuid.uuid4())
    persist_path = get_db_path(db_id)
    os.makedirs(persist_path, exist_ok=True)

    doc = data_loader(yt_url)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000 , chunk_overlap = 200)
    text_chunk = text_splitter.split_documents(doc)
    emedder = emed_model()
    vector_store = Chroma.from_documents(
        documents=text_chunk,
        embedding=emedder,
        persist_directory=get_db_path(db_id=db_id)
    )
    return db_id

## CHAT PART

## load database
def load_db(db_id):
    return Chroma(
        persist_directory=get_db_path(db_id),
        embedding_function=emed_model()
    )

## user query
def video_chat(db_id,query:str):
    vectore_store = load_db(db_id)
    retrival_text = vectore_store.as_retriever(search_kwargs={'k':3})
    template = '''
        You are an expert AI assistant.

        Use ONLY the information provided in the CONTEXT to answer the QUESTION.
        Do NOT use prior knowledge or make assumptions.

        CONTEXT:
        {context}

        INSTRUCTIONS:
        - Answer clearly and concisely.
        - If the answer is explicitly stated in the context, quote or paraphrase it accurately.
        - If the context does NOT contain enough information to answer the question, say:
        "The provided video context does not contain enough information to answer this question."
        - Do NOT hallucinate or infer beyond the context.
        - If the question is ambiguous, ask for clarification instead of guessing.
        - Prefer bullet points or step-by-step explanations when appropriate.

        QUESTION:
        {query}

        '''
    prompt = ChatPromptTemplate.from_template(template,input_variable = ['context','query'])
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    parallel_chain = RunnableParallel({
        'context' : retrival_text | RunnableLambda(format_docs),
        'query' : RunnablePassthrough()
    })

    main_chain = parallel_chain | prompt | llm_model() | StrOutputParser()

    return main_chain.invoke('query') 

if __name__ == "__main__":
    ytube_link = input("Enter youtube url: ")
    print("\nProcessing video... Please wait.")
    db_id = prepared_data(ytube_link)
    print("\nVideo processed successfully.")
    print("You can now ask questions about the video.\n")

    while(1):
        query = input("Ask a question (or type 'exit'): ").strip()

        if query.lower() == "exit":
            break

        answer = video_chat(db_id, query)
        print("\nAnswer:\n", answer)