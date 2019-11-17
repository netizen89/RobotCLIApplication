from sys import argv


# function to return minimum distance
def find_distance(optimised_str) :
    distance = 0
    effective_distance = 0
    count_forwards = 0
    count_backwards = 0
    print(optimised_str)


    for i in range(len(optimised_str)) :
        print("value of index", i)
        print("first element", optimised_str[i])
        print("Effective distance", effective_distance)
        print("total distance",distance)
        #print("second element",optimised_str[i + 1])
        #get sum of b's and f's till a direction is found

        #change in direction would mean steps are added
        if(optimised_str[i][0 :1] != "L") and (optimised_str[i][0 :1] != "R") :
            print("if loop:got some movement command")
            # last element


            if(optimised_str[i][0 :1] == "B"):
                print("backward count loop")
                print("value of index", i)
                print(optimised_str[i])
                count_backwards=count_backwards + int(optimised_str[i][1:2])
                print("backward count", count_backwards)


            if(optimised_str[i][0 :1] == "F"):
                print("forward count loop")
                count_forwards = count_forwards + int(optimised_str[i][1 :2])

            #determine which movement was greater and find effective distance(subtraction)
            print("backward_Count, forward_count", count_backwards, count_forwards)
            if (count_forwards >= count_backwards):
                effective_distance = count_forwards - count_backwards
            else:
                effective_distance = count_backwards - count_forwards


        elif(optimised_str[i][0 :1] == "L") or (optimised_str[i][0 :1] == "R"):
            print("else loop:got some direction command")
            distance = distance + effective_distance
            print("Distance computed till first direction", distance)

            # computations done till a direction;resetting movement counters
            count_forwards = 0
            count_backwards = 0
            effective_distance = 0
            print("distance in else", distance)
            continue
    distance = distance + effective_distance

    print("Minimum distance", distance)

# function to optimise list to remove iterations
def optimise_commands(reversed_str) :
    #optimised_list= []
    for i in range(len(reversed_str) - 1) :
        print("index", i)
        print("length of list", len(reversed_str))
         # out of bound exception
        if i >= (len(reversed_str) - 1) :
            break;
        print("first elemnt", reversed_str[i][0 :1])
        print("second  elemnt", reversed_str[i+1][0 :1])
        #effectively at the same position or straight line
        if reversed_str[i][0 :1] == "L":
            if reversed_str[i+1][0 :1] == "R":
                # removing from the list
                reversed_str.remove(reversed_str[i])
                reversed_str.remove(reversed_str[i])
                print("optimised list after removing",reversed_str)
        elif reversed_str[i][0 :1] == "R":
            if reversed_str[i+1][0 :1] == "L":
                # removing from the list
                reversed_str.remove(reversed_str[i])
                reversed_str.remove(reversed_str[i])
                print("optimised list after removing", reversed_str)
        #4 l's and 4 r,s same position(TO DO)
        # using groupby() + list comprehension removing consecutive duplicates
        #res = [i[0] for i in groupby(test_list)]

        #3 l's,3 r's(TO DO)

    print("list after optimisation", reversed_str)

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
    # optimsing list;removing opposite actions from the list
    print("Calling optimise function with list as ",snippet)
    optimise_commands(snippet)
    # finding distance
    find_distance(snippet)


# if __name__ == " __main__":
commandString = argv[1]
print(commandString)
# gives a list of commands; to separate commas
# list values can be replaced, unlike strings
commandList = commandString.split(',')
print(commandList)
# function to get answer
analyse_command(commandList)
