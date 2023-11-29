msg = input('Enter a message you want encrypted/decrypted: ')

key = int(input('Enter key for encrypting or decrypting: '))

mode = input('Enter mode(\'encrypt\' or \'decrypt\'): ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.' # This is a constant variable
# represented by capital letters by convention.
translated = ''

'''Iterating through the code block in a for loop, the code checks if the character
in the message is part of the SYMBOLS constant variable string. 
 If so, in the variable symbolIndex, it finds the index of the character in the SYMBOLS string
 and then saves it as a value under symbolIndex.
 The code also checks to see if the mode input is 'encrypt' or 'decrypt'. If 'encrypt', it stores the value of
  addition of the index of the character and the key in a variable called translatedIndex. If 'decrypt', it stores the 
  value of subtraction of the symbolIndex and key in the translatedIndex variable.
  
  Next, the code checks if the length of translatedIndex is either less than zero or greater than or equal to the length
  of the SYMBOLS variable and deducts the length of SYMBOLS from translatedIndex if higher or equal and
  subtracts if less than 0.
  The translated variable is then concatenated(joined) with the values of the whole operation and printed outside the
  loop.
  '''
for symbol in msg:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol

print(translated)
