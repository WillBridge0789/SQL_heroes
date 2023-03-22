from database.db_connection import execute_query

art = """ 
      
███████╗ ██████╗ ██╗         ██╗  ██╗███████╗██████╗  ██████╗ ███████╗███████╗
██╔════╝██╔═══██╗██║         ██║  ██║██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔════╝
███████╗██║   ██║██║         ███████║█████╗  ██████╔╝██║   ██║█████╗  ███████╗
╚════██║██║▄▄ ██║██║         ██╔══██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ╚════██║
███████║╚██████╔╝███████╗    ██║  ██║███████╗██║  ██║╚██████╔╝███████╗███████║
╚══════╝ ╚══▀▀═╝ ╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
                                                                              
  
"""

def select_all_heroes():
    
     query = """
        SELECT name from heroes
     """
     hero_list = execute_query(query).fetchall()
     for num, value in enumerate(hero_list):
         print(f"{num + 1}: {value[0]}")
     return hero_list

def main_menu():
    response = input("Welcome! Would you like to see out heroes? y or n ")
    if response == 'y':
        print(select_all_heroes())
main_menu()
