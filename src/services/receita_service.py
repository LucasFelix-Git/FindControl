import repositories.receita_repository as receita_repository
from repositories.categoria_repository import buscar_categoria_por_id
from repositories.usuario_repository import buscar_usuario_por_id

def cadastrar_receita(descricao: str, valor: float, id_usuario: int, id_categoria: int):

    if valor <= 0 or descricao.strip() == "":
        return False
    categoria = buscar_categoria_por_id(id_categoria)
    if categoria is None:
        return False
    usuario = buscar_usuario_por_id(id_usuario)
    if usuario is None:
        return False
    
    receita_repository.criar_receita(descricao,valor,id_usuario,id_categoria)
    return True

def listar_receita(id_usuario):
    listar_receitas = receita_repository.listar_receitas_usuario(id_usuario)
    return listar_receitas