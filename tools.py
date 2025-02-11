import subprocess
from fastapi import HTTPException
import httpx
import os


def install_pip_pkg(pkg_name):
    try:
        res = subprocess.run(['./scripts/install_python_pkg.sh', pkg_name], check=True, capture_output=True, text=True)
        return {"status": "success"}
    except subprocess.CalledProcessError as e:
        return {"status": "fail"}

# Function for task A1
def generate_data_using_script(script_url, email_argument):
    try:
        res = subprocess.run(['./scripts/a1_generate_data_using_script.sh', script_url, email_argument], check=True, capture_output=True, text=True)
        return {"message": "task execution successful", "status_code": 200}

    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail="Bad Request")



# Function for task A2
def format_file(prettier_version, file_path):
    try:
        res = subprocess.run(['./scripts/a2_format_file.sh', prettier_version, file_path], check=True, capture_output=True, text=True)
        return {"message": "task execution successful", "status_code": 200}

    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail="Bad Request")
    


# Function for task A3
def count_no_of_days(dates_file_path, day_of_the_week, output_file_path):
    from datetime import datetime
    from dateutil.parser import parse
    try:
        day_count = 0

        day_num = {
            "Monday": 0,
            "Tuesday": 1,
            "wednesday": 2,
            "Thursday": 3,
            "Friday": 4,
            "Saturday": 5,
            "Sunday": 6
        }

        with open(dates_file_path, 'r') as file:
            for line in file:
                date_str = line.strip()
                try:
                    date_obj = parse(date_str)
                    if date_obj.weekday() == day_num[day_of_the_week]:
                        day_count += 1
                except ValueError:
                    continue
        
        with open(output_file_path, 'w') as out_file:
            out_file.write(str(day_count))

        return {"message": "task execution successful", "status_code": 200}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail="Bad Request")



#Function for task A4
def sort_contacts(contacts_file_path, sorting_properties , output_file_path):
    import json
    try:
        contacts = None

        with open(contacts_file_path, 'r') as file:
            contacts = json.load(file)
        
        if(len(sorting_properties) == 1 ):
            contacts.sort(key=lambda c: (c[sorting_properties[0]]))
        elif(len(sorting_properties) == 2):
            contacts.sort(key=lambda c: (c[sorting_properties[0]], c[sorting_properties[1]]))
        elif(len(sorting_properties) == 3):
            contacts.sort(key=lambda c: (c[sorting_properties[0]], c[sorting_properties[1]], c[sorting_properties[2]]))

        with open(output_file_path, 'w') as out_file:
            out_file.write(json.dumps(contacts))

        return {"message": "task execution successful", "status_code": 200}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail="Bad Request")

# Function for task A5
def manipulate_logs(dir_path, num_of_recent, output_file_path):
    try:
        res = subprocess.run(['./scripts/a5_write_logs.sh', dir_path, num_of_recent, output_file_path], check=True, capture_output=True, text=True)
        return {"message": "task execution successful", "status_code": 200}

    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail="Bad Request")


# Function for task A6
def manipulate_markdowns(dir_path, output_file_path):
    import os
    import json
    try:
        def get_h1_title(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('# '):
                        return line.strip('# ').strip()
            return None

        
        index = {}
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.md'):
                    full_path = os.path.join(root, file)
                    title = get_h1_title(full_path)
                    if title:
                        relative_path = os.path.relpath(full_path, dir_path)
                        index[relative_path] = title

        
        with open(output_file_path, 'w+', encoding='utf-8') as f:
            json.dump(index, f, ensure_ascii=False)

        return {"message": "task execution successful", "status_code": 200}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail="Bad Request")
    


# Function for task A7
def extract_email_info(email_file_path, req_info, output_file_path):
    try:
        content = None
        with open(email_file_path, 'r') as f:
            content = f.read()
        task = f"Extract only the {req_info} from the given content: {content}"
        response = httpx.post(
            "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('AIPROXY_API_KEY')}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [

                    {
                        "role": "user", 
                        "content": task
                    }
                    ],
            },
        )

        returned_info = response.json()["choices"][0]["message"]["content"]

        with open(output_file_path, 'w') as out_file:
            out_file.write(str(returned_info))

        return {"message": "task execution successful", "status_code": 200}

    except Exception as e:
        raise HTTPException(status_code=400, detail="Bad Request")


