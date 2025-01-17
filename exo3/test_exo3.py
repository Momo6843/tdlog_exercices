import unittest

from exo3 import processLines


class TestExo3(unittest.TestCase):
    def test_input_1(self):
        with open("exo3/sample/input1.txt") as input1:
            lines = input1.readlines()

        with open("exo3/sample/output1.txt") as output1:
            expected = output1.read().strip()  # .strip() to handle any extra newlines or spaces

        self.assertEqual(expected, processLines(lines))

    def test_input_2(self):
        with open("exo3/sample/input2.txt") as input2:
            lines = input2.readlines()

        with open("exo3/sample/output2.txt") as output2:
            expected = output2.read().strip()  # .strip() to handle any extra newlines or spaces

        self.assertEqual(expected, processLines(lines))


if __name__ == '__main__':
    unittest.main()
