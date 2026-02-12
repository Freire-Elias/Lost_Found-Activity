class CriarItem:
    def __init__(self, item_repository, match_usecase):
        self.item_repository = item_repository
        self.match_usecase = match_usecase

    def executar(self, tipo, nome, descricao, categoria, local, data, id_usuario):
        item_id = self.item_repository.inserir(tipo, nome, descricao, categoria, local, data, id_usuario)
        item_salvo = self.item_repository.buscar_id(item_id)
        self.match_usecase.executar(item_salvo)

        return {"mensagem": "Item criado com sucesso"}