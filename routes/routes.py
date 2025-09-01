from fastapi import APIRouter
from typing import Any
from model.filmes import API_Filmes

router = APIRouter()

@router.get("/",
    summary="Página inicial",
    description="Retorna uma mensagem de boas-vindas à API de Filmes.",
    status_code=200)
def main_screen():
    return {"Series": "Must Watch"}

@router.get("/api_filmes/{movie_id}",
    summary="Consultar item por ID",
    description="Retorna um único item da tabela especificada com base no ID.",
    status_code=200,
    response_model=Any
)
@router.get("/api_filmes/",
    summary="Consultar todos os itens",
    description="Retorna todos os registros da tabela especificada.",
    status_code=200,
    response_model=Any)
def read_item (item_id: int = None):
    api_filmes = API_Filmes(item={}, item_id=item_id)

    resultado = api_filmes.consultarSerie()

    return resultado
    
@router.post("/api_filmes/",
    summary="Criar novo item",
    description="Insere um novo item na tabela especificada.",
    status_code=201,
    response_model=dict)
def create_item(item: dict):
    api_filmes = API_Filmes(item=item) 

    api_filmes.inserirSerie()

    return {"message": "Item adicionado com sucesso!"}

@router.delete("/api_filmes/{movie_id}",
    summary="Deletar item",
    description="Remove um item da tabela com base no ID.",
    status_code=200,
    response_model=dict)
def delete_item(item_id: int):
    api_filmes = API_Filmes(item={}, item_id=item_id)

    api_filmes.removerSerie()

    return {"message": "Item deletado com sucesso!"}

@router.put("/api_filmes/{movie_id}",
    summary="Atualizar item",
    description="Atualiza os dados de um item na tabela especificada com base no ID.",
    status_code=200,
    response_model=dict)
def update_item(item_id: int, item: dict):
    api_filmes = API_Filmes(item=item, item_id=item_id)

    api_filmes.atualizarSerie()

    return {"message": "Item atualizado com sucesso!"}