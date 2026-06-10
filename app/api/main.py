from fastapi import FastAPI
from app.rag.embedder import Embedder
from app.rag.vector_store_manager import VectorStoreManager
from app.rag.retriever import Retriever
from app.agents.research_agent import ResearchAgent
from app.api.schema import QueryRequest, QueryResponse

app = FastAPI(title="AI Research Assistant", version="1.0.0")
embedder = Embedder()
vectorstore = VectorStoreManager.load(embedder.embedding_model)
retriever = Retriever(vectorstore)
agent = ResearchAgent(retriever)


@app.get("/")
def home():
    return{"message" : "AI Research Assistant API"}

@app.post("/ask", response_model=QueryResponse)
def ask(request:QueryRequest):
    answer = agent.invoke(request.question)
    return QueryResponse(question = request.question,
                         answer = answer)
