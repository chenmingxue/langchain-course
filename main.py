from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
def main():
    print("Hello, LangChain!")
    print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
    

if __name__ == "__main__":
    main()