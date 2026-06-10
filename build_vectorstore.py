from app.ingestion.squad_loader import SquadLoader
from app.rag.chunker import Chunker
from app.rag.embedder import Embedder
from app.rag.vector_store import VectorStore
from app.rag.vector_store_manager import VectorStoreManager
from app.logger import logger

loader = SquadLoader()
documents = loader.load_documents()

chunker = Chunker()
chunks = chunker.split_documents(documents[:100])

embedder = Embedder()

store = VectorStore()

vectorstore = store.create_vectorstore(chunks, embedder.embedding_model)
VectorStoreManager.save(vectorstore)
print("Vector Store saved successfully")
logger.info("Vector Store saved successfully")