from app.rag.embedder import Embedder
from app.rag.vector_store_manager import VectorStoreManager
from app.rag.retriever import Retriever
from app.agents.research_agent import ResearchAgent

def test_agent():
    embedder = Embedder()
    vectorstore = VectorStoreManager.load(embedder.embedding_model)
    retriever = Retriever(vectorstore)
    agent = ResearchAgent(retriever)
    answer = agent.invoke("Who did the Virgin mary appear to??")
     
    assert "Bernadette" in answer
