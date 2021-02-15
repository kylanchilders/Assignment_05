# Assignment_05
Kylan Childers
2/15/2021
Foundations of Programming: Python
Assignment 05

Converting CD Inventory Program to work with list of dictionaries

Introduction
This exercise demonstrates working with someone else’s code to understand and modify it. The task here was to:
A)	Understand and modify their code in order to fill in the remaining required lines
B)	Re-write the code to use a list of dictionaries rather than a 2D list
What I did
Most of the code was already present. My strategy here was to first accomplish all the TODOs using the existing data types prior to rewriting them to accommodate the new data types, just to get the logic down first.
I started with the easiest, which was the ‘d’ choice to delete an entry from inventory. I simply used the del feature on the lstTbl variable, passing it in a -1 index to target the last entry in the list. This actually did not change when refactoring everything for a list of dictionaries. Syntax remained the exact same.
Next added the functionality of loading existing data. I had actually already done something like this in the previous assignment in order to load the IDs to automate that process. However, refactoring it to work with dictionaries, I had to do the following:
With the CDInventory.txt file open and set to read mode, I created a variable called loadEntries using the .read() function and the .splitlines() functions. This allowed me to loop through each row of my text file. For each row in there, I used the ast.literal_eval function (I found this on google) and it’s a fast way to convert the string from the text file back into a dictionary for use within the program. I then append that dictionary back into my lstRow variable.
Refactoring the a option to add a new CD to inventory was achieved simply by changing the variable type that the user input was being entered into into a dictionary. I did this by assigning those values directly into the hard coded keys of that variable.
The last part, saving to the txt file, I open the text file with open(), and then for every row in my lstTbl variable, I simply used the write function to turn each row of my list into a string, add a page break at the end, and then write it to file.
