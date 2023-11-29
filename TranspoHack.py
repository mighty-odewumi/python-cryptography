import EnglishDetective
import transpositonDecrypt


def main():
    myMessage = input('Enter the encrypted text to be decrypted: ')  # '''weh oy oaur'''  # Encrypted message

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage is None:
        print('\n[-] Failed to hack encryption')

    else:
        print('Hacked message is: %s' % hackedMessage)


def hackTransposition(message):
    print('\n[*] Hacking encryption...')

    print('Enter Ctrl C (Windows) or Ctrl D (Linux) to quit\n')

    for key in range(1, len(message)):
        print('[*] Trying key #%s...' % key)
        decryptedText = transpositonDecrypt.decryptMessage(key, message)  # Calls the decryption function from
        # transpositionDecrypt

        # print(transpositonDecrypt.decryptMessage(key, message))

        if EnglishDetective.isEnglish(decryptedText):  # Checks if the decrypted text is English and asks the user to
            # input a response to continue or stop which prints the hacked message.
            print()
            print('Possible encryption hack: ')
            print('[*] Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D if done, and anything else to continue hacking: ')
            response = input('>')

            if response.strip().upper().startswith('D'):  # Removes whitespace from the user's input and converts to
                # uppercase, then check if the response input starts with a 'd'
                return decryptedText  # Return the decrypted text if found

    return None  # This is returned as the return value of the hackTransposition function which is then checked
    # in main() for None keyword, which prints the failed to hack message.


# If not a module import, run code
if __name__ == '__main__':
    main()
