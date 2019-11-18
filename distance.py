"""
File Name  : distance.py
Description: Find minimum distance robot needs to travel to get to starting position
"""

from sys import argv
import logging

# logging.basicConfig(level=logging.disable())
logging.basicConfig(level=logging.INFO)


def get_location(direction, x, y, distance) :
    """
        Function to calculate final position after movement
        :param : Direction,position(x,y),distance
        :return: position calculated by movement
    """
    if (direction == 0) :
        return x, y + distance
    if (direction == 1) :
        return x + distance, y
    if (direction == 2) :
        return x, y - distance
    if (direction == 3) :
        return x - distance, y


def find_distance(optimised_str) :
    """
        Function to return minimum distance to starting position
        :param : optimised string
        :return: minimum distance
    """

    logging.debug('optimised string is %s', optimised_str)
    # initialising position
    x, y = 0, 0
    direction = 0  # Taking 0 to be north, 1 - south, 2 - east, 3 - west
    for i in range(len(optimised_str)) :
        logging.debug('index is %s', i)
        logging.debug('element is %s', optimised_str[i])
        # change in direction would mean steps are added
        if (optimised_str[i][0 :1] != "L") and (optimised_str[i][0 :1] != "R") :
            logging.debug('if loop:got some movement command')
            if (optimised_str[i][0 :1] == "B") :
                x, y = get_location(direction, x, y, -int(optimised_str[i][1 :2]))
            if (optimised_str[i][0 :1] == "F") :
                x, y = get_location(direction, x, y, int(optimised_str[i][1 :2]))
        elif (optimised_str[i][0 :1] == "L") or (optimised_str[i][0 :1] == "R") :
            logging.debug('else loop:got some direction command')
            if optimised_str[i][0 :1] == "L" :
                direction -= 1 if direction > 0 else -3
            else :
                direction += 1 if direction < 3 else -3
            continue
    distance = abs(x) + abs(y)
    return distance



def optimise_commands(reversed_str) :
    """
        Function to optimise command string to get less iterations
        :param : Reversed Command string
        :return: optimised reversed string
    """

    for i in range(len(reversed_str) - 1) :
        logging.debug('length of list %s', len(reversed_str))
        # out of bound exception
        if i >= (len(reversed_str) - 1) :
            break;
        logging.debug('first element %s', reversed_str[i][0 :1])
        logging.debug('second element %s', reversed_str[i + 1][0 :1])
        # effectively at the same position or straight line
        if reversed_str[i][0 :1] == "L" :
            if reversed_str[i + 1][0 :1] == "R" :
                logging.debug('L/R pair-removing')
                # removing from the list
                reversed_str.remove(reversed_str[i])
                reversed_str.remove(reversed_str[i])
        elif reversed_str[i][0 :1] == "R" :
            if reversed_str[i + 1][0 :1] == "L" :
                logging.debug('R/L pair-removing')
                # removing from the list
                reversed_str.remove(reversed_str[i])
                reversed_str.remove(reversed_str[i])
    logging.debug('list after optimisation %s', reversed_str)
    return reversed_str


def reverse_command(snippet) :
    """
        Function to reverse command string
        :param : Validated command string given by user
        :return: reversed Command list
    """
    logging.debug('list of commands %s', snippet)
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
    # reversing list to get back to starting position
    snippet.reverse()
    logging.debug('list after reversal %s', snippet)
    return snippet


def validate_command(cmd) :
    """
        Function to validate command string
        :param : Command string given by user
        :return:Command list
    """
    # gives a list of commands; to separate commas
    # list values can be replaced, unlike strings
    cmd_list = cmd.split(',')
    logging.debug('command element %s', cmd_list)
    for i in range(0, len(cmd_list)) :
        if ((cmd_list[i][0 :1] == 'F' or cmd_list[i][0 :1] == 'R' or cmd_list[i][0 :1] == 'B' or cmd_list[i][
                                                                                                 0 :1] == 'L')) :
            if ((cmd_list[i][0 :1] == 'L') or (cmd_list[i][0 :1] == 'R')) :
                if (cmd_list[i][1 :2] != '1') :
                    logging.error('Command Format invalid! L and R can only have 1 succeeding them!')
                    # print("Command Format invalid! L and R can only have 1 succeeding them!")
                    exit()
        else :
            logging.error('Invalid command:can have L|R|F|B')
            # print("Invalid command:can have L|R|F|B")
            exit()
    return cmd_list


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
            logging.error('Cannot find file command.txt')
            exit()
    logging.debug('Commmand String %s', command_string)
    # function to validate commandString
    cmd_list = validate_command(command_string)
    # function to get reverse commands
    reversed_list = reverse_command(cmd_list)
    # optimising list;removing opposite actions from the list
    optimised_list = optimise_commands(reversed_list)
    # finding distance
    distance = find_distance(optimised_list)
    print('MINIMUM DISTANCE TO GET BACK TO STARTING POINT :', distance)


if __name__ == "__main__" :
    logging.debug('argument length %s', len(argv))
    if len(argv) == 2 :
        main(argv[1])
    else :
        logging.error('Command list missing!Try again')
        exit()
