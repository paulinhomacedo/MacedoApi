from fastapi import FastAPI
from httpx import get

app = FastAPI()


@app.get("/")
async def root():
    return {"mensagem": "Consulte a Documentacao em /docs"}

@app.get("/busca_cep/{cep_id}")
def busca_cep(cep_id  = '05145901'):   
    response = get(f'https://cep.awesomeapi.com.br/{cep_id}').json()
    return response  
