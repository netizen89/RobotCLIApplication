from sys import argv


# function to return minimum distance
def find_distance(reversed_str) :
    distance = 0
    print(reversed_str)

    for i in range(len(reversed_str)-1) :
        print("value of index", i)
        print("first element", reversed_str[i])
        print("second element", reversed_str[i + 1])

        #analysing first command is movement
        if (reversed_str[i][0 :1] == "B" or reversed_str[i][0 :1]== "F") :
            print("movement first")
            print("second element after movement element", reversed_str[i + 1][0 :1])
            if(reversed_str[i + 1][0 :1] == "F" or reversed_str[i + 1][0 :1] == "B"):
                print("B,F together")
                print("distance", distance)
                #effective movemment:subtraction(direction-direction pair
                if reversed_str[i][1 :2] >= reversed_str[i + 1][1 :2] :
                    print("first element higher")
                    distance = distance + (int(reversed_str[i][1 :2]) - int(reversed_str[i + 1][1 :2]))
                    print("distance in first if", distance)


                else:
                    distance = distance + (int(reversed_str[i + 1][1 :2]) - int(reversed_str[i][1 :2]))
            #incrementing index(element already considered

                # effective movemment:addition(direction-movement pair
            elif(reversed_str[i + 1][0 :1] == "L" or reversed_str[i + 1][0 :1] == "R"):
                print("B/F and L/R together")
                distance = distance + int(reversed_str[i][1 :2])

            print("distance", distance)
            #already computed pairs
            i += 3
         #analysis of first direction command

        elif (reversed_str[i][0 :1] == "L" or reversed_str[i][0 :1]== "R") :
            print("direction first")
            print("inside elseif")
                #checking for next command to be movement command:add distances
            print("second element after direction element",reversed_str[i + 1][0:1])
            if(reversed_str[i + 1][0 :1] == "B" or reversed_str[i+1][0 :1]== "F"):
                print("loop check: after direction;movemnt command")
                distance = distance + int(reversed_str[i+1][1 :2])
             #no movement;just changing directions
            else:
                i = i+3
                continue
        print("distance", distance)

    print("Minimum distance", distance)


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
    print("reserved elements as per solution", snippet)
    # reversing list to get back to starting position
    snippet.reverse()

    # finding distance
    find_distance(snippet)



# main
commandString = argv[1]
print(commandString)
# gives a list of commands; to separate commas
# list values can be replaced, unlike strings
commandList = commandString.split(',')
print(commandList)
# function to get answer
analyse_command(commandList)
