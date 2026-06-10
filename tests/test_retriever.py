from app.rag.embedder import Embedder
from app.rag.vector_store_manager import VectorStoreManager
from app.rag.retriever import Retriever

def test_retriever():
    embedder = Embedder()
    vectorstore = VectorStoreManager.load(embedder.embedding_model)
    retriever = Retriever(vectorstore)

    docs = retriever.retrieve("Who did the Virgin Mary appear to?")
    assert len(docs)>0