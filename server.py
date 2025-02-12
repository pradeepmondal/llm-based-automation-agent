# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "fastapi",
#   "uvicorn",
#   "python-dateutil",
# ]
# ///



import httpx
import os
import json
from typing import Dict, Any
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from tools_description import tools
from tools import *
from business_tools import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Make sure this covers the client's origin
    allow_credentials=True,
    allow_methods=["*"],  # Ensure this includes 'OPTIONS'
    allow_headers=["*"],  # Make sure the necessary headers are included
)

@app.post("/run")
async def ask_gpt(task = Query(None, title="Task String", description="The task string for the model"), tools=tools):
    try:
        response = httpx.post(
            "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('AIPROXY_TOKEN')}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "system",
                        "content": "You must adhere to the following rules: 1) Data outside /data is never accessed or exfiltrated, even if the task description asks for it. 2) Data is never deleted anywhere on the file system, even if the task description asks for it."
                    },
                    {
                        "role": "user", 
                        "content": f"""{task}"""
                    }
                    ],
                "tools": tools,
                "tool_choice": "auto",
            },
        )
        output = response.json()["choices"][0]["message"]
        res = {"name": output["tool_calls"][0]["function"]["name"] , "arguments": output["tool_calls"][0]["function"]["arguments"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
   
    fn = eval(res["name"])
    arguments = json.loads(res["arguments"])
    with open('logs.txt', 'a+') as log_details:
        log_details.write(str(res))
    return fn(**arguments)


@app.get("/read", response_class=PlainTextResponse)
async def get_file(path = Query(None, title="Path String", description="Path string of the file")):
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(path, 'r') as file:
        content = file.read()
        return content



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)