import subprocess
from fastapi import HTTPException
import httpx
import json
import os
from tools import install_pip_pkg


#Function for handling B3 task

def fetch_and_save_data(api_url, output_file_path, params=None):
    try:
        response = httpx.get(api_url, params=params)
        with open(output_file_path, 'w') as out_file:
            out_file.write(json.dumps(response.json()))
        
        return {"message": "task execution successful", "status_code": 200}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Bad Request")



#Function for handling B4 task

def clone_and_commit_git_repo(prompt):
    try:
        api_key = os.getenv('AIPROXY_API_KEY')
        response = httpx.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
                            headers={
                                "Authorization": f"Bearer {api_key}",
                                    "Content-Type": "application/json",
                                
                            }, 
                            json={
                                "model": "gpt-4o-mini",
                                    "messages": [
                
                {"role": "system", "content": "Given this task return a bash script to achieve this, assuming this will be run inside a docker image. Return only the bash script without any markdown in plain text"},
                {"role": "user", "content": f"{prompt}"},
            ]
        })

        bash_script = response.json()["choices"][0]["message"]["content"]

        with open('./scripts/temp_script.sh', 'w') as temp_script:
            temp_script.write(str(bash_script))

        os.chmod('./scripts/temp_script.sh', 0o755)
        res = subprocess.run(['./scripts/temp_script.sh'], check=True, capture_output=True, text=True)
        return {"message": "task execution successful", "status_code": 200}
    
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail="Bad Request")


