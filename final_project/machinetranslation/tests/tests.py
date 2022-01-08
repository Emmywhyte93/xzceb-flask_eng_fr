import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french('HELLO'), 'BONJOUR')
        self.assertEqual(english_to_french(), '')

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('BONJOUR'), 'HELLO')
        self.assertEqual(french_to_english(), '')

if __name__=='__main__':
    unittest.main()
        