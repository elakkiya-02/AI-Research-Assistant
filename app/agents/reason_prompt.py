from langchain_core.prompts import PromptTemplate

REASON_PROMPT = PromptTemplate(input_variables = ['question'],
                               template="""
                Available actions:

                calculator
                text_stats
                retrieve

                Question: {question}

                Respond with only one action name
                """)