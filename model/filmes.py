from model.database import Database
from fastapi import HTTPException

db = Database()

class API_Filmes:
    def __init__(self, movie_id: int = None, searchTerm: str = None, poster_url: str = None, count: int = None, item: dict = None):
        self.movie_id = movie_id
        self.searchTerm = searchTerm
        self.poster_url = poster_url
        self.count = count
        self.item = item

    def consultar(self):
        db.conectar()
        try:
            if self.movie_id is None:
                sql = "SELECT * FROM api_filmes"
                params = ()
            else:
                sql = "SELECT * FROM api_filmes WHERE movie_id = %s"
                params = (self.movie_id,)
            resultado = db.executar_consulta(sql, params, fetch=True)
            if not resultado:
                raise HTTPException(status_code=404, detail="Item não encontrado")
            return resultado
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao consultar o banco de dados: {str(e)}")
        finally:
            db.desconectar()

    def inserir(self):
        """Adiciona um item a uma tabela específica no banco de dados."""
        db.conectar()

        try:
            if not self.item:
                raise HTTPException(status_code=400, detail="Nenhum dado fornecido para adicionar")
            # Erro 400: Bad Request

            colunas = ', '.join(self.item.keys()) 
            # para cada chave do dicionário, cria uma string separada por vírgula
            valores = ', '.join(['%s'] * len(self.item)) 
            # para cada valor do dicionário, cria uma string no formato "%s", separando por vírgula. .join = juntar strings
            sql = f"INSERT INTO api_filmes ({colunas}) VALUES ({valores})"
            params = tuple(self.item.values())

            db.executar_consulta(sql, params)
            db.desconectar()
        
        except Exception as e:
            db.desconectar()
            raise HTTPException(status_code=500, detail=f"Erro ao adicionar o item: {str(e)}")
            # Erro 500: Internal Server Error
        
    def remover(self):
        '''Remove um item de alguma lista do banco de dados'''
        db.conectar()

        try:
            if self.movie_id is None:
                raise HTTPException(status_code=403, detail="Mudança não permitida (Não foi atribuído um ID)")
                # Erro 403: Forbidden

            sql = "DELETE FROM api_filmes WHERE movie_id = %s"
            params = (self.movie_id,)

            db.executar_consulta(sql, params)
            db.desconectar()

        except Exception as e:
            db.desconectar()
            raise HTTPException(status_code=500, detail=f"Erro ao remover o item: {str(e)}")
        
    def atualizar(self):
        '''Atualiza um item de alguma lista do banco de dados'''
        db.conectar()

        try:
            if self.movie_id is None:
                raise HTTPException(status_code=403, detail="Mudança não permitida (Não foi atribuído um ID)")
                # Erro 403: Forbidden
            if not self.item:
                raise HTTPException(status_code=400, detail="Nenhum dado fornecido para atualização")
                # Erro 400: Bad Request
            
            set_clause = ", ".join([f"{key} = %s" for key in self.item.keys()]) 
            # para cada chave do dicionário, cria uma string no formato "chave = %s", separando por vírgula
            sql = f"UPDATE api_filmes SET {set_clause} WHERE movie_id = %s"
            params = tuple(self.item.values()) + (self.movie_id,)

            db.executar_consulta(sql, params)
            db.desconectar()
        except Exception as e:
            db.desconectar()
            raise HTTPException(status_code=500, detail=f"Erro ao atualizar o item: {str(e)}")