from langchain_core.prompts import PromptTemplate

RAG_PROMPT = PromptTemplate(input_variables=['context','question'],
                            template = """ Use the provided context to answer the question.input_types=
                            Context:
                            {context}

                            Question:
                            {question}

                            Answer:
                            """)
