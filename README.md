# 🦜🔗 LangChain - Complete Learning Journey

> Notes, code, and experiments following the [CampusX LangChain Playlist](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0)

---

## 📚 Table of Contents

1. [Introduction to LangChain](#1-introduction-to-langchain)
2. [LangChain Components](#2-langchain-components)
3. [LangChain Models](#3-langchain-models)
4. [Prompt Templates](#4-prompt-templates)
5. [Output Parsers](#5-output-parsers)
6. [Chains](#6-chains)
7. [Runnables (LCEL)](#7-runnables-lcel)
8. [Structured Output](#8-structured-output)
9. [Document Loaders](#9-document-loaders)

---

## 1. Introduction to LangChain

- What is LangChain and why it matters
- The LLM application development landscape
- Setting up the environment (`langchain`, `langchain-community`, `langchain-openai`)
- Hello World with LangChain

## 2. LangChain Components

- Overview of the LangChain ecosystem
- Models, Prompts, Chains, Memory, Agents, Tools
- LangChain vs LangChain Community vs LangChain Core
- How components fit together in a pipeline

## 3. LangChain Models

- **LLMs** — text-in, text-out (legacy interface)
- **Chat Models** — message-in, message-out (modern interface)
- **Embedding Models** — text-in, vector-out
- Using OpenAI, HuggingFace, Groq, and Ollama models
- Model parameters: `temperature`, `max_tokens`, `top_p`

## 4. Prompt Templates

- `PromptTemplate` — simple string templates with variables
- `ChatPromptTemplate` — structured system/human/ai messages
- `MessagesPlaceholder` — injecting dynamic chat history
- Saving and loading prompt templates (JSON format)
- Building a chatbot with memory using prompts

## 5. Output Parsers

- `StrOutputParser` — raw string extraction
- `JsonOutputParser` — structured JSON responses
- `PydanticOutputParser` — type-safe parsing with Pydantic models
- `StructuredOutputParser` — schema-based parsing
- Chaining parsers with prompts

## 6. Chains

- `SimpleChain` — single prompt → model → output
- `SequentialChain` — output of one chain feeds next
- `ParallelChain` — multiple chains running simultaneously
- `ConditionalChain` — routing logic based on input
- When to use each chain pattern

## 7. Runnables (LCEL)

> LangChain Expression Language — the modern way to compose pipelines using the `|` operator

- `RunnableSequence` — pipe components with `|`
- `RunnableParallel` — run multiple runnables at once
- `RunnablePassthrough` — pass inputs unchanged downstream
- `RunnableLambda` — wrap any Python function as a Runnable
- `RunnableBranch` — conditional routing in pipelines

## 8. Structured Output

- `with_structured_output()` — native structured output support
- Using **Pydantic** models for type-safe schemas
- Using **TypedDict** for lightweight schemas
- Using **JSON Schema** directly
- Structured output with open-source models (Llama via Ollama)

## 9. Document Loaders

- `TextLoader` — loading `.txt` files
- `PDFLoader` — extracting text from PDFs
- `CSVLoader` — loading tabular data
- `WebBaseLoader` — scraping web pages
- `DirectoryLoader` — loading all files from a folder

---

## 🛠️ Setup

```bash
# Clone the repo
git clone https://github.com/neemydev/langchain.git
cd langchain

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install langchain langchain-community langchain-openai python-dotenv
```

Create a `.env` file in the root:

```env
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

---

## 📁 Folder Structure

```
langchain/
├── 01_intro/
├── 02_components/
├── 03_models/
├── 04_prompts/
├── 05_output_parsers/
├── 06_chains/
├── 07_runnables/
├── 08_structured_output/
├── 09_document_loaders/
└── README.md
```

---

## 🔗 Resources

- 📺 [CampusX LangChain Playlist](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0)
- 📖 [LangChain Official Docs](https://python.langchain.com/docs/introduction/)
- 🐙 [CampusX GitHub](https://github.com/campusx-official)
