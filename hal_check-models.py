#imports
import os
import platform
import requests
import json
from decouple import config
import openai

#api key
openai.api_key = config('API_KEY')

def list_models():
    try:
        response = openai.Model.list()
        models = response['data']
        return models
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    available_models = list_models()
    if available_models:
        print("Available Models:")
        for model in available_models:
            print(f"ID: {model.id}, Name: {model.id}")
    else:
        print("No models found.")

if __name__ == "__main__":
    main()
