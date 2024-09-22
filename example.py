from pdf_qa_agent import PDFQAAgent
import os
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")

agent = PDFQAAgent(openai_api_key)

pdf_path = "handbook.pdf"
questions = [
    "What is the name of the company?",
    "Who is the CEO of the company?",
    "What is their vacation policy?",
    "What is the termination policy?"
]

results = agent.run(pdf_path, questions)
print(results)