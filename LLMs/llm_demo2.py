import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
)

user_input = input("Enter your prompt: ")

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V4-Pro:novita",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ],
)

print(completion.choices[0].message.content)

