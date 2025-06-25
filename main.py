import os
from dotenv import load_dotenv

load_dotenv()

if __name__=="__main__":
    print("Hello ReAct Langgraph with Function Calling!")
    print(os.environ["OPENAI_API_KEY"])