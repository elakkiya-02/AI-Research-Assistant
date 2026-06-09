from app.services.llm_service import LLMService

class RAGChain:
    def __init__(self, retriever):
        self.retriever = retriever
        self.llm = LLMService()
        
    def generate_answer(self, query:str):
        retrieved_docs = self.retriever.retrieve(query)
        context="\n\n".join(doc.page_content for doc in retrieved_docs)
        prompt = f""" Use the provided context to answer the question.
        Context: 
        {context}
        Question:
        {query}
        Answer:
        """
        return self.llm.generate_response(prompt)
