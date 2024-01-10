import enchant

def spell_check(text):
    checker = enchant.Dict("en_US")
    words = text.split()
    corrected_words = [checker.suggest(word)[0] if not checker.check(word) else word for word in words]
    return ' '.join(corrected_words)

t = 1
while t:
    word_input = input("Enter the text to be checked: ")
    print("Your original text: " + str(word_input))

    corrected_text = spell_check(word_input)
    
    if word_input.lower() == corrected_text.lower():
        print("The text is already correct.")
    else:
        print("Corrected text: " + corrected_text)
    
    t = int(input("Do you want to correct another text? 1 (yes) : 0 (no) "))


# TO-DO: Figure out why the Dict attribute is not recognised here, when the docs beg to differ