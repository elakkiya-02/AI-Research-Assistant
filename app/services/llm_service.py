from ollama import chat
class LLMService():
    def __init__(self):
        self.model_name = 'qwen3:4b'

    def generate_response(self, prompt:str)->str:
        response = chat(model =self.model_name,
                        messages=[{"role": "user",
                                   "content": prompt}])
        return response["message"]['content']