from langchain_core.prompts import PromptTemplate

REASON_PROMPT = PromptTemplate(input_variables = ['question'],
                               template="""
                Available actions:

                1. calculator > For simple Arithmetic Operations (+,-,*,/)
                2.text_stats > For counting words/characters
                3. retrieve > For factual questions that require knowledge retrieval (Squad)

                Question: {question}

                Respond with only one word:

                calculator
                text_stats
                retrieve
                """)