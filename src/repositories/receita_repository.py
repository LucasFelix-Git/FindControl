from database import get_connection
from models.receita import Receita
from dto.historico_receita_dto import HistoricoReceitaDTO
from datetime import date

def criar_receita(descricao: str, valor: float, id_usuario: int ,id_categoria: int):
    data_receita = date.today()
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
        INSERT INTO receita (descricao, valor, data_receita, id_usuario, id_categoria)
        VALUES
        (? ,?, ?, ?, ?) """,
        (descricao, valor, data_receita, id_usuario, id_categoria)
    )
    connect.commit()
    connect.close()

def listar_receitas_usuario(id_usuario: int):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
        SELECT r.data_receita, r.descricao, r.valor, c.nome_categoria FROM receita AS r
        INNER JOIN categoria AS c
        ON r.id_categoria = c.id_categoria
        WHERE r.id_usuario =  ? """,
        (id_usuario,)
    )
    receita = cursor.fetchall()
    connect.close()
    lista_receita = []
    for i in receita:
        lista_receita.append(HistoricoReceitaDTO(*i))
    return lista_receita