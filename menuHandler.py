from dbHandler import Database


class Menu:
    AMOUNT_QUESTIONS = 0
    SCORE = 0

    def __init__(self):
        self.db = Database() # Instantiate the DB class. They are not static.
        # self.quiz = Quiz #

    def switch_main_menu(self, arg, client_communicator, client_message_only): # Options for Main Menu

        switcher = { # Simple switch statement
            "1": self.db.createPlayer, # Removing the () so that they are not executed immediately
            "2": self.db.logIn
        }
        result = switcher.get(arg) # Saves the function to result if 1-3 or default
        if callable(result):
            result(client_communicator, client_message_only) # Calls the function
            return True
        else:
            return False

    def get_current_player(self):
        return self.db.CURRENT_USER

    def set_amount_questions(self, amount):
        self.AMOUNT_QUESTIONS = amount

    def set_score(self):
        self.SCORE = self.SCORE + 1


    def post_game_log(self, category):
        self.db.game_log(self.SCORE,self.AMOUNT_QUESTIONS,category)


























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



