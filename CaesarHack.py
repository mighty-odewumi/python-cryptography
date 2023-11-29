msg = input('Enter an encrypted text: ')
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'  # This is a constant variable
# represented by capital letters

# Looping using the value of the length of the SYMBOLS variable.
for key in range(len(SYMBOLS)):
    translated = ''  # This line is placed here, in a for loop to make that the value of translated is an empty string
    # on each iteration.

    # Checking through the msg variable
    for symbol in msg:
        if symbol in SYMBOLS: # If the character in msg is contained in SYMBOLS, find the index
            # and also subtract the key from the character's index to decrypt the message
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            #If the value after decryption is less than zero, add the value of the  length of the SYMBOLS to it.
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]

        # If the character in the message is not in the SYMBOLS variable, print the symbol(character) that way
        else:
            translated = translated + symbol

    # Print final results using string formatting.
    print("[*] Key #%s: %s" %(key,translated))
