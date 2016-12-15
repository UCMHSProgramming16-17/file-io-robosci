#open file called list.txt in write mode
file = open("list.txt", "w")

#repeat this ten times:

input = input("What?")
file.write(input)
    #Take user input
    #Write user input to a file
    
#Close File
file.close()