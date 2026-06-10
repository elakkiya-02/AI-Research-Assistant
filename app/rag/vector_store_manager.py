from langchain_community.vectorstores import FAISS
from app.config import VECTORSTORE_PATH

class VectorStoreManager:
    @staticmethod
    def save(vectorstore, path=VECTORSTORE_PATH):
        vectorstore.save_local(path)

    @staticmethod
    def load(embedding_model, path=VECTORSTORE_PATH):
        vectorstore = FAISS.load_local(path,
                                embedding_model,
                                allow_dangerous_deserialization=True)
        return vectorstore
    