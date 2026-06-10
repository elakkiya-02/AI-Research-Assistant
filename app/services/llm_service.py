from ollama import chat
from app.config import MODEL_NAME
class LLMService():
    def __init__(self):
        #self.model_name = 'qwen3:4b'
        self.model_name = MODEL_NAME

    def generate_response(self, prompt:str)->str:
        response = chat(model =self.model_name,
                        messages=[{"role": "user",
                                   "content": prompt}])
        return response["message"]['content']