from services.usuario_service import autenticar_usuario, cadastrar_usuario
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
            print("Entrou em Adicionar Receita")
        
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

menu_principal()
