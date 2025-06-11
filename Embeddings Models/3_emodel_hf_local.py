from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents=[
    "Delhi is the capital of India",
    "Kolkata is the capital of India",
    "Hyderabad is the capital of Telangana"
]

result=embedding.embed_documents(documents)

print(str(result))