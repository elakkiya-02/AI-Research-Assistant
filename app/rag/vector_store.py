from langchain_community.vectorstores import FAISS

class VectorStore:
    def create_vectorstore(self, chunks, embedding_model):
        vectorstore = FAISS.from_documents(documents=chunks,
                                           embedding=embedding_model)
        return vectorstore