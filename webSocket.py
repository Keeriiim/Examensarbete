import socket
import threading

from questions import questions_data
from apiHandler import API

class Server:
    def __init__(self):
        self.host = '127.0.0.1'  # Localhost
        self.port = 12345  # Choose any available port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []  # List to store connected clients
        self.api = None  # Initialize API instance
        self.quiz_started = False
        self.lock = threading.Lock()  # Lock for thread safety

    def start(self):
        self.socket.bind((self.host, self.port))
        #self.socket.listen(5)  # Allow up to 5 clients to queue
        self.socket.listen(1)
        self.accept_client()

    def accept_client(self):
        self.client_socket, client_address = self.socket.accept()
        print(f"Client {client_address} connected.")

        # Start the quiz once the client is connected
        self.start_quiz()

        '''print("Server started. Waiting for clients...")

        while True:
            client_socket, client_address = self.socket.accept()
            print(f"Client {client_address} connected.")

            # Handle each client in a separate thread
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()'''

    '''def handle_client(self, client_socket):
        with self.lock:
            self.clients.append(client_socket)
            if len(self.clients) == 2 and not self.quiz_started:
                self.start_quiz()

        while True:
            try:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                print(f"Received from {client_socket.getpeername()}: {data}")
            except ConnectionResetError:
                break

        with self.lock:
            self.clients.remove(client_socket)

        if not self.clients:
            self.quiz_started = False
            print("All clients disconnected. Server restarting...")
            exit()'''



    def start_quiz(self):
        self.api = API()
        self.quiz_started = True
        #for client_socket in self.clients:
        for data in questions_data:
            question_text = data['question']
            question_answer = data['answer']
            print(question_text)
            self.client_socket.send(question_text.encode())

            # Receive answer from client
            client_answer = self.client_socket.recv(1024).decode()
            print(f"Received answer from {self.client_socket.getpeername()}: {client_answer}")

            # Check if the answer matches the correct answer
            if client_answer.lower() == question_answer.lower():
                # Send confirmation message to the client
                self.client_socket.send("Correct!".encode())

        # Quiz ended, close the connection
        self.client_socket.close()
        print("Quiz ended. Connection closed.")

    '''def stop(self):
        for client_socket in self.clients:
            client_socket.close()
        self.socket.close()'''

if __name__ == "__main__":
    server = Server()
    server.start()


'''class Server:
    def __init__(self):
        self.host = '127.0.0.1'  # Localhost
        self.port = 12345  # Choose any available port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []  # List to store connected clients
        self.quiz = None  # Initialize quiz instance
        self.api = None # Initialize API instance

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)  # Allow up to 5 clients to queue
        print("Server started. Waiting for clients...")

        while True:
            client_socket, client_address = self.socket.accept()
            print(f"Client {client_address} connected.")
            self.clients.append(client_socket)

            # Start the quiz when the first client connects
            if len(self.clients) == 2:
                self.start_quiz()

    def start_quiz(self):
        # self.quiz = Quiz()
        self.api = API()
        # Send questions to clients
        for client_socket in self.clients:
            for data in questions_data:
                question_text = data['question']
                print(question_text)
                client_socket.send(question_text.encode())


    def stop(self):
        for client_socket in self.clients:
            client_socket.close()
        self.socket.close()

if __name__ == "__main__":
    server = Server()
    server.start()
'''



'''print('Score = ' + str(player_score) + "/" + str(len(questions_data)))
                print(data['question'])

                user1 = input('True / False ?: ')
                if user1.lower() == data['answer'].lower():
                    print('Correct!\n')
                    player_score += 1
                else:
                    print('Incorrect!\n')

            self.PLAYER_SCORE = player_score
            self.MAX_POINTS = len(questions_data)
            print(f'Ending score: {self.PLAYER_SCORE}')
            print()
            print('Thank you for playing the game!')


            questions = self.quiz.get_questions()  # Assume Quiz class has a method to get questions
            for question in questions:
                client_socket.send(question.encode())'''

