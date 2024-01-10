# Import textblob library.
from textblob import TextBlob

# Initialise a loop to allow the user input words until they choose to exit.
t = 1
while t:
    # accept user input and print word
    word_input = input("Enter the text to be checked: ")
    print("Your original text: "+str(word_input))
    
    # Create an object from the user's input.  
    blob = TextBlob(word_input)  

    if word_input.lower() == str(blob.correct()).lower():
        print("The text is already correct.")
    else:
        # Use correct() method to correct the spelling of the text; print the corrected spelling
        corrected_text = blob.correct()
        print("corrected text: "+str(corrected_text))
    
    t = int(input("Do you want to correct another text? 1 (yes) : 0 (no) "))
