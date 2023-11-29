# import time


# Defining the main() function
def main():
    myMessage = input('Enter a plaintext to be encrypted: ')
    # time.sleep(5)
    myKey = int(input('Enter the key for the encryption: '))
    cipherText = encryptMessage(myKey, myMessage)
    print(cipherText + '|')
    # print(len(myMessage))


# This function is responsible for the encryption process
def encryptMessage(key, message):
    # Sets the cipherText to be a list of empty string multiplied by the value of the key.
    cipherText = [''] * key
    # A loop through the key which means that on each iteration, the value of column is 0, 1, 2, 3,... depending on the
    # value of the key input
    # And this is held by the variable CurrentIndex
    for column in range(key):
        CurrentIndex = column
        # print(CurrentIndex)

        # The while loop checks if the value of the CurrentIndex is not up to the length of the message,
        # adds the value of the key to the index on each iteration of the code
        while CurrentIndex < len(message):
            cipherText[column] += message[CurrentIndex]
            # print(cipherText[column])
            # print(message[CurrentIndex])
            CurrentIndex += key

    # The return function joins the empty string to the values in the cipherText.
    return ''.join(cipherText)


# This block of code calls the main() function if the code is not imported as a module
if __name__ == '__main__':
    main()
