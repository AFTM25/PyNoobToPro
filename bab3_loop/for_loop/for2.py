# Prompt the user to enter a word
user_word = input('Input your of word: ')
# and assign it to the user_word variable.
user_word = user_word.upper()
for letter in user_word:
    # Complete the body of the for loop.
    if letter == 'A' or letter == 'I' or letter == 'O' or letter == 'U' or letter == 'E':
        continue
    else:
        print(letter)
