import requests


# the code for calling the open router api was found in the open router website
# https://openrouter.ai/x-ai/grok-3-mini/api
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
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

print(completion.choices[0].message.content)