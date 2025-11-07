# A function allows us to bundle  code into 
# a reusable block, making it easier to manage 
#and uderstand, By defining functions, we can
# avoid code repetition and enhance readability.\

#defining a function
def problem1():
    # pass 1 put pass here to avoid indentation error
    # Problem Set 1: Indexing and Slicing Strings
    # Basic Indexing:
    # Given the string magic = 'abracadabra',
    # a. Retrieve the 5th character.
    # b. Retrieve the second to last character.
    # c. Find the first occurrence of the letter 'c'.
    magic = 'abracadabra'
    fifth_character = magic[4]
    print(fifth_character)
    # Advanced Slicing:
    # Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
    # a. Extract the letters 'hij'.
    # b. Extract every second letter starting from 'a' to 'm'.
    # c. Reverse the entire string using slicing.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ye = alphabet[7:10]
    print(ye)
    second =alphabet[0:12:2]
    reversd = alphabet[::-1]
    print(second)
    print(reversd)
#calling a function