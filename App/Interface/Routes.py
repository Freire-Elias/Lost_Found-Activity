from fastapi import FastAPI

from App.Application.Item_usecase import CriarItem
from App.Application.match_usecase import MatchAutomatico
from App.Application.usuario_usecase import CriarUsuario
from App.Domain.models import Usuario, Item
from App.Infrastructure.match_repository import MatchRepository
from App.Infrastructure.usuario_repository import UsuarioRepository
from App.Infrastructure.item_repository import ItemRepository

app = FastAPI()

@app.post("/Usuarios")
def criar_usuario(dados: Usuario):
   repository = UsuarioRepository()
   use_case = CriarUsuario(repository)

   return use_case.executar(
       dados.nome,
       dados.telefone,
       dados.senha
   )

@app.post("/Itens")
def criar_item(dados: Item):
    item_repository = ItemRepository()
    match_repository = MatchRepository()

    match_usecase = MatchAutomatico(item_repository,match_repository)

    usecase = CriarItem(item_repository, match_usecase)

    return usecase.executar(
        dados.tipo,
        dados.nome,
        dados.descricao,
        dados.categria,
        dados.local,
        dados.data,
        dados.id_usuario
    )