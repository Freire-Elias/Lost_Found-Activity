from fastapi import FastAPI
from fastapi import HTTPException

from App.Application.Item_usecase import CriarItem, ListarItens
from App.Application.match_usecase import MatchAutomatico, ListarMatchs
from App.Application.usuario_usecase import CriarUsuario, LoginUsuario
from App.Domain.models import Usuario, Item, LoginUsuarioSchema
from App.Infrastructure.match_repository import MatchRepository
from App.Infrastructure.usuario_repository import UsuarioRepository
from App.Infrastructure.item_repository import ItemRepository
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/usuarios")
def criar_usuario(dados: Usuario):
   repository = UsuarioRepository()
   use_case = CriarUsuario(repository)

   return use_case.executar(
       dados.nome,
       dados.telefone,
       dados.senha
   )

@app.post("/login")
def login_usuario(dados: LoginUsuarioSchema):
    repository = UsuarioRepository()
    usecase = LoginUsuario(repository)

    usuario = usecase.executar(dados.telefone, dados.senha)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    return {
        "id_usuario": usuario["id_usuario"],
        "nome": usuario["nome"]
    }


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
        dados.categoria,
        dados.local,
        dados.data,
        dados.id_usuario
    )

@app.get("/Itens")
def listar_itens():
    repository = ItemRepository()
    usecase = ListarItens(repository)
    return usecase.executar()

@app.get("/match")
def listar_matchs():
    repository = MatchRepository()
    usecase = ListarMatchs(repository)
    print(usecase.executar())
    return usecase.executar()