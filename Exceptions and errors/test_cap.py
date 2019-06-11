import unittest
import cap

#Class for testing
class TestCap(unittest.TestCase):

    #Test if it works with one word
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')

    #Test if it works for multiple words
    def test_multiple_word(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Monty Python')

#Run the tests
if __name__ == '__main__':
    unittest.main()
