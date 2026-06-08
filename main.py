from app.services.llm_service import LLMService

def main():
    llm = LLMService()
    print("AI Research Assistant")
    print("Type exit to quit.\n")

    while True:
        query = input("You...")
        if query.lower()=='exit':
            break
        response = llm.generate_response(query)
        print("\nAssistant: ")
        print(response)
        print()

if __name__=="__main__":
    main()