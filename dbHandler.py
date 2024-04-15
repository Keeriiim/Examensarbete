import pymongo
import time
class Database:
    MYCLIENT_ADDRESS = "mongodb://localhost:27017/"
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
                "score": "TEST",
                "subject": "TEST",
                "time": time.asctime()
            }
            game_logs_col.insert_one(default_log)
        '''
        if "mydatabase" in dblist:
            print("The database exists.")
        else:
            # Important: In MongoDB, a database is not created until it gets content!
            print(myClient.list_database_names())
            if "players" in collist:
                print("The collection exists.")
            else:
                # Important: In MongoDB, a collection is not created until it gets content!
                mycol = self.DB["players"]
                defualt_account = {
                    "username": "Admin",
                    "password": "Admin"
                }
                mycol.insert_one(defualt_account)
                self.DB = myClient["mydatabase"]
        if "game_logs" in collist:
            print("The collection exists.")
        else:
            # Important: In MongoDB, a collection is not created until it gets content!
            mycol = self.DB["game_logs"]
            defualt_account = {
                "username": "Admin",
                "score": "TEST",
                "subject": "TEST",
                "time": time.asctime()
            }
            mycol.insert_one(defualt_account)
            '''





    def createPlayer(self):
        print('\n***** Create new player *****')
        userName = input('UserName: ')

        if self.DB['players'].find_one({
            "username":userName
        }):
            print('UserName already exists, try again')
            self.createPlayer()
        else:
            password = input('Password: ')

            self.DB['players'].insert_one({
                "username": userName,
                "password": password
            })
            print(f'Successfully created {userName}')

    def logIn(self):
        print('\n********** Log In **********')
        username = input('UserName: ')
        password = input('Password: ')
        print('****************************')


        user = self.DB['players'].find_one({
            "username": username,
            "password": password
        })

        if user is not None:
            print('LogIn Successfull!\n')
            self.CURRENT_USER = username
        else:
            print('Wrong UserName or Password')
            self.logIn()


# Behöver hantera websocket för multiplayers !
# Kommer skicka in infon i databasen gällande game







