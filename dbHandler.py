import pymongo
import time
class Database:
    #MYCLIENT_ADDRESS = "mongodb://admin:admin@172.18.0.2:27016/"
    MYCLIENT_ADDRESS = "mongodb://admin:admin@localhost:27016/"
    DB = ""
    CURRENT_USER =""

    def __init__(self):
        self.dbConnect() # Initializes the DB if there is none


    def dbConnect(self):
        myClient = pymongo.MongoClient(self.MYCLIENT_ADDRESS)
        dblist = myClient.list_database_names()
        self.DB = myClient["mydatabase"]
        collist = self.DB.list_collection_names()

        if "mydatabase" not in dblist:
            self.create_default_collections()

    def create_default_collections(self):
        players_col = self.DB["players"]
        default_player = {
            "username": "Admin",
            "password": "Admin"
        }
        players_col.insert_one(default_player)

        game_logs_col = self.DB["game_logs"]
        default_log = {
            "username": "Admin",
            "score": "0",
            "subject": "Initiation",
            "time": time.asctime()
        }
        game_logs_col.insert_one(default_log)




    def createPlayer(self, client_communicator, client_message_only):
        client_message_username = '***** Create new player *****\n'\
                         'Enter UserName: '

        client_response_username = client_communicator(client_message_username)

        if self.DB['players'].find_one({
            "username":client_response_username
        }):
            user_already_exists_error = 'UserName already exists, type ok to continue'
            client_message_only(user_already_exists_error)

        else:
            client_message_password = 'New password: '
            client_response_password = client_communicator(client_message_password)

            self.DB['players'].insert_one({
                "username": client_response_username,
                "password": client_response_password
            })
            successfully_created_user = f'Successfully created {client_response_username}, type ok to continue\n'
            client_message_only(successfully_created_user)
            print(f'Successfully created {client_response_username}')

    def logIn(self, client_communicator, client_message_only):
        client_message_username = '********** Log In **********\n'\
                                  'Enter UserName: '

        client_response_username = client_communicator(client_message_username)

        client_message_password = 'Enter Password: '

        client_response_password = client_communicator(client_message_password)



        user = self.DB['players'].find_one({
            "username": client_response_username,
            "password": client_response_password
        })

        if user is not None:
            log_in_success = 'LogIn Successfull!, type ok to continue'
            client_message_only(log_in_success)
            self.CURRENT_USER = client_response_username
        else:
            print('Wrong UserName or Password')
            log_in_error = 'Wrong UserName or Password, type ok to continue'
            client_message_only(log_in_error)




    def game_log(self, score, amount, category):
        game_logs_col = self.DB["game_logs"]
        user = self.CURRENT_USER

        new_log = {
            "username": self.CURRENT_USER,
            "score": str(score) + ' / ' + str(amount),
            "subject": "any",
            "time": time.asctime()
        }

        print(new_log)
        #game_logs_col.insert_one(new_log)







