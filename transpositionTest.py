import TranspositionCipher
import random
import sys
import transpositonDecrypt


def main():
    random.seed(42)   # Setting a static value for the random method. This makes sure that the same set of random values
    # are generated for every run.

    # Looping for a particular number of times(20)
    for i in range(20):
        # Generate random messages.

        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        # Make the message into a list.
        message = list(message)

        # We want a message with scrambled message.
        random.shuffle(message)
        message = ''.join(message)  # Make the message into a string.

        # Print out the index of the message and show only the first 50 characters in the string.
        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # Iterate through the code where the division of the length of the message is the ending value of the range
        # function.
        for key in range(1, int(len(message)/2)):
            # Call the functions from the respective modules for encryption and decryption and make sure they are of the
            # same key.
            encrypted = TranspositionCipher.encryptMessage(key, message)
            decrypted = transpositonDecrypt.decryptMessage(key, encrypted)

            if message != decrypted:
                print('[-] Mismatch with key %s and message %s.' % (key, message))
                print('[*] Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher test passed.')


# If not a module import, run the code.

if __name__ == '__main__':
    main()
