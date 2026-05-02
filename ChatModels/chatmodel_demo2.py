from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = 'claude-sonnet-4-6')

res = model.invoke('Wnat is the capital of India')

print(res.content)