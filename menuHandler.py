from dbHandler import Database
from quiz import Quiz

class Menu:


    def __init__(self):
        self.db = Database() # Instantiate the DB class. They are not static.
        self.quiz = Quiz
        self.run() # Runs the program




    def run(self): # Runs the main program
        menu_running = True
        while menu_running is True:
            game_running = True
            menu_running = self.switch_case()
            print('Welcome ' + self.db.CURRENT_USER)

            while game_running is True:
               game_running = self.switch_case_game()


    def switch_case(self): # Options for Main Menu
        print('********* Main Menu *********\n'
              '1. Create a player\n'
              '2. Log in as player\n'
              '3. Exit\n'
              '****************************')
        user = input('Choice: ')


        switcher = { # Simple switch statement
            "1": self.db.createPlayer, # Removing the () so that they are not executed immediately
            "2": self.db.logIn,
            "3": None # Works with False as well
        }
        result = switcher.get(user, self.default_switcher) # Saves the function to result if 1-3 or default
        if callable(result):
            result() # Calls the function
            return True
        else:
            print('Exiting program')
            return False

    def switch_case_game(self):  # Options for Main Menu
        print('********* Game Menu *********\n' 
              '1. Singleplayer\n'
              '2. Multiplayer\n'
              '3. Back\n'
              '****************************')
        user = input('Choice: ')

        switcher = {  # Simple switch statement
            "1": self.quiz,  # Removing the () so that they are not executed immediately
            "2": None,
            "3": None  # Works with False as well
        }
        result = switcher.get(user, self.default_switcher)  # Saves the function to result if 1-3 or default
        if callable(result):
            result()  # Calls the function
            return True
        else:

            return False


    def default_switcher(self): # Default print if something goes wrong
        print('You need to choose 1-3\n')
        self.switch_case()
