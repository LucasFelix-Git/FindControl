import repositories.categoria_repository as categoria_repository

def cadastrar_categoria(nome_categoria: str) -> bool:
    nome_categoria = nome_categoria.strip().title()
    categoria = categoria_repository.buscar_categoria_por_nome(nome_categoria)
    if len(nome_categoria) < 3:
        return False
    
    if categoria is None:
        categoria_repository.criar_categoria(nome_categoria)
        return True
    
    return False

def listar_categoria():
    lista_categoria = categoria_repository.listar_categorias()
    return lista_categoria

def buscar_categoria_por_id(id_categoria: int):
    categoria = categoria_repository.buscar_categoria_por_id(id_categoria)
    return categoria