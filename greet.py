print("Hello world!") 

user = input("What is your name? ")
greeting = "Hello " + user

def greet():
    print(greeting)

greet()

age = input("How old are you? ")
fav_colour = input("What is your favourite colour? ")

def converse():
    print(f'Your name is {user}, you are {age} years old and your favourite colour is {fav_colour}')

converse()
