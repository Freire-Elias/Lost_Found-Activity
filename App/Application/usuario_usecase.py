class CriarUsuario:
    def __init__(self, repository):
        self.repository = repository

    def executar(self, nome, telefone, senha):
        self.repository.inserir(nome, telefone, senha)
        return {"mensagem": "Usuário criado com sucesso"}

class LoginUsuario:

    def __init__(self, repository):
        self.repository = repository

    def executar(self, telefone, senha):
        usuario = self.repository.buscar_telefone(telefone)

        if not usuario:
            return None

        if usuario["senha"] != senha:
            return None

        return usuario


