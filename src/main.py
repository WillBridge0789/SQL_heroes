from database.db_connection import execute_query

art = """ 
      
███████╗ ██████╗ ██╗         ██╗  ██╗███████╗██████╗  ██████╗ ███████╗███████╗
██╔════╝██╔═══██╗██║         ██║  ██║██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔════╝
███████╗██║   ██║██║         ███████║█████╗  ██████╔╝██║   ██║█████╗  ███████╗
╚════██║██║▄▄ ██║██║         ██╔══██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ╚════██║
███████║╚██████╔╝███████╗    ██║  ██║███████╗██║  ██║╚██████╔╝███████╗███████║
╚══════╝ ╚══▀▀═╝ ╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
                    
                    
                    Welcome to Hall of Digital Justice League
  
  1. Join our ranks
  2. Read Hero Bio
  3. Update a Hero
  4. Be a Villain. Eliminate a hero
"""
# Game start menu showing game name with a menu list 
def initiate_game():
    start_response = input('Press ENTER to START')
    if start_response == "":
        print(art)
        main_menu()
        
# Main menu options showing via "art" variable. Number input corresponds with which function will run.
def main_menu():
    response = input("What would you like to do first? ")
    if response == "1":
        input_create_hero()
    elif response == "2":
        input_select_hero()
    elif response == '3':
        print(input_update_hero())
    elif response == '4':
        print(input_remove_hero())

# Showing all heroes in heroes table by id numbers (ascending 1 - 6+)
def show_all_heroes():
     query = """
        SELECT name from heroes
     """
     hero_list = execute_query(query).fetchall()
     for num, value in enumerate(hero_list):
         print(f"{num + 1}: {value[0]}")
     return hero_list

# Shows the list of heroes and asks for user to type in a number corresponding with hero id number
def input_select_hero():
    show_all_heroes()
    hero_pick = input('Choose a hero to get to know...')
    select_a_hero(hero_pick)
    return_to_main_menu()

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
    
# Asking for user input for a new hero's NAME, ABOUT, and BIO 
def input_create_hero():
    name = input('We would be honored for you to join our ranks! What is your name? ')
    about = input('A pleasure to meet you, ' + name + '! Tell us a little about yourself. ')
    bio = input('Thats interesting! Tell us a little about your upbringing.... ')
    create_new_hero(name, about, bio)
    return_to_main_menu()

# Creates a new hero by user input being put into the heroes table
def create_new_hero(name, about, bio):
    query = """
        INSERT INTO heroes (name, about_me, biography)
         VALUES (%s, %s, %s)
    """
    execute_query(query, (name, about, bio))
    show_all_heroes()

# If user types ENTER, it will go back to the start(main menu) OR if they press BACK, it will go 
# back to list of heroes
def return_to_main_menu():
    answer = input("Press ENTER to return to the main menu OR type BACK to go back to our heroes: ")
    if answer == "": 
        print(art)
        print(main_menu())
    elif answer == "back".upper():
        print(input_select_hero())

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