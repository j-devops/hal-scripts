#imports
import os
import platform
import requests
import json
from decouple import config

#vars
API_URL = "https://api.openai.com/v1/engines/text-davinci-002/completions"
API_KEY = config('API_KEY')

#open ai request
def openai_request(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    data = {
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 100,
    }
    response = requests.post(API_URL, headers=headers, json=data)
    response_json = response.json()

    if 'choices' not in response_json:
        print("Error in API response:", response_json)
        return None

    return response_json

#lets go grab some info
def analyze_system(system_info):
    prompt = f"Analyze the following Linux system information:\n\n{system_info}\n\nProvide any potential issues or recommendations:"
    response = openai_request(prompt)
    
    if response is None:
        return "An error occurred while analyzing the system information."

    analysis = response["choices"][0]["text"].strip()
    return analysis

def gather_system_info():
    system_info = f"Operating System: {platform.system()}\n"
    system_info += f"Platform: {platform.platform()}\n"
    system_info += f"Kernel Version: {platform.release()}\n"
    system_info += f"CPU Information: {os.popen('lscpu').read().strip()}\n"
    system_info += f"Memory Information: {os.popen('free -h').read().strip()}\n"
    system_info += f"Disk Usage: {os.popen('df -h').read().strip()}\n"
    system_info += f"Running Processes: {os.popen('ps aux').read().strip()}\n"
    
    return system_info

system_info = gather_system_info()
print("System Information:\n", system_info)

analysis = analyze_system(system_info)
print("\nAI Analysis:\n", analysis)

