import os
import json
from typing import List, Dict
from PyPDF2 import PdfReader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.schema import HumanMessage, SystemMessage

class PDFQAAgent:
    def __init__(self, openai_api_key: str):
        self.openai_api_key = openai_api_key
        os.environ["OPENAI_API_KEY"] = self.openai_api_key
        self.embeddings = OpenAIEmbeddings()
        self.chat_model = ChatOpenAI(model_name="gpt-4o-mini")

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        pdf_reader = PdfReader(pdf_path)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    def split_text(self, text: str) -> List[str]:
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=800,
            chunk_overlap=200,
            length_function=len,
        )
        return text_splitter.split_text(text)

    def create_vector_store(self, texts: List[str]) -> FAISS:
        return FAISS.from_texts(texts, self.embeddings)

    def answer_question(self, question: str, vector_store: FAISS) -> str:
        docs = vector_store.similarity_search(question, k=5)
        context = "\n".join([doc.page_content for doc in docs])
        
        system_message = SystemMessage(content="You are a helpful assistant that answers questions based on the provided context. If you can't find a specific answer in the context, respond with 'Data Not Available'.")
        human_message = HumanMessage(content=f"Context:\n{context}\n\nQuestion: {question}")
        
        response = self.chat_model.invoke([system_message, human_message])
        return response.content.strip()

    def process_questions(self, questions: List[str], vector_store: FAISS) -> Dict[str, str]:
        results = {}
        for question in questions:
            answer = self.answer_question(question, vector_store)
            results[question] = answer
        return results

    def run(self, pdf_path: str, questions: List[str]) -> str:
        '''
        1. Extract text from PDF using PyPDF2
        2. Split the text into chunks to efficiently store in vector store
        3. Create a vector store using FAISS
        4. Process the questions, retrieve the most relevant answer from the vector store and improvise it using the chat model
        '''
        raw_text = self.extract_text_from_pdf(pdf_path)
        texts = self.split_text(raw_text)
        vector_store = self.create_vector_store(texts)
        results = self.process_questions(questions, vector_store)
        json_results = json.dumps(results, indent=2)
        
        return json_results