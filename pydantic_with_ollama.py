from pydantic_ai import Agent # <-- import the correct function
from pydantic import BaseModel
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
import os
import asyncio

#Define a structured output model
class CustomerResponse(BaseModel):
    reply:str
    sentiment:str
    action_needed:bool


ollama_model = OpenAIModel(
    model_name="llama3.2:latest",
    provider=OpenAIProvider(base_url="http://localhost:11434")
)

#Define the agent with gemini model
agent = Agent(ollama_model,output_type=CustomerResponse)

#Run the agent with a sample query


if __name__ == "__main__":
    result = agent.run_sync("I lost my credit card, what should I do?")
    print(result.output)
    print(result.usage())