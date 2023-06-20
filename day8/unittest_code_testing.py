"""
This is a code checked with unit test, 
which is integrated in python
"""
import unittest
import text_change

class TestTextChange(unittest.TestCase):
    """
    Asserts that the `all_upper` function from the `text_change` module returns the expected output 'HELLO' 
    when given the input 'hello'. Takes in one parameter, `self`, an instance of the test case class.
    Requires that the test function start with 'test_'
    """
    def test_upper(self):
        word = "hello"
        result = text_change.all_upper(word)
        spec_result = "HELLO !!!"
        self.assertEqual(result, spec_result)
    
# Requires the main function to be executed from the command line
if __name__ == '__main__':
    unittest.main()


