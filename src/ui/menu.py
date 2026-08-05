from services.usuario_service import autenticar_usuario, cadastrar_usuario
from services.categoria_service import cadastrar_categoria, buscar_categoria_por_id, listar_categoria
from services.receita_service import cadastrar_receita, listar_receita
from models.usuario import Usuario


def menu_principal():
    while True:
        print("""

    ========================
        FinControl
    ========================

    1 - Login

    2 - Criar usuário

    3 - Sair""")
        
        number = int(input("Escolha uma opção: "))

        if number == 1:
            
            nome_usuario = input("Nome: ")
            senha = input("Senha: ")
            
            usuario = autenticar_usuario(nome_usuario, senha)
            if usuario is None:
                print("Usuário ou senha inválidos.")
            else:
                menu_usuario(usuario)
                
        
        elif number == 2:
            
            nome_usuario = input("Nome: ")
            senha = input("Senha: ")

            sucesso = cadastrar_usuario(nome_usuario, senha)
            if sucesso is True:
                print("✔ Usuário criado com sucesso!")
            else:
                print("Nome em uso!")
        elif number == 3:
            print("Saindo...")
            break
        else:
            print("Opção invalida")

def menu_usuario(usuario: Usuario):
    while True:
    
        print(f"""
    ========================
    Olá, {usuario.nome_usuario}
    ========================

    1 - Adicionar Receita

    2 - Adicionar Despesa

    3 - Ver Saldo

    4 - Histórico

    5 - Logout
        """)
        number = int(input("Escolha uma opção: "))
    
        if number == 1:
            descricao = input("Digite uma Descrição: ")
            valor = float(input("Digite o Valor: "))

            mostrar_categorias()
            
            id_categoria = int(input("Escolha uma categoria: "))

            if id_categoria == 0:
                nova_categoria = input("Nome da nova Categoria: ")
                sucesso = cadastrar_categoria(nova_categoria)
                if sucesso == True:
                    print("categoria criada com sucesso")
                    mostrar_categorias()
                else:
                    print("Categoria existente ou menos de 3 caracteres")

            receita = cadastrar_receita(descricao, valor, usuario.id_usuario, id_categoria)

            if receita == False:
                print("Não foi possivel registar a receita, verifique suas informações novamente")
            else:
                print("✔ Receita criada com sucesso!")


        
        elif number == 2:
            print("Entrou em Adicionar Despesas")
            
        elif number == 3:
            print("Entrou em Ver Saldo")
            
        elif number == 4:
            print("Entrou em Histórico")

        elif number == 5:
            print("Saindo...")
            break

        else:
            print("Opção invalida")

def mostrar_categorias():
    categorias = listar_categoria()

    for categoria in categorias:
        print(f"{categoria.id_categoria} - {categoria.nome_categoria}")

    print("0 - Criar Categoria")
    
menu_principal()
