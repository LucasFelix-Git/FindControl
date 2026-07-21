from database import get_connection
from models.categoria import Categoria

def criar_categoria(nome_categoria: str):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO categoria (nome_categoria)
        VALUES
        (?)   """,
        (nome_categoria,)
    )
    connection.commit()
    connection.close()

def buscar_categoria_por_nome(nome_categoria: str):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id_categoria, nome_categoria FROM categoria
        WHERE nome_categoria = ? """, (nome_categoria,)
    )
    categoria = cursor.fetchone()
    connection.close()
    if categoria is None:
        return None
    categoria = Categoria(*categoria)
    return categoria

def buscar_categoria_por_id(id_categoria: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id_categoria, nome_categoria FROM categoria
        WHERE id_categoria = ? """, (id_categoria,)
    )
    categoria = cursor.fetchone()
    connection.close()
    if categoria is None:
        return None
    categoria = Categoria(*categoria)
    return categoria

def listar_categorias():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id_categoria, nome_categoria FROM categoria
""")
    categoria = cursor.fetchall()
    connection.close()
    lista_categoria = []
    for i in categoria:
        lista_categoria.append(Categoria(*i))
    return lista_categoria
