from langchain_ollama import OllamaEmbeddings
from app.config import EMBEDDING_MODEL

class Embedder:
    def __init__(self):
        #self.embedding_model = OllamaEmbeddings(model='nomic-embed-text')
        self.embedding_model = OllamaEmbeddings(model = EMBEDDING_MODEL)

    def embed_documents(self, texts):
        return self.embedding_model.embed_documents(texts)