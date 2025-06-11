from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model='gpt-3.5-turbo-instruct')
result=llm.invoke('What is the capital of India')

print(result)

# LLMs - General-purpose models that is used for raw text generation.
# They take a string(or plain text) as input and returns a string(plain text).
# These are older models and are not used much now.