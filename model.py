import ollama

# Set your exact local Gemma model configuration string
MODEL_NAME = 'gemma4:e2b'

def summarize_document(document_text: str) -> str:
    """Generates a clear and concise summary of the document using local Gemma."""
    try:
        prompt = f"Provide a clear, brief, and structured summary of the following document:\n\n{document_text}"
        
        response = ollama.generate(
            model=MODEL_NAME,
            prompt=prompt
        )
        return response['response']
        
    except Exception as e:
        return f"Ollama Error: Ensure the Ollama background application is running. Details: {str(e)}"

def answer_question(document_text: str, question: str) -> str:
    """Answers a question scoped strictly to the text using local Gemma."""
    try:
        prompt = (
            f"Context Document Data:\n{document_text}\n\n"
            f"Question: {question}\n\n"
            f"Based on the context provided above, answer the question accurately and concisely."
        )
        
        response = ollama.generate(
            model=MODEL_NAME,
            prompt=prompt
        )
        return response['response']
        
    except Exception as e:
        return f"Ollama Error: Could not connect to the local engine. Details: {str(e)}"
