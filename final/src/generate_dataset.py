import requests
import os
import time
import json
from openai import OpenAI
import random
import uuid

openrouter_key = os.environ.get("OPENROUTER_API_KEY")

def load_questions(path):
    with open(path , 'r') as f:
        questions = json.load(f)

    return questions


def get_model_response(question):
    # the code for calling the open router api was found in the open router website
    # https://openrouter.ai/x-ai/grok-3-mini/api

    client = OpenAI(    
        base_url="https://openrouter.ai/api/v1",
        api_key=openrouter_key,
    )

    completion = client.chat.completions.create(
        # model="x-ai/grok-3-mini",
        # model="google/gemini-2.5-flash-lite",
        model ="meta-llama/llama-3.2-3b-instruct",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    # print(completion.choices[0].message.content)
    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens
    cost = completion.usage.cost


    time.sleep(2)
    try:
        # this leaves a dns marker in the packet trace which helps differentiate
        # what packets go with what request
        # claude helped a little conceptually with this
        # https://claude.ai/share/bd26116f-d738-4598-8fbd-c551845a6d1e
        marker = f"{uuid.uuid4().hex}"
        print("makingdnsrequest")
        request = requests.get(f'https://{marker}.zephaniahdev.com/')
    except:
        pass
    time.sleep(2)

    return {
        'prompt_tokens': prompt_tokens,
        'completion_tokens': completion_tokens,
        'cost': cost
    }

def main():
    questions = load_questions('questions.json')
    labels = []

    for question in questions[:1000]:
        y = get_model_response(question)
        print(y)
        labels.append(y)

        with open("lamma.json", 'w') as f:
            json.dump(labels, f, indent=2)


if __name__ == "__main__":
    main()