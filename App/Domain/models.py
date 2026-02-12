from pydantic import BaseModel

class Usuario(BaseModel):
    nome: str
    telefone: str
    senha: str

class LoginUsuarioSchema(BaseModel):
    telefone: str
    senha: str

class Item(BaseModel):
    tipo: str
    nome: str
    descricao: str
    categoria: str
    local: str
    data: str
    id_usuario: int
    
class MatchService:
    @staticmethod
    def sao_compativeis(item1, item2):
        return (
            item1["categoria"] == item2["categoria"] and
            item1["local"] == item2["local"] and
            item1["tipo"] != item2["tipo"]
        )

