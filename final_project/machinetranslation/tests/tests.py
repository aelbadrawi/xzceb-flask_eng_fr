import unittest
from translator import englishToFrench,frenchToEnglish


class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertNotEqual(englishToFrench("Hello"), "Bonjourrr")


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Bonjour"), "Hello")
        self.assertEqual(englishToFrench("Bonjour"), "Hello")
        self.assertNotEqual(englishToFrench("Bonjour"), "Helloooo")