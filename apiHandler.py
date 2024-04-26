import requests # # Run pip install requests to get the library, then import to make POST requests
import questions

class API:
    TRIVIA_AMOUNT = ""
    TRIVIA_DIFFICULTY = ""
    TRIVIA_TYPE = ""

    def __init__(self):  # Constructor to start the class
        self.payload()
        self.request()

    def payload(self): # Sets the payload for the game request
        self.TRIVIA_AMOUNT = "10"  #input("How manny questions do you want? ( 1 - 50 ):    ")
        self.TRIVIA_DIFFICULTY = "medium"
        self.TRIVIA_TYPE="boolean"

    def request(self): # Send a GET request via trivia API to recieve the game questions
        data_dict = ""

        url = "https://opentdb.com/api.php?amount="+self.TRIVIA_AMOUNT+"&difficulty="+self.TRIVIA_DIFFICULTY+"&type="+self.TRIVIA_TYPE
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
            question = question.replace('&quot;', '"').replace("&#039;", "`").replace("&Aring;", "Å")
            # Assign values to the dictionary
            question_dict["question"] = question
            question_dict["answer"] = answer

            #print(question_dict)
            question_list.append(question_dict)
            #print(question_list)

            # Write to questions.py
            with open('questions.py', 'w',encoding='utf-8') as file:
                file.write(f"questions_data = {question_list}\n")






