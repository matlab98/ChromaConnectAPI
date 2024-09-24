import chromadb
from chromadb.config import Settings

setting = Settings(
    chroma_api_impl="rest",
    chroma_server_host= '192.168.1.11',
    chroma_server_http_port = 8001
)

client = chromadb.Client(setting)

client.get_version()
collection = client.get_collection(name="test")
est = collection.get(
    include=["documents"]
)

print(est)
