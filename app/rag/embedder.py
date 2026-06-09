from langchain_ollama import OllamaEmbeddings

class Embedder:
    def __init__(self):
        self.embedding_model = OllamaEmbeddings(model='nomic-embed-text')

    def embed_documents(self, texts):
        return self.embedding_model.embed_documents(texts)