from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

documents=[
    "Delhi is the capital of India",
    "Kolkata is the capital of India",
    "Hyderabad is the capital of Telangana"
]

result=embedding.embed_documents(documents)
print(result)