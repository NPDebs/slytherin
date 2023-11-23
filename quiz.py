# pop quiz 
# create a dictionary of questions and answers
test_bank = {
    "1": {
        "question": "The Eiffel Tower can be found in which European capital city?",
        "answer": "Paris"
    },

    "2": {
        "question": "Acrophobia is a fear of?",
        "answer": "heights"
    },

    "3": {
        "question": "What city is the capital of Turkey?",
        "answer": "Ankara"
    },

    "4": {
        "question": "A nonagon is a shape that has how many sides? (A digit)",
        "answer": "9",
    },

    "5": {
        "question": "The world’s tallest structure is the?",
        "answer": "Burj Khalifa"
    },

    "6": {
        "question": "What is the tallest mountain on earth?",
        "answer": "Everest"
    },

    "7": {
        "question": "In which country would you find the last standing original 7 Wonders of the World, the Great Pyramid of Giza?",
        "answer": "Egypt"
    },

    "8": {
        "question": "The Statue of Liberty was a gift to America from which country?",
        "answer": "France"
    },

    "9": {
        "question": "In what country do we find the Taj Mahal?",
        "answer": "India"
    },

    "10": {
        "question": "What day of the week comes after Tuesday",
        "answer": "Wednesday"
    },

    "11": {
        "question": "Christ the Redeemer is a statue which looks over which city? (3 letters)",
        "answer": "Rio"
    },
}

# create function to display questions and keep score
def take_quiz():
    print("Welcome to the ultimate quiz bank!")
    question_number = int(input("How many questions would you like to attempt?"))

    score = 0
   
   # only display the number of questions the user requests
    for key in map(str, range(1, question_number + 1)):
        question = test_bank[key]
        print(question["question"])        
        answer = input("Enter answer: ")

        if answer.lower() == question["answer"].lower():
            print("\nThat's correct!")
            score +=1
        else:
            print("\nWrong! \nThe answer is: ", question["answer"])

    # display final score
    print("\nYour score is: ", score)
    print("Percentage score: ", str(int(score / question_number * 100)) + "%")

take_quiz()

#To-do: Randomise questions