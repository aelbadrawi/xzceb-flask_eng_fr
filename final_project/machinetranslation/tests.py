import unittest
from translator import englishToFrench,frenchToEnglish


class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        print("Hello")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertNotEqual(englishToFrench("Hello"), "Bonjourrr")