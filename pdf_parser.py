from langchain_community.document_loaders import PyPDFLoader

class PDFParser:
    def load_pdf(self, pdf_path:str):
        loader = PDFParser(pdf_path)
        documents=loader.load()
        return documents