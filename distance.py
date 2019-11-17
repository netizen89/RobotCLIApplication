from sys import argv


# function to analyse answer
def analyse_command(snippet) :
    # direction and step variables
    direction = []
    movement = []

    print("list of commands", snippet)
    print("length of list", len(snippet))

    # reversing directions to get to the solution
    for i in range(len(snippet)) :
        if snippet[i][0 :1] == "R" :
            snippet[i] = "L" + snippet[i][1 :2]
        elif snippet[i][0 :1] == "L" :
            snippet[i] = "R" + snippet[i][1 :2]
        elif snippet[i][0 :1] == "F" :
            snippet[i] = "B" + snippet[i][1 :2]
        else :
            snippet[i] = "F" + snippet[i][1 :2]
    print("modified as per solution", snippet)




# if __name__ == " __main__":
commandString = argv[1]
print(commandString)
# gives a list of commands; to separate commas
# list values can be replaced, unlike strings
commandList = commandString.split(',')
print(commandList)
# function to get answer
analyse_command(commandList)
