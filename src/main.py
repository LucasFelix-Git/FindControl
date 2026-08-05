from database import initialize_database, initialize_categories
from ui.menu import menu_principal

initialize_database()
initialize_categories()
print("Banco inicializado com sucesso!")

menu_principal()
