import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
VECTORSTORE_PATH = os.getenv("VECTORSTORE_PATH")