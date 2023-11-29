import os
import TranspositionCipher
import sys
import transpositonDecrypt
import time


def main():
    inputFilename = input('\nEnter the input filename to be processed here: ')
    Key = int(input('Enter the value for the key: '))
    mode = input('Enter the mode of the process you want to run? \'encrypt\'/\'decrypt\': ')
    outputFilename = input('Enter the name of the ouput file here: ')

    # Check if the file we want to operate on exists, if not print an error and quit.
    if not os.path.exists(inputFilename):
        print('\n[-] No such file named %s. Quitting run...' % inputFilename)
        sys.exit()

    # Check if the file exists and asks if user wants to continue or quit because the initial files will be overwritten.
    # And check the response, if it is continue or quit
    if os.path.exists(outputFilename):
        print('Files in %s will be overwritten. Do you want to continue? Enter (C)ontinue or (Q)uit'
              % outputFilename)
        response = input('>')
        if not response.lower().startswith('c'):
            print('[-] Quitting')
            sys.exit()

    # Open the file we want to operate on
    InputFile = open(inputFilename)
    content_of_InputFile = InputFile.read()
    InputFile.close()

    print('[*] %sing...' % (mode.title()))

    # Check the time
    startTime = time.time()

    # Check the mode of the process and execute accordingly.
    if mode == 'decrypt':
        translated = transpositonDecrypt.decryptMessage(Key, content_of_InputFile)
    elif mode == 'encrypt':
        translated = TranspositionCipher.encryptMessage(Key, content_of_InputFile)

    # Get the total time taken and round off to two decimal places.
    totalTime = round(time.time() - startTime, 2)

    print('[*] Total %sion time is %s seconds' % (mode, totalTime))

    # Open the file we want to write our encrypted or decrypted text to depending on the mode input
    outputFile = open(outputFilename, 'w')
    # assert isinstance(translated, object)
    outputFile.write(translated)
    outputFile.close()

    print('[*] %sion process finished. File contains %s characters.' % (mode.title(), len(content_of_InputFile)))
    print('[*] %sed file is %s' % (mode.title(), outputFilename))


# Calls the main() function if we are not importing
if __name__ == '__main__':
    main()
