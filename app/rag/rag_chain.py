from app.services.llm_service import LLMService
from app.rag.prompt_template import RAG_PROMPT

class RAGChain:
    def __init__(self, retriever):
        self.retriever = retriever
        self.llm = LLMService()

    def generate_answer(self, query:str):
        retrieved_docs = self.retriever.retrieve(query)
        context="\n\n".join(doc.page_content for doc in retrieved_docs)
        prompt = RAG_PROMPT.format(context = context,
                                   question = query)
        return self.llm.generate_response(prompt)
