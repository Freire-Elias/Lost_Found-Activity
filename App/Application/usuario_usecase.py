class CriarUsuario:
    def __init__(self, repository):
        self.repository = repository

    def executar(self, nome, telefone, senha):
        self.repository.inserir(nome, telefone, senha)
        return {"mensagem": "Usuário criado com sucesso"}

