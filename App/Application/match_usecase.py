from App.Domain.models import MatchService

class MatchAutomatico:
    def __init__(self, item_repository, match_repository):
        self.item_repository = item_repository
        self.match_repository = match_repository

    def executar(self, item_novo):
        tipo_oposto = "achado" if item_novo["tipo"] == "perdido" else "perdido"
        sugestoes = self.item_repository.buscar_tipo(tipo_oposto)

        for sugestoes in sugestoes:
            if MatchService.sao_compativeis(item_novo, sugestoes):
                if item_novo["tipo"] == "perdido":
                    self.match_repository.criar_match(
                        item_novo["id_item"],
                        sugestoes["id_item"]
                    )
                else:
                    self.match_repository.criar_match(
                        sugestoes["id_item"],
                        sugestoes["id_item"]
                    )

class ListarMatchs:
    def __init__(self, repository):
        self.repository = repository

    def executar(self):
        return self.repository.listar_matchs()
