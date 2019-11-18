import unittest

# importing class which needs to be tested
from distance import *


class Test(unittest.TestCase) :
    """
   The basic class that inherits unittest.TestCase
   """


class TestCliApp(unittest.TestCase) :

    @unittest.skip("")
    def test_0_main(self) :
        main("command.txt")
        self.assertRaises(FileNotFoundError)

    @unittest.skip("")
    def test_validate_command(self) :
        result = validate_command("L2,F3")
        self.assertEqual(result, 0)

    @unittest.skip("")
    def test_reverse_commands(self) :
        result = analyse_command(['R1', 'F2', 'F3'])
        self.assertEqual(result, ['B3', 'B2', 'L1'])

    @unittest.skip("")
    def test_optimise_commands(self) :
        result = optimise_commands(['F2'])
        self.assertEqual(result, ['F2'])

    @unittest.skip("")
    def test_find_distance(self) :
        result = find_distance(['B2', 'B3', 'F6', 'B2'])
        self.assertEqual(result, 2)


if __name__ == '__main__' :
    # begin the unittest.main()
    unittest.main()
