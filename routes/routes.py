from fastapi import APIRouter
from typing import Any
from model.filmes import API_Filmes

router = APIRouter()

@router.get("/",
    summary="Página inicial",
    description="Retorna uma mensagem de boas-vindas à API de Filmes.",
    status_code=200)
def main_screen():
    return {"API": "Filmes"}

@router.get("/api_filmes/{movie_id}",
    summary="Consultar item por ID",
    description="Retorna um único item da tabela especificada com base no ID.",
    status_code=200,
    response_model=Any
)
def read_item (movie_id: int = None):
    api_filmes = API_Filmes(item={}, movie_id=movie_id)

    resultado = api_filmes.consultar()

    return resultado
    
@router.post("/api_filmes/",
    summary="Criar novo item",
    description="Insere um novo item na tabela especificada.",
    status_code=201,
    response_model=dict)
def create_item(item: dict):
    api_filmes = API_Filmes(item=item) 

    api_filmes.inserir()

    return {"message": "Item adicionado com sucesso!"}

@router.delete("/api_filmes/{movie_id}",
    summary="Deletar item",
    description="Remove um item da tabela com base no ID.",
    status_code=200,
    response_model=dict)
def delete_item(movie_id: int):
    api_filmes = API_Filmes(item={}, movie_id=movie_id)

    api_filmes.remover()

    return {"message": "Item deletado com sucesso!"}

@router.put("/api_filmes/{movie_id}",
    summary="Atualizar item",
    description="Atualiza os dados de um item na tabela especificada com base no ID.",
    status_code=200,
    response_model=dict)
def update_item(movie_id: int, item: dict):
    api_filmes = API_Filmes(item=item, movie_id=movie_id)   

    api_filmes.atualizar()

    return {"message": "Item atualizado com sucesso!"}