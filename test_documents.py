""" from app.ingestion.squad_loader import SquadLoader

loader = SquadLoader()
documents = loader.load_documents()
print(type(documents))
print(len(documents))
print(documents[0]) """

""" from app.rag.chunker import Chunker
chunker =Chunker()
chunks = chunker.split_documents(documents[:5])
print("Documents ", len(documents[:5]))
print("Chunk ",len(chunks))
print("\n1st CHUNK:")
print(chunks[0].page_content)
print("\nMETADATA:")
print(chunks[0].metadata) """

""" #embeddings
from app.rag.embedder import Embedder
embedder = Embedder()
vectors = embedder.embed_documents(['Machine learning is a branch of AI',
                                    'Deep Learning uses Neural Network'])
print(type(vectors))
print(len(vectors))
print("Vector Dimension ", len(vectors[0])) """
"""
#VECTOR STORE
from app.ingestion.squad_loader import SquadLoader
from app.rag.chunker import Chunker
from app.rag.embedder import Embedder
from app.rag.vector_store import VectorStore
from app.rag.retriever import Retriever
from app.rag.rag_chain import RAGChain

loader = SquadLoader()
documents = loader.load_documents()

chunker = Chunker()
chunks = chunker.split_documents(documents[:20])

embedder = Embedder()

store = VectorStore()
vectorstore = store.create_vectorstore(chunks = chunks,
                                       embedding_model = embedder.embedding_model)
retriever = Retriever(vectorstore)
#results = retriever.retrieve("Who did the viegin mary appear to?")
print("retrieved doc: ", len(results))
print("1st result\n")
print(results[0].page_content)
print("\n Metadata")
#print(results[0].metadata)
rag = RAGChain(retriever)
answer = rag.generate_answer("Who did the virgin mary appear to?")

print(answer)"""
"""
from app.tools.calculator_tool import calculator_tool
print(calculator_tool("25+5"))
print(calculator_tool("10*3"))"""

#testing agents
from app.ingestion.squad_loader import SquadLoader
from app.rag.chunker import Chunker
from app.rag.embedder import Embedder
from app.rag.vector_store import VectorStore
from app.rag.retriever import Retriever
from app.agents.research_agent import ResearchAgent
from app.rag.vector_store_manager import VectorStoreManager
from pathlib import Path

#following runs
if Path("vectorstore/index.faiss").exists():
    vectorstore = VectorStoreManager.load(embedding_model=embedder.embedding_model)
else:
    loader = SquadLoader()
    documents = loader.load_documents()
    chunker = Chunker()
    chunks = chunker.split_documents(documents[:20])
    embedder = Embedder()
    store = VectorStore()
#first run
    vectorstore = store.create_vectorstore(chunks,
                                       embedder.embedding_model)
    VectorStoreManager.save(vectorstore)
    print("Vector Store saved....")
    
retriever = Retriever(vectorstore)
agent = ResearchAgent(retriever)
print(agent.invoke("20/5"))
print("\n")
#print(agent.invoke("Who did the Virgin Mary appear to?"))
#print("\n")
print(agent.invoke("count words Learning Multiple tool iteration.."))
#print(answer)