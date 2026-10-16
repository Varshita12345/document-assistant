# 🛠️ AI Document Understanding Assistant

An offline, privacy-first command-line utility built to parse, process, and extract key insights from text documents using a local Large Language Model.

## 🚀 Skill Overview
This assistant solves the problem of parsing lengthy text documents manually. By utilizing a local AI inference framework, it guarantees full data privacy—meaning no document data ever leaves your physical machine or gets sent to external cloud APIs.

## 🧰 Core Tech Stack
* **Language:** Python 3.12+
* **Local Inference Engine:** Ollama (Desktop Client)
* **Open Source LLM:** Google Gemma 2B (`gemma:2b`)
* **Environment:** Virtual Environment (`.venv`) with Windows PowerShell execution

## ⚙️ How It Works (Architecture)

1. **`tools.py`**: Handles basic file system operations. It opens the designated text file securely, handles encoding exceptions, reads raw text data into memory blocks, and strips out unneeded whitespace.
2. **`model.py`**: Communicates directly with the running Ollama background service using the native `ollama` Python client. It passes the raw document data along with specialized engineering prompts targeting text synthesis or context-bound question answering.
3. **`main.py`**: Manages the application workflow. It initiates a clean terminal user interface (CLI), handles runtime loops, verifies document presence using path checks, and safely streams back outputs to the user window.

## 🤖 Model Performance Configuration
This application is explicitly built to run on the **Gemma 2B** architecture. The model parameters utilize the following engineered task contexts:

* **Document Summarization:** The text context is bound by structural rules requiring the model to extract main headers and key milestones without introducing outside hallucinations.
* **Contextual Q&A:** A tight systemic constraint is injected (`"Based ONLY on the context provided above..."`), forcing the model to operate strictly as a semantic search and answering engine rooted in the source material.

## 💻 How to Run This Skill

### 1. Initialize Local AI Server
Ensure your background Ollama desktop app engine is open and active. Pull the required model profile inside your system terminal:
```bash
ollama pull gemma:2b
```

### 2. Launch the Application
Run the main script wrapper from your workspace directory by passing the exact execution string:
```powershell
python "C:\Users\Varshitha\Desktop\Hacthober fest\open\main.py"
```

### 3. Usage Instructions
1. Enter your text document target (e.g., `document.txt`) when prompted by the initialization interface.
2. Choose option `1` to generate an automated local text summary.
3. Choose option `2` to run ad-hoc custom questions against the document's knowledge base.
