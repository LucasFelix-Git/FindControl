class Receita:
    def __init__(self,id_receita: int,descricao: str, valor:float, data_receita: str, id_categoria: int, id_usuario: int):
        self.id_receita = id_receita
        self.descricao = descricao
        self.valor = valor
        self.data_receita = data_receita
        self.id_categoria = id_categoria
        self.id_usuario = id_usuario