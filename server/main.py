from fastapi import FastAPI
from agents.main_agent import MainAgent

app = FastAPI()

agent = MainAgent()

@app.post("/ask")
async def ask_question(question: str):
    response = agent.run(question)
    return {"response": response}

@app.get("/")
def root():
    return {"message": "Finance AI Agent rodando!"}
