class Retriever:
    def __init__(self, vectorstore):
        self.retriever = vectorstore.as_retriever(search_kwargs={'k':3})

    def retrieve(self, query):
        return self.retriever.invoke(query)