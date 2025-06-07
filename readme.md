# Pydantic-AI Agentic Example

This project demonstrates how to build a basic query-answering AI agent using the [pydantic-ai](https://github.com/ContextualAI/pydantic-ai) agentic framework. It shows how to define structured output models with Pydantic, connect to LLMs (such as Gemini or Ollama), and run queries with structured responses.

## Features

- **Agentic architecture** using pydantic-ai
- **Structured output** using Pydantic models
- **Supports multiple LLM backends** (Gemini, Ollama via OpenAI API)
- **FastAPI integration** for serving agents as APIs

## Example: Using Ollama with Pydantic-AI

```python
from pydantic_ai import Agent
from pydantic import BaseModel
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

class CustomerResponse(BaseModel):
    reply: str
    sentiment: str
    action_needed: bool

ollama_model = OpenAIModel(
    model_name="llama3.2:latest",  # Use your Ollama model name
    provider=OpenAIProvider(base_url="http://localhost:11434/v1")
)

agent = Agent(ollama_model, output_type=CustomerResponse)

if __name__ == "__main__":
    result = agent.run_sync("I lost my credit card, what should I do?")
    print(result.output)
    print(result.usage())
```

## Running

1. Make sure you have [Ollama](https://ollama.com/) running and the model pulled (e.g., `ollama pull llama3.2:latest`).
2. Install dependencies:  
   ```
   pip install pydantic-ai fastapi
   ```
3. Run the script:
   ```
   python pydantic_with_ollama.py
   ```

## FastAPI Example

You can also expose your agent as an API using FastAPI. See `agent_controller.py` for an example endpoint.

---

**This project is a minimal demonstration of agentic LLM orchestration with structured outputs using pydantic-ai.**