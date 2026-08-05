class HistoricoReceitaDTO:
    def __init__(self, descricao: str, valor: float, data_receita: str, nome_categoria: str):
        self.descricao = descricao
        self.valor = valor
        self.data_receita = data_receita
        self.nome_categoria = nome_categoria