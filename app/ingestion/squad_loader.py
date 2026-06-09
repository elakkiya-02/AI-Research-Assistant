from datasets import load_dataset
from langchain_core.documents import Document

class SquadLoader:
    def load_documents(self):
        dataset = load_dataset("rajpurkar/squad")
        documents=[]
        for row in dataset["train"]:
            document = Document(page_content=row["context"],
                                metadata={"id": row["id"],
                                          "title": row["title"]
                                          })
            documents.append(document)
        return documents