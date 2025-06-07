from pydantic_ai import Agent # <-- import the correct function
from pydantic import BaseModel
import os
import asyncio

#Define a structured output model
class CustomerResponse(BaseModel):
    reply:str
    sentiment:str
    action_needed:bool

#Set up the GEMINI API KEY
os.environ["GEMINI_API_KEY"] = "your api key"

#Define the agent with gemini model
support_agent = Agent(
    system_prompt= "You are a customer support assistant. Provide a concise response to the customer's query, analyze sentiment, and indicate if action is needed.",
    model="gemini-1.5-flash",
    output_model=CustomerResponse
)

#Run the agent with a sample query
async def main():
    query = "I lost my credit card, what should I do?"
    response = await support_agent.run(query)
    print(response)

if __name__ == "__main__":
    asyncio.run(main())