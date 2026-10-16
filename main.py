import os
from tools import read_document
from model import summarize_document, answer_question

def main():
    print("=========================================")
    print("    AI DOCUMENT UNDERSTANDING ASSISTANT  ")
    print("=========================================")
    print("Running locally via Ollama (Gemma E2B)\n")

    # 1. Ask the user for the text document name
    filename = input("Enter your document filename (e.g., document.txt): ").strip()
    
    # Check if the file exists locally before running model requests
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found in the current folder path.")
        return
        
    # 2. Extract text data using your custom tools module
    document_text = read_document(filename)
    
    if not document_text or len(document_text.strip()) == 0:
        print("Error: The document text is empty or could not be processed.")
        return

    print(f"\n[Success: '{filename}' loaded into memory!]")
    
    # 3. Main execution loop
    while True:
        print("\nWhat would you like to do?")
        print("1. Generate a document summary")
        print("2. Ask a question about the document data")
        print("3. Exit Program")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            print("\n--- Requesting Summary from local Gemma ---")
            summary = summarize_document(document_text)
            print("\n[Summary Result]:")
            print(summary)
            
        elif choice == "2":
            question = input("\nWhat information are you looking for? ")
            if not question.strip():
                print("Question cannot be blank.")
                continue
                
            print("\n--- Processing Question with local Gemma ---")
            answer = answer_question(document_text, question)
            print("\n[Answer Result]:")
            print(answer)
            
        elif choice == "3":
            print("\nShutting down AI Assistant. Goodbye!")
            break
            
        else:
            print("\nInvalid selection. Please input 1, 2, or 3.")

if __name__ == "__main__":
    main()
