from database.db_connection import execute_query

def initiate_game():
    start_response = input('Press ENTER to START')
    if start_response == "":
        print(art)


art = """ 
      
███████╗ ██████╗ ██╗         ██╗  ██╗███████╗██████╗  ██████╗ ███████╗███████╗
██╔════╝██╔═══██╗██║         ██║  ██║██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔════╝
███████╗██║   ██║██║         ███████║█████╗  ██████╔╝██║   ██║█████╗  ███████╗
╚════██║██║▄▄ ██║██║         ██╔══██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ╚════██║
███████║╚██████╔╝███████╗    ██║  ██║███████╗██║  ██║╚██████╔╝███████╗███████║
╚══════╝ ╚══▀▀═╝ ╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
                    
                    
                    Welcome to Hall of Digital Justice League
  
  1. Create a New Hero
  2. Read Hero Bio
  3. Update a Hero
  4. Be a Villain. Eliminate a hero
"""

def show_all_heroes():
     query = """
        SELECT name from heroes
     """
     hero_list = execute_query(query).fetchall()
     for num, value in enumerate(hero_list):
         print(f"{num + 1}: {value[0]}")
     return hero_list

def input_select_hero():
    show_all_heroes()
    hero_pick = input('Choose a hero to get to know...')
    select_a_hero(hero_pick)

def select_a_hero(pick):
     query = f"""
        SELECT
            id,
            name,
            about_me,
            biography
        FROM heroes
        WHERE heroes.id = {pick}; 
     """
     hero = execute_query(query).fetchall()
     for count, value in enumerate(hero):
        print(f"""
        {value[0]}: {value[1]}
        {value[2]}
        {value[3]}    
        """)

def main_menu():
    response = input("What would you like to do first? ")
    if response == '1':
        print(create_new_hero())
    elif response == "2":
        input_select_hero()
    elif response == '3':
        print(input_update_hero())
    elif response == '4':
        print(input_remove_hero())


# input_select_hero()

def hero_choice():
    response2 = input("Which hero would you like to know about? ")
    if response2 <= [6]:
        print(select_a_hero())
# hero_choice()

def create_new_hero(name, bio):
     query = """
        INSERT INTO patients (name, bio)
         VALUES (%s, %s)
     """
     execute_query(query, (name, bio))

# def remove_hero():
#         query = """
#             DELETE FROM heroes WHERE id = %s
#         """
#         id = 1
#         my_params = (id,) # trailing is needed to make it a tuple
#         execute_query(query, my_params) # params is no longer None but the value of my_params
#         delete_choice = my_params.int(input('Which hero do you wish to eliminate? '))
#         if delete_choice <= 6:


initiate_game()
