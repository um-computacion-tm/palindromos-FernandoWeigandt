import unittest
from palindrome import *



class TestIfPalindrome(unittest.TestCase):

    def test_isPalindrome(self):

        resultado=palindrome('ala')

        self.assertEqual(resultado, True)

    def test_notPalindrome(self):

        resultado=palindrome('hola')

        self.assertEqual(resultado, False)

    def test_isPalindrome2(self):

        resultado=palindrome('neuquen')

        self.assertEqual(resultado, True)

    def test_notPalindrome2(self):

        resultado=palindrome('aceituna')

        self.assertEqual(resultado, False)

if __name__=='__main__':
    unittest.main()