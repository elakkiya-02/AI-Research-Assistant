from langchain_core.prompts import PromptTemplate

TOOL_PROMPT = PromptTemplate(input_variables=['context', 'question'],
                             template="""You are an assistant.

                             Tool Output:
                             {context}

                             Original Question:
                             {question}

                             Answer briefly and directly. 
                             Do not explain unnecessarily
                             """)