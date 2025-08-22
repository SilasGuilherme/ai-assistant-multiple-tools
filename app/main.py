from fastapi import FastAPI
from pydantic import BaseModel
from app.agents.router import create_agent

app = FastAPI()
agent = create_agent()


class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
async def ask(req: QuestionRequest):
    try:
        # Executa a pergunta usando o novo padrão
        result = agent.invoke({"input": req.question})
        # O resultado vem em dict; a resposta final fica em "output"
        return {"answer": result["output"]}
    except Exception as e:
        return {"error": str(e)}


@app.get("/")
def root():
    return {"message": "API do assistente está rodando!"}
