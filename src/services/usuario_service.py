from repositories.usuario_repository import criar_usuario, buscar_usuario_por_nome

def autenticar_usuario (nome_usuario: str, senha: str):
    
    usuario = buscar_usuario_por_nome(nome_usuario)
    
    if usuario is None:
        return None
    if senha !=  usuario.senha:
        return None
    return usuario

def cadastrar_usuario(nome_usuario: str, senha: str) -> bool:

    usuario = buscar_usuario_por_nome(nome_usuario)

    if usuario is not None:
        return False

    criar_usuario(nome_usuario, senha)

    return True