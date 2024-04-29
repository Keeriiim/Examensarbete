import socket
import threading
import time

from questions import questions_data
from apiHandler import API
from menuHandler import Menu

class Server:
    def __init__(self):
        self.host = '127.0.0.1'  # Localhost
        self.port = 12345  # Choose any available port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []  # List to store connected clients
        self.api = None  # Initialize API instance
        self.menu = Menu() # Initialize menu
        self.client_running = True
        self.lock = threading.Lock()  # Lock for thread safety

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        while self.client_running is True:
            self.accept_client()

    def accept_client(self):
        self.client_socket, client_address = self.socket.accept()
        print(f"Client {client_address} connected.")

        self.start_quiz()



    def start_quiz(self):
        self.api = API()

        # Pre game authentication
        player = self.menu.get_current_player()
        while player == "":
            self.client_auth()
            player = self.menu.get_current_player()

        print('We passed the Auth, now its time to play !!!!!!!!')
        intro_message = '**************** QUIZ ****************\n'\
                        'Answer the questions with true or false, if you want to end type quit.\n\n'
        self.client_message_only(intro_message)

        # Game loop:
        self.menu.set_amount_questions(len(questions_data))
        still_running = True
        while still_running is True:
            for i, data in enumerate(questions_data, start=1):
                question_text = f"Question {i}/{len(questions_data)} | Score:{self.menu.SCORE}/{len(questions_data)}\n{data['question']}"
                question_answer = data['answer']

                # Send & receive answer from client
                client_answer = self.client_communicator(question_text)

                print(f"Received answer from {self.client_socket.getpeername()}: {client_answer}")

                # Check if the answer matches the correct answer
                if client_answer.lower() == question_answer.lower():
                    # Increment score
                    self.menu.set_score()

            self.finished_quiz()
            still_running = False




    def finished_quiz(self):
        # Quiz ended, or game crashed - close the connection
        client_message = 'Congratz you finished the Quiz.' \
                         ' Type yes to save the game to the database?'
        self.client_message_only(client_message)
        try:
            client_response = self.client_socket.recv(1024).decode()
            if client_response.lower() == "yes":
                self.menu.post_game_log(self.api.TRIVIA_CATEGORY)

            self.client_message_only('Thanks for playing, type quit')
            self.client_running = False
        except ConnectionAbortedError:
            print("Connection aborted by the client.")




    def client_communicator(self,arg):
        try:
            self.client_socket.send(arg.encode())
            return self.client_socket.recv(1024).decode()
        except Exception as e:
            print(e)

    def client_message_only(self,arg):
        try:
            self.client_socket.send(arg.encode())
        except Exception as e:
            print(e)

    def client_auth(self):
        menu_questions = '********* Main Menu *********\n' \
                         '1. Create a player\n' \
                         '2. Log in as player\n' \
                         '****************************'


        # Send to client & receive answer
        client_answer = self.client_communicator(menu_questions)

        if client_answer in ('1','2'):   #== '1' or '2' or '3': will always be true !
            # Send the choice to menu class
            self.menu.switch_main_menu(client_answer, self.client_communicator, self.client_message_only)
        elif client_answer == 'quit':
            print('Exiting program')
            exit(0)

        else:
            self.client_auth()





if __name__ == "__main__":
    server = Server()
    server.start()


