# RobotCLIApplication
CLI Application


## Introduction
A CLI application for robots which receives a string of commands and outputs the robot's distance from it's starting point.This distance will be the minimum amount of units the robot will need to traverse in order to get back to it's starting point.

## Commands
Robot receives commands in order to move.  These commands will tell the robot to go forwards or backwards, and turn left or right.

Format :  CommandNumber
 
* `F` - move forward 1 unit
* `B` - move backward 1 unit
* `R` - turn right 90 degrees
* `L` - turn left 90 degrees
  
 The robot can only turn 90 degrees at a time while forward/backward steps could be any. For example 'L1' means 'turn left by 90 degrees once'.  'B2' would mean go backwards 2 units.
 
 ## Input 
 A string of comma-separated commands eg `F1,R1,B2,L1,B3`.
 
 ## Output
 The minimum amount of distance to get back to the starting point (`4` in this case).
 
 ## Usage
 Input can be given as command line arguments or as a file.
 
 Format : PyFile InputString/File
 * File "command.txt" is provided to give command string
  
 ## Testing
 Unit test cases for the CLI application are available.
 
 
 
 
