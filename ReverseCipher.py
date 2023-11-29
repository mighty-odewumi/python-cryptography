# msg = 'Three can keep a secret, if two of them are dead.'
msg = input('Enter a secret word to be encrypted (hehe)\'reversed\': ')
translated = ''

'''
To understand this code, you can add another line in the while block to display how the values grew and the code
worked. Adding print('i is ', i, ', message is ', ,msg, ',translated is ', translated) shows that the code starts
from counts the number of characters in the string and minuses it by 1 recursively. It then prints the character
at each position, joining it to the translated variable on every pass starting from the last character'''

i = len(msg) - 1
while i >= 0:
    # print('i is ', i, ', message is ', msg[i], ', translated is ', translated)
    translated = translated + msg[i]
    i = i - 1

print(translated)
