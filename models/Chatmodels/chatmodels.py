from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()
import os 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")



# Interact with OpenAI's GPT-3.5-turbo model
#model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, max_completion_tokens=100)
# -----------------------------------------------------------------------
#  Interact with Anthropic's Claude 4.5 Sonnet model
# model = ChatAnthropic(model="claude-sonnet-4-5", api_key=ANTHROPIC_API_KEY, temperature=0.7, max_tokens=100)

# -------------------------------------------------------------------------
# Interact with Google's Gemini Pro model
# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", api_key=GOOGLE_API_KEY, temperature=0.7, max_tokens=100)
# Temperature controls the randomness of the output. Higher values (e.g., 0.8) make the output more random, while lower values (e.g., 0.2) make it more focused and deterministic.
# -------------------------------------------------------------------------

# Interact with Ollama's Llama 3 model
model = ChatOllama(model="qwen3:4b", temperature=0.7, max_tokens=100)
response = model.invoke("write a short poem about cats?")

print(response.content)
print(response.response_metadata.get("model_name"))  # Accessing the model name from additional_kwargs

