# Interview Question Creator

An AI-powered web application that automatically generates interview questions and answers from PDF documents using LangChain and OpenAI GPT.

## Features

- Upload PDF documents
- Automatic question generation using GPT
- Context-aware answer generation using FAISS vector retrieval
- Export Q&A pairs to CSV format
- Modern, responsive web UI
- Real-time processing feedback

## Technologies Used

- **Backend**: FastAPI, Python 3.13, Uvicorn
- **AI/ML**: LangChain, LangChain Classic, OpenAI GPT, FAISS
- **PDF Processing**: pypdf
- **Frontend**: HTML, CSS, Bootstrap 5, JavaScript, Jinja2 Templates
- **Vector Store**: FAISS (Facebook AI Similarity Search)

## Prerequisites

- Python 3.10 or higher
- OpenAI API Key

## Installation

### 1. Create Virtual Environment

```bash
conda create -n interview python=3.10 -y
conda activate interview
```

Or using venv:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Application

Start the FastAPI server:

```bash
python app.py
```

Or using uvicorn directly:

```bash
uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

The application will be available at `http://localhost:8080`

## Usage

1. Open your browser and navigate to `http://localhost:8080`
2. Upload a PDF file
3. Click "Generate Q&A" button
4. Wait for the AI to analyze your document
5. Download the generated Q&A CSV file

## How It Works

### Document Processing Pipeline

1. **PDF Loading**: Extracts text from uploaded PDF using PyPDFLoader
2. **Text Splitting**: Splits content into chunks using TokenTextSplitter
   - Question generation: 10,000 token chunks with 200 token overlap
   - Answer generation: 1,000 token chunks with 100 token overlap
3. **Question Generation**: Uses a refine chain with GPT to generate relevant interview questions
4. **Vector Store Creation**: Creates FAISS index from document chunks with OpenAI embeddings
5. **Answer Generation**: Uses RetrievalQA chain to generate context-aware answers



## Output

- Generated Q&A pairs are saved to `static/output/QA.csv`
- CSV format with columns: `Question`, `Answer`



## Notes

- Supported format: PDF only
- Generated files are stored in `static/output/QA.csv`
- Uploaded files are stored in `static/docs/`
- Uses GPT model for both question and answer generation
