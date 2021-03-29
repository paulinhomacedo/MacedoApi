from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from httpx import get

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("/docs")

@app.get("/busca_cep/{cep_id}")
def busca_cep(cep_id  = '05145901'):   
    response = get(f'https://cep.awesomeapi.com.br/{cep_id}').json()
    return response  

@app.get("/cotacao-moeda")
def cotacao_all():
    response = get('https://economia.awesomeapi.com.br/json/all').json()
    return response

@app.get("/cotacao-moeda/{id_moeda}")
def cotacao_moeda(id_moeda):
    response = get(f'https://economia.awesomeapi.com.br/json/all/{id_moeda}').json()
    return response
