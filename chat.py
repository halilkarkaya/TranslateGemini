from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes

load_dotenv()

# Get API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

model = ChatGoogleGenerativeAI(
    google_api_key=api_key,
    model="gemini-1.5-pro",  # Using the correct model name
    temperature=0.3,
)


system_prompt = "çeviri yap{language}"


prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{text}")
])
app = FastAPI(
    title="Çeviri uygulaması",
    description="diller arası çeviri yapan bir uygulama",
    version="1.0.0"

)
parser = StrOutputParser()
chain= prompt_template|model|parser
add_routes(app, chain, path="/chain")




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

