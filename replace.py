# word_replacement
# From a sentence, the user picks a word and replaces with another

while True:
    def word_replacement():
        sentence = "Snape is everyone's favourite teacher at Hogwarts."
        print(sentence)
        wrong_word = input("Which word do you want to replace? ")
        right_word = input("Enter word to replace it with: ")

        print(sentence.replace(wrong_word, right_word))

    word_replacement()
