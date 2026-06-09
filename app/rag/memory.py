class ConversationMemory:
    def __init__(self):
        self.history=[]
    def add_message(self, role, content):
        self.history.appen({'role': role,
                            'content': content})
    def get_history(self):
        return self.history