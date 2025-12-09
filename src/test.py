import requests
import os

openrouter_key = os.environ.get("OPENROUTER_API_KEY")


# the code for calling the open router api was found in the open router website
# https://openrouter.ai/x-ai/grok-3-mini/api
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=openrouter_key,
)

completion = client.chat.completions.create(
  model="x-ai/grok-3-mini",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)

# print(completion.choices[0].message.content)
print(completion.usage.prompt_tokens)
print(completion.usage.completion_tokens)
print(completion.usage.cost)