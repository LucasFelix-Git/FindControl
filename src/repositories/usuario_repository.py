from database import get_connection
from models.usuario import Usuario   

def criar_usuario(nome_usuario: str , senha: str) -> None:
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute ("""
        INSERT INTO usuario (nome_usuario, senha)
        VALUES
        (?, ?)      """,
        (nome_usuario, senha)
    )
    connection.commit()
    connection.close()

def buscar_usuario_por_nome (nome_usuario: str):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id_usuario, nome_usuario, senha FROM usuario
        WHERE nome_usuario = ? """, 
        (nome_usuario,)
    )
    usuario = cursor.fetchone()
    connection.close()
    if usuario is None:
        return None
    else:
        usuario = Usuario(*usuario)
        return usuario

def buscar_usuario_por_id (id_usuario: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id_usuario, nome_usuario, senha FROM usuario
        WHERE id_usuario = ? """, (id_usuario,)
    )
    usuario = cursor.fetchone()
    connection.close()
    if usuario is None:
        return None
    else:
        usuario = Usuario(*usuario)
        return usuario