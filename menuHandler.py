from dbHandler import Database
from quiz import Quiz
from webSocket import Server

class Menu:


    def __init__(self):
        self.db = Database() # Instantiate the DB class. They are not static.
        self.quiz = Quiz #
        self.server=Server() # Starts the Server
        self.run() # Runs the program





    def run(self): # Runs the main program
        menu_running = True
        while menu_running is True:
            game_running = True
            menu_running = self.switch_case()

            print(self.db.CURRENT_USER) # Troubleshooting

            # Auth verifier
            if self.db.CURRENT_USER != "":
                print('Welcome ' + self.db.CURRENT_USER)

                # Runs the main game
                while game_running is True:
                    game_running = self.switch_case_game()

            # Checks to see if the user wants to exit the game
            elif menu_running is False:
                exit('See ya next time!')
            # No need for recursion
            '''
            else:
                self.run()
            '''


    def switch_case(self): # Options for Main Menu
        print('********* Main Menu *********\n'
              '1. Create a player\n'
              '2. Log in as player\n'
              '3. Exit\n'
              '****************************')
        user = input('Choice: ')


        '''self.socket_handler(self,'********* Main Menu *********\n'
                            '1. Create a player\n'
                            '2. Log in as player\n'
                            '3. Exit\n'
                            '****************************')

        ''' 
        switcher = { # Simple switch statement
            "1": self.db.createPlayer, # Removing the () so that they are not executed immediately
            "2": self.db.logIn,
            "3": False # Works with False as well
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

        '''self.socket_handler('********* Game Menu *********\n' 
              '1. Singleplayer\n'
              '2. Multiplayer\n'
              '3. Back\n'
              '****************************')'''

        switcher = {  # Simple switch statement
            "1": self.quiz,  # Removing the () so that they are not executed immediately
            "2": self.server.start(),
            "3": False  # Works with False as well
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


    '''def socket_handler(self, input):

        self.server.inputHandler(input)'''



