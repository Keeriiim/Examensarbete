import requests # # Run pip install requests to get the library, then import to make POST requests
import json # Needed for json.loads()


class APIHandler:
    # Class attributes
    TRIVIA_AMOUNT=""           # Amount of question in the game
    TRIVIA_CATEGORY=""         # Game category
    TRIVIA_DIFFICULTY = ""     # Game difficulty
    TRIVIA_TYPE="boolean"      # Guessing type for the game - True/False
    TRIVIA_ENCODE="default"    # Basic encoding - UTF 8



    def __init__(self):  # Constructor to start the class
        self.payload()
        self.request()


    def payload(self): # Sets the payload for the game request
        trivia_amount = input("How manny questions do you want? ( 1 - 50 ):    ")
        trivia_choice = input("Choose a category: \n"
                                "1.General knowledge\n"
                                "2.Entertainment: Books\n"
                                "3.Entertainment: Film\n"
                                "4.Entertainment: Television\n"
                                "5.Entertainment: Video Games\n"
                                "6.Entertainment: Board Games\n"
                                "7.Entertainment: Comics\n"
                                "8.Mythologi\n"
                                "9.Geography\n"
                                "10.Animals\n"
                                "11.Vehicles\n"
                                "12.Science: Computers\n"
                                "13.any\n")

        if trivia_choice == "1":
            trivia_category = "9"

        elif trivia_choice == "2":
            trivia_category = "10"

        elif trivia_choice == "3":
            trivia_category = "11"

        elif trivia_choice == "4":
            trivia_category = "14"

        elif trivia_choice == "5":
            trivia_category = "15"

        elif trivia_choice == "6":
            trivia_category = "16"

        elif trivia_choice == "7":
            trivia_category = "29"

        elif trivia_choice == "8":
            trivia_category = "20" # Mythologi

        elif trivia_choice == "9":
            trivia_category = "22" # Geography

        elif trivia_choice == "10":
            trivia_category = "27" # Animals

        elif trivia_choice == "11":
            trivia_category = "28" # Vehicles

        elif trivia_choice == "12":
            trivia_category = "any"

        trivia_difficulty = input("Difficulty: easy/medium/hard/any:    ")

        # Set the class constant variables
        self.TRIVIA_AMOUNT = trivia_amount
        self.TRIVIA_CATEGORY = trivia_category
        self.TRIVIA_DIFFICULTY = trivia_difficulty
        self.TRIVIA_TYPE = "boolean"
        self.TRIVIA_ENCODE = "default"



    def request(self): # Send a POST request via trivia API to recieve the game questions
        print(f"{self.TRIVIA_AMOUNT}")
        print(f"{self.TRIVIA_CATEGORY}")
        print(f"{self.TRIVIA_DIFFICULTY}")
        print(f"{self.TRIVIA_TYPE}")
        print(f"{self.TRIVIA_ENCODE}")
        data_dict = ""

        url = "https://opentdb.com/api.php?amount="+self.TRIVIA_AMOUNT+"&category="+self.TRIVIA_CATEGORY+"&difficulty="+self.TRIVIA_DIFFICULTY+"&type="+self.TRIVIA_TYPE
        response = requests.get(url) # Class object of Response, raw HTTP response as bytes in .content and string in .text
        print(response.status_code)
        print(response.headers.get("content-type").lower())
        if response.status_code == 200:
            if "application/json" in response.headers.get("content-type","").lower():
                data_dict = response.json()

        question_list = []
        for data in data_dict["results"]:
            question = data["question"]
            answer = data["correct_answer"]

            question_dict = {} # Temporary dictionary

            # Replace &quot; and &#039; in the question
            question = question.replace('&quot;', '"').replace("&#039;", "`").replace("&Aring;", "Å").encode('utf-8')
            # Assign values to the dictionary
            question_dict["question"] = question
            question_dict["answer"] = answer

            print(question_dict)
            question_list.append(question_dict)
            print(question_list)




'''
        url ="https://opentdb.com/api_config.php"
        payload = {
            "trivia_amount": self.TRIVIA_AMOUNT,
            "trivia_category": self.TRIVIA_CATEGORY,
            "trivia_difficulty": self.TRIVIA_DIFFICULTY,
            "trivia_type": self.TRIVIA_TYPE,
            "trivia_encode": self.TRIVIA_ENCODE
        }
        headers = {
            "method"
        }
        response = requests.post(url, data=payload)
        print(response.text)
        
        # Parsing the data into a dictionary
        print(response.text)
        with open('questions.txt', 'w') as file:
            file.write(response.text)
        '''



