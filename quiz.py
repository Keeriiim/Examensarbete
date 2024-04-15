from questions import questions_data
from apiHandler import APIHandler
from dbHandler import Database
import time
import pymongo
class Quiz:
    PLAYER_SCORE = 0
    MAX_POINTS = 0


    def __init__(self):
        self.api = APIHandler()

        print('Welcome to the game!')
        player_score = 0


        # loop through every iteration for questions and answers
        for data in questions_data:
            print('Score = ' + str(player_score)+"/"+str(len(questions_data)))
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


    def game_log(self):
        print(Database.CURRENT_USER)
        print(str(self.PLAYER_SCORE)+"/"+str(self.MAX_POINTS))
        print(time.asctime())

        myClient = pymongo.MongoClient(Database.MYCLIENT_ADDRESS)
        dblist = myClient.list_database_names()
        self.DB = myClient["mydatabase"]
        if "mydatabase" in dblist:
            print("The database exists.")
        else:
            # Important: In MongoDB, a database is not created until it gets content!
            print(myClient.list_database_names())
            collist = self.DB.list_collection_names()
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


