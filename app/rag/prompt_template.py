from langchain_core.prompts import PromptTemplate

RAG_PROMPT = PromptTemplate(input_variables=['context','question'],
                            template = """ You are an AI research Assistant.
                            Use ONLY the provided context to answer the question.input_types=
                            Context:
                            {context}

                            Question:
                            {question}

                            Provide a concise answer:
                            """)
