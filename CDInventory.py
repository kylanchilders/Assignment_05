#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script modified to use list of dicts instead of 2d table
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# KChilders, 2021-Feb-11, Filled out each function to work with existing 2d table structure
# KChilders, 2021-Feb-15, Rewrote all functions to use list of dicts instead of 2d table. Commented code
#------------------------------------------#

#import ast so I can convert strings in file back into dictionary
import ast

strChoice = ''
lstTbl = []
lstRow = []
strFileName = 'CDInventory.txt'
objFile = None

print('The Magic CD Inventory\n')
while True:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()
    print()
    # x closes the program
    if strChoice == 'x':
        break
    # l loads from the CDInventory.txt file.
    if strChoice == 'l':
        with open("CDInventory.txt", "r") as cdTextFile:
            # I use .read to get the content of the file, and then .splitlines to split it into rows.
            loadEntries = cdTextFile.read().splitlines()
            # For each row, I use ast.literal_eval to read the string and convert it into a dictionary
            for x in loadEntries:
                lstRow = ast.literal_eval(x)
                # Once converted to a dictionary, I append it to my lstTbl list variable
                lstTbl.append(lstRow)     
    # a adds a new entry into inventory by capturing user input          
    elif strChoice == 'a':
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        # The below line assigns a key to the inputted values to make it an dictionary
        lstRow = {'ID' : intID, 'Title' : strTitle, 'Artist' : strArtist}
        # Appends the dictionary into our listTbl list variable
        lstTbl.append(lstRow)
        # i just prints the lstTbl variable to screen
    elif strChoice == 'i':
        print(lstTbl)
        # d deletes the last dictionary in our listTbl variable
    elif strChoice == 'd':
        del lstTbl[-1]
        # s writes our lstTbl variable to text file
    elif strChoice == 's':
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            #Takes each row of our lstTbl variable, turns it into a string with a page break, and writes to file
            objFile.write(str(row) + '\n')
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

