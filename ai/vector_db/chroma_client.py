import chromadb
from chromadb.config import Settings
from core.config import settings

class ChromaDBManager:
    def __init__(self):
        try:
            self.client = chromadb.HttpClient(
                host=settings.CHROMA_HOST, 
                port=settings.CHROMA_PORT,
                settings=Settings(allow_reset=True)
            )
            print("Connected to ChromaDB")
        except Exception as e:
            print(f"Failed to connect to ChromaDB: {e}")
            self.client = None
            
    def get_collection(self, name: str):
        if not self.client:
            return None
        return self.client.get_or_create_collection(name)

chroma_manager = ChromaDBManager()
