import math


# The main() function calls the other functions if the code is run(in my opinion)
def main():
    myMessage = 'weh oy oaur'  # input('Enter an encrypted text: ')
    myKey = 9  # int(input('Enter a key for decryption: '))

    plaintext = decryptMessage(myKey, myMessage)
    print('[*] Decrypted text is \'' + plaintext + '|\'')


def decryptMessage(key, message):
    # The num_of_columns finds the number of columns of the text by dividing by rounding up
    # the value of the length of the message and dividing by the value of key as a float,
    # later converting to an integer.

    num_of_columns = int(math.ceil(len(message) / float(key)))
    num_of_rows = key  # Eqauls the value of the key input
    num_of_shadedBoxes = (num_of_columns * num_of_rows) - len(message)  # This finds the num_of_boxes that are not used
    # by the text by subtracting the length of the message from the product of num_of_columns and num_of_rows.

    plaintext = [''] * num_of_columns  # A list of empty string multiplied by the value of the num_of_columns
    # the variable contains value of the strings in each iteration of the next code block

    column = 0  # Initial values are zero to enable the code to track the column and row where the character in the code
    # will go
    row = 0

    # An iteration to get each character in the message
    for symbol in message:
        plaintext[column] += symbol  # Add the value of symbol to the position of plaintext represented by
        # plaintext[column] which is the index of the plaintext.

        column += 1  # Increment the value of column

        # Nested if conditions shortened by the use of boolean operators
        # Checks to see if the value for column is equal to the num_of_columns variable or
        # if the column is equal to num_of_column - 1 which tells that the code has reached the last column
        # and row >= num_of_rows - num_of_shadedBoxes tests to see if the value of row is greater than or equal to the
        # num_of_rows - num_of_shadedBoxes
        # It resets the value of column back to 0 to make it start from the beginning of the column and
        # increment the value of row by 1

        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_shadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)  # Joins the broken strings into a single string.


# Called if the code is not being imported and is executed normally.
if __name__ == '__main__':
    main()
