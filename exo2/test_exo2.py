import unittest
from exo2 import Solution
class TestSolution(unittest.TestCase):
    
    def test_terminaison_vraie(self):
        tests_vrais = (
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        )
        for chaine1, chaine2 in tests_vrais:
            with self.subTest(f"Test : {chaine1} se termine par {chaine2}"):
                solution = Solution(chaine1, chaine2)
                self.assertTrue(solution.se_termine_par())

    def test_terminaison_fausse(self):
        tests_faux = (
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        )
        for chaine1, chaine2 in tests_faux:
            with self.subTest(f"Test : {chaine1} ne se termine pas par {chaine2}"):
                solution = Solution(chaine1, chaine2)
                self.assertFalse(solution.se_termine_par())

if __name__ == '__main__':
    unittest.main()
