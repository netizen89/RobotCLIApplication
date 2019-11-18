import unittest

# importing class which needs to be tested
from distance import *


class Test(unittest.TestCase) :
    """
   The basic class that inherits unittest.TestCase
   """


class TestCliApp(unittest.TestCase) :

    #@unittest.skip("")
    def test_0_main(self) :
        main("command.txt")
        self.assertRaises(FileNotFoundError)

    #@unittest.skip("")
    def test_validate_command(self) :
        result = validate_command("F3,R1,L1,B2,F2,R1,L1,B6")
        #self.assertRaises(SystemExit)
        self.assertEqual(result, ['F3', 'R1', 'L1', 'B2', 'F2', 'R1', 'L1', 'B6'])

    def test_reverse_commands(self) :
        result = reverse_command(['F3', 'R1', 'L1', 'B2', 'F2', 'R1', 'L1', 'B6'])
        self.assertEqual(result, ['F6', 'R1', 'L1', 'B2', 'F2', 'R1', 'L1', 'B3'])

    def test_optimise_commands(self) :
        result = optimise_commands(['F6', 'R1', 'L1', 'B2', 'F2', 'R1', 'L1', 'B3'])
        self.assertEqual(result, ['F6', 'B2', 'F2', 'B3'])

    def test_find_distance(self) :
        result = find_distance(['F6', 'B2', 'F2', 'B3'])
        self.assertEqual(result, 3)


if __name__ == '__main__' :
    # begin the unittest.main()
    unittest.main()
