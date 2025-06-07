from fastapi import FastAPI,HTTPException
import os
from pydantic import BaseModel
from agents import support_agent

class CustomerRequest(BaseModel):
    query:str


app = FastAPI()
@app.post("/run_agent")
async def run_agent(request: CustomerRequest):
    try:
        response = await support_agent.run(request.query)

        content = None
        if hasattr(response, "content"):
            content = response.content
        elif isinstance(response, dict) and "content" in response:
            content = response["content"]
        elif hasattr(response, "reply"):
            content = response.reply
        else:
            content = str(response)

        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    