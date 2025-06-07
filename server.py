import uvicorn

if __name__ == "__main__":
    uvicorn.run("agent_controller:app",host="127.0.0.1",port=8082, reload=True,log_level="info")