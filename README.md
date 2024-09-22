# PDF Q&A Agent

## Overview

The PDF Q&A Agent is a Python-based tool that uses OpenAI's language models to answer questions based on the content of a PDF document. This agent extracts text from a PDF, processes it, and then uses AI to generate answers to user-provided questions.

## Features

- Extract text from PDF documents
- Process and chunk text for efficient analysis
- Use OpenAI's GPT models to generate answers
- Handle multiple questions in a single run
- Return results in a structured JSON format

## Requirements

- Python 3.7+
- OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/pdf-qa-agent.git
   cd pdf-qa-agent
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Import the `PDFQAAgent` class from the main script:

   ```python
   from pdf_qa_agent import PDFQAAgent
   ```

2. Initialize the agent with your OpenAI API key:

   ```python
   agent = PDFQAAgent('your-openai-api-key')
   ```

3. Prepare your PDF file path and a list of questions:

   ```python
   pdf_path = "path/to/your/document.pdf"
   questions = [
       "What is the main topic of this document?",
       "Who is mentioned in the introduction?",
       "What are the key findings?"
   ]
   ```

4. Run the agent and get the results:

   ```python
   results = agent.run(pdf_path, questions)
   print(results)
   ```

## Example

```python
from pdf_qa_agent import PDFQAAgent

agent = PDFQAAgent('your-openai-api-key')

pdf_path = "company_handbook.pdf"
questions = [
    "What is the name of the company?",
    "Who is the CEO of the company?",
    "What is their vacation policy?",
    "What is the termination policy?"
]

results = agent.run(pdf_path, questions)
print(results)
```