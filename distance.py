"""
File Name  : distance.py
Description: Find minimum distance robot needs to travel to get to starting position
"""

from sys import argv


def find_distance(optimised_str) :
    """
        function to return minimum distance
    """
    distance = 0
    print(optimised_str)
    # initialising position
    x,y = 0,0
    direction = 0 # Taking 0 to be north, 1 - south, 2 - east, 3 - west

    for i in range(len(optimised_str)) :

        print("value of index", i)
        print("first element", optimised_str[i])


        # change in direction would mean steps are added
        if (optimised_str[i][0 :1] != "L") and (optimised_str[i][0 :1] != "R") :
            print("if loop:got some movement command")
            # last element

            if (optimised_str[i][0 :1] == "B") :
                x,y = get_location( direction, x, y, -int(optimised_str[i][1 :2]) )

            if (optimised_str[i][0 :1] == "F") :
                x,y = get_location( direction, x, y, int(optimised_str[i][1 :2]) )


        elif (optimised_str[i][0 :1] == "L") or (optimised_str[i][0 :1] == "R") :
            print("else loop:got some direction command")

            if (optimised_str[i][0 :1] == "L") :
                direction -= 1 if direction > 0 else -3
            else :
                direction += 1 if direction < 3 else -3

            continue

    distance = abs(x) + abs(y)

    return distance

def get_location( direction, x, y, distance ):
    """
        function to calculate final position after movement
    """
    if ( direction == 0 ) :
        return x, y + distance
    if ( direction == 1 ) :
        return x + distance , y
    if ( direction == 2 ) :
        return x, y - distance
    if ( direction == 3 ) :
        return x - distance , y

def optimise_commands(reversed_str) :
    """
        function to optimise list to remove iterations
    """
    # optimised_list= []
    for i in range(len(reversed_str) - 1) :
        print("index", i)
        print("length of list", len(reversed_str))
        # out of bound exception
        if i >= (len(reversed_str) - 1) :
            break;
        print("first elemnt", reversed_str[i][0 :1])
        print("second  elemnt", reversed_str[i + 1][0 :1])
        # effectively at the same position or straight line
        if reversed_str[i][0 :1] == "L" :
            if reversed_str[i + 1][0 :1] == "R" :
                print("L/R pair-removing")
                # removing from the list
                reversed_str.remove(reversed_str[i])
                print("optimised list after removing 1 element", reversed_str)
                reversed_str.remove(reversed_str[i])
                print("optimised list after removing", reversed_str)
        elif reversed_str[i][0 :1] == "R" :
            if reversed_str[i + 1][0 :1] == "L" :
                print("R/L pair-removing")
                # removing from the list
                reversed_str.remove(reversed_str[i])
                reversed_str.remove(reversed_str[i])
                print("optimised list after removing", reversed_str)

    print("list after optimisation", reversed_str)

    # testing
    return reversed_str



def analyse_command(snippet) :
    """
        function to analyse answer
    """
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

     # testing
    return snippet


def validate_command(cmd) :
    """
    Function to validate command string
    :param cmd: Command string given by user
    :return:
    """

    # gives a list of commands; to separate commas
    # list values can be replaced, unlike strings
    cmd_list = cmd.split(',')
    print("command element", cmd_list)
    for i in range(0, len(cmd_list)) :
        if ((cmd_list[i][0 :1] == 'F' or cmd_list[i][0 :1] == 'R' or cmd_list[i][0 :1] == 'B' or cmd_list[i][
                                                                                                 0 :1] == 'L')) :
            if ((cmd_list[i][0 :1] == 'L') or (cmd_list[i][0 :1] == 'R')) :
                if (cmd_list[i][1 :2] != '1') :
                    print("Command Format invalid! L and R can only have 1 succeeding them!")
                    exit()
        else :
            print("Invalid command:can have L|R|F|B")
            exit()

    return cmd_list

    # testing
    # return 0


def main(var) :
    """
        main function
    """

    command_string = var

    # read from a file
    if command_string == "command.txt" :
        try :
            with open("command.txt") as fileobj :
                command_string = fileobj.read()
        except FileNotFoundError :
            print("Cannot find file command.txt")
            exit()


    print(command_string)
    # function to validate commandString
    cmd_list = validate_command(command_string)

    # function to get answer
    reversed_list = analyse_command(cmd_list)

    # optimising list;removing opposite actions from the list
    print("Calling optimise function with list as ", reversed_list)
    optimised_list = optimise_commands(reversed_list)

    # finding distance
    distance = find_distance(optimised_list)
    print("MINIMUM DISTANCE TO GET BACK TO STARTING POINT", distance)


if __name__ == "__main__" :
    print(len(argv))
    if len(argv) == 2 :
        main(argv[1])
    else :
        print("Command list missing!Try again")
        exit()