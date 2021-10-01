"""
Written by Preston Zen
https://prestonzen.com
https://github.com/prestonzen
"""

def main():
    #Message to decrypt

    unformatted = input('Type in BOAR Cipher message to decrypt: ')
    formatted = unformatted.lower()
    message = list(formatted)
        
    newMessage = []

    #conversion dictionary

    boarCipher = {
        '11': "a",
        '12': "b",
        '13': "c",
        '14': "d",
        '15': "e",
        '21': "f",
        '22': "g",
        '23': "h",
        '24': "i",
        '25': "k",
        '31': "l",
        '32': "m",
        '33': "n",
        '34': "o",
        '35': "p",
        '41': "q",
        '42': "r",
        '43': "s",
        '44': "t",
        '45': "u",
        '51': "v",
        '52': "w",
        '53': "x",
        '54': "y",
        '55': "z"
    }

    for character in message:
        if character == 'a':
            character = '11'
            newMessage.append(character)
        elif character == 'b':
            character = '12'
            newMessage.append(character)
        elif character == 'c':
            character = '13'
            newMessage.append(character)
        elif character == 'd':
            character = '14'
            newMessage.append(character)
        elif character == 'e':
            character = '15'
            newMessage.append(character)
        elif character == 'f':
            character = '21'
            newMessage.append(character)
        elif character == 'g':
            character = '22'
            newMessage.append(character)
        elif character == 'h':
            character = '23'
            newMessage.append(character)
        elif character == 'i':
            character = '24'
            newMessage.append(character)
        elif character == 'k':
            character = '25'
            newMessage.append(character)
        elif character == 'l':
            character = '31'
            newMessage.append(character)
        elif character == 'm':
            character = '32'
            newMessage.append(character)
        elif character == 'n':
            character = '33'
            newMessage.append(character)
        elif character == 'o':
            character = '34'
            newMessage.append(character)
        elif character == 'p':
            character = '35'
            newMessage.append(character)
        elif character == 'q':
            character = '41'
            newMessage.append(character)
        elif character == 'r':
            character = '42'
            newMessage.append(character)
        elif character == 's':
            character = '43'
            newMessage.append(character)
        elif character == 't':
            character = '44'
            newMessage.append(character)
        elif character == 'u':
            character = '45'
            newMessage.append(character)
        elif character == 'v':
            character = '51'
            newMessage.append(character)
        elif character == 'w':
            character = '52'
            newMessage.append(character)
        elif character == 'x':
            character = '53'
            newMessage.append(character)
        elif character == 'y':
            character = '54'
            newMessage.append(character)
        elif character == 'z':
            character = '55'
            newMessage.append(character)

    #print(''.join(newMessage))

    newMessage = ''.join(newMessage) #makes the entire list one line instead of broken apart

    def split_list(newMessage): #splits the joined list into 2 halves
        half = len(newMessage)//2
        return newMessage[:half], newMessage[half:]

    topHalf, bottomHalf = split_list(newMessage)

    newTopHalf = []
    newBottomHalf = []

    for character in topHalf: #looping through the top half to index each number in a list
        newTopHalf.append(character)

    for character in bottomHalf: #looping through the bottom half to index each number in a list
        newBottomHalf.append(character)  

    #decrypt by getting the sum of the top line index position and the bottom line index position

    sumList = []
    for i in range(0, len(newTopHalf)):
        sumList.append(newTopHalf[i] + newBottomHalf[i])

    #convert to ascii text by checking table and append to new decode List
    decodedText = []

    for n in sumList:
        decodedText.append(boarCipher[n])

    print(''.join(decodedText))

    restart = input('Type yes to exit or press enter to continue decrypting')
    if restart == "yes" or restart == "Yes" or restart == "y" or restart == "y":
        exit()
    else:
        main()
    
main()
