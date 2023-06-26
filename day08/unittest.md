
# Unit test
This does not evaluate style, but results.

## use:
For this example:

```pylint code_testing.py -r y```

Module to be tested:

```py
def all_upper(text):
    return text.upper()
```

Test structure:
```py
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
        spec_result = "HELLO"
        self.assertEqual(result, spec_result)
    
# Requires the main function to be executed from the command line
if __name__ == '__main__':
    unittest.main()
```

# Report:

```sh
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Generating an error on purpose

```py
        ...
        spec_result = "HELLO !!!"
        self.assertEqual(result, spec_result)
        ...
```

# Report:

```sh
======================================================================
FAIL: test_upper (__main__.TestTextChange)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\aortiz\Documents\python\python_basics\day8\unittest_code_testing.py", line 18, in test_upper
    self.assertEqual(result, spec_result)
AssertionError: 'HELLO' != 'HELLO !!!'
- HELLO
+ HELLO !!!
?      ++++


----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```