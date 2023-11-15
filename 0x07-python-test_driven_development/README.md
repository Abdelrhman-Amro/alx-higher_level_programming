- **RESOURCES**
    
    [Untitled Database](https://www.notion.so/bca7009a4d3c4e6badce5734e9e827b4?pvs=21)
    
- **LEARNING OBJECTIVES**
    - [x]  ***Why Python programming is awesome***
    - [ ]  ***What’s an interactive test***
    - [ ]  ***Why tests are important***
    - [ ]  ***How to write Docstrings to create tests***
    - [ ]  ***How to write documentation for each module and function***
    - [ ]  ***What are the basic option flags to create tests***
    - [ ]  ***How to find edge cases***

---

# ****Never forget a test [***](https://intranet.alxswe.com/concepts/47)**

---

# Test-Driven-Development (TDD)

**Step 1: Write tests**

**Step 2: Run the tests**

**Step 3: Write the actual code**

**Step 4: Make all tests now pass**

**Step 5: Refactor and improve**

**RED → GREEN → REFACTOR**

# UNITTEST

**Unit Testing is the first level of software testing where the smallest testable parts of software are tested. This is used to validate that each unit of the software performs as designed.**

- ***Test files must begin with a `test` prefix followed by the name of the file we’re testing.***
    - `**test’_name’.py**`
- ***Import your class to be tested and import `unittest`.***
    - `**import unittest**`
- ***Create a class that inherits from `unittest.TestCase`. This class will contain your test methods.***
    - `**class ‘name’(unittest.TestCases):**`
- ***Test methods must start with the word "test”. These methods will contain the actual tests for your code.***
    - `**def test’_name’:**`
    - **TABLE OF METHODS**
        
        
        | Method | Checks That |
        | --- | --- |
        | https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual | a == b |
        | assertNotEqual(a, b) | a != b |
        | assertTrue(x) | bool(x) is True |
        | assertFalse(x) | bool(x) is False |
        | https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs | a is b |
        | https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot | a is not b |
        | https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone | x is None |
        | assertIsNotNone(x) | x is not None |
        | https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn | a in b |
        | assertNotIn(a, b) | a not in b |
        | https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance | isinstance(a, b) |
        | https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance | not isinstance(a, b) |
        
- ***Add the following code at the end of your script to run the tests.***
    
    ```python
    if __name__ == '__main__':
        unittest.main()
    ```
    
- **`*setUp` method is called before each test method.***
    - `***def setUp(self):***`
- **`*tearDown` method is called after each test method.***
    - `***def tearDown(self):***`
- ***Additional Tips From (GPT):***
    - ***1. Keep test methods small and focused on specific functionality***
        
        Each test method should focus on testing a specific piece of functionality or behavior in your code. By keeping them small and focused, it becomes easier to identify what part of your code is being tested and understand the purpose of each test. This also makes it simpler to pinpoint the cause of any failures.
        
        - **EXAMPLE**
            
            ```python
            def test_addition(self):
                result = add_numbers(2, 2)
                self.assertEqual(result, 4)
            
            def test_subtraction(self):
                result = subtract_numbers(5, 3)
                self.assertEqual(result, 2)
            
            ```
            
    - ***2. Organize your tests logically within your test class***
        
        Arrange your test methods in a way that makes logical sense. You might group tests based on similar functionality or the component being tested. This organization can make your test suite more readable and help you quickly locate specific tests.
        
        - **EXAMPLE**
            
            ```python
            class CalculatorTests(unittest.TestCase):
            
                def test_addition(self):
                    # ...
            
                def test_subtraction(self):
                    # ...
            
            class StringUtilsTests(unittest.TestCase):
            
                def test_concatenation(self):
                    # ...
            ```
            

---

# DOCTEST

`**doctest` tests source code by running examples embedded in the documentation and verifying that they produce the expected results. It works by parsing the help text to find examples, running them, then comparing the output text against the expected value. Many developers find `doctest` easier to use than `[unittest](https://pymotw.com/3/unittest/index.html#module-unittest)` because, in its simplest form, there is no API to learn before using it.**

- ***You can use the interactive interpreter to create examples and then copy and paste them into the docstrings***
    - ***Simple Example***
        
        ```python
        doctest_simple.py
        def my_function(a, b):
            """
            >>> my_function(2, 3)
            6
            >>> my_function('a', 3)
            'aaa'
            """
            return a * b
        ```
        
- `***$ python3 -m doctest -v doctest_simple.py***`
    - **`*-v` flag stands for "verbose." When you include the `-v` flag, Python will run the tests in verbose mode, providing more detailed output about which tests pass and which fail.***
    - **`*-m` flag stands for "module." When you use `-m` followed by a module name, it tells Python to run the specified module as the main program.***
- ***When the tests include values that are likely to change in unpredictable ways, and where the actual value is not important USE …***
    - ***EXMAPLE***
        
        ```python
        # doctest_ellipsis.py
        class MyClass:
            pass
        
        def unpredictable(obj):
            """Returns a new list containing obj.
        
            >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
            [<doctest_ellipsis.MyClass object at 0x...>]
            """
            return [obj]
        ```
        
- `***doctest` makes a special effort to recognize tracebacks, and ignore the parts that might change from system to system.***
    - ***In fact, the entire body of the traceback is ignored and can be omitted.***
    - ***EXAMPLE***
        
        ***When `doctest` sees a traceback header line (either “`Traceback (most recent call last):`” or “`Traceback (innermost last):`”, to support different versions of Python), it skips ahead to find the exception type and message, ignoring the intervening lines entirely.***
        
        ```python
        # doctest_tracebacks_no_body.py
        
        def this_raises():
            """This function always raises an exception.
        
            >>> this_raises()
            Traceback (most recent call last):
            RuntimeError: here is the error
        
            >>> this_raises()
            Traceback (innermost last):
            RuntimeError: here is the error
            """
            raise RuntimeError('here is the error')
        ```
        
- ***To match the blank lines, replace them in the sample input with the string `<BLANKLINE>`. [EX](https://www.notion.so/8fe5aabfa16d4732a9ad8c18c2fcf041?pvs=21)***
- `***REPORT_NDIFF`, shows the difference between the actual and expected values with more detail, and the extra space becomes visible. [EX](https://www.notion.so/8fe5aabfa16d4732a9ad8c18c2fcf041?pvs=21)***
- **`*+NORMALIZE_WHITESPACE` option allows for flexibility in the number of spaces or newlines, but it doesn't allow you to add new spaces where there are none in the original output.***
    - ***EXAMPLE***
        
        ```python
        def my_function(a, b):
            """Returns a * b.
        
            >>> my_function(['A', 'A'], 3)  #doctest: +NORMALIZE_WHITESPACE
            ['A', 'A',
             'A', 'A',
             'A', 'A']
            """
            return a * b
        ```
        
- ***Test Locations → [***](https://pymotw.com/3/doctest/#tracebacks:~:text=Failed***%202%20failures.-,Test%20Locations%C2%B6,-All%20of%20the)***
- ***Doctest with txt files → [***](https://pymotw.com/3/doctest/#tracebacks:~:text=failed.%0ATest%20passed.-,External%20Documentation,-%C2%B6)***
    - `***python3 -m doctest -v doctest_in_help.txt***`
- ***Running Tests → [***](https://pymotw.com/3/doctest/#tracebacks:~:text=file%20is%20enough.-,Running%20Tests,-%C2%B6)***
    - ***By module [***](https://pymotw.com/3/doctest/#tracebacks:~:text=By-,Module,-%C2%B6)***
        - `***python3 doctest_testmod.py -v***`
        - ***CODE***
            
            ```python
            # doctest_testmod.py
            def my_function(a, b):
                """
                >>> my_function(2, 3)
                6
                >>> my_function('a', 3)
                'aaa'
                """
                return a * b
            
            if __name__ == '__main__':
                import doctest
                doctest.testmod()
            ```
            
    - ***By file [***](https://pymotw.com/3/doctest/#tracebacks:~:text=failed.%0ATest%20passed.-,By%20File,-%C2%B6)***
        - `***python3 doctest_testfile.py -v***`
        - ***CODE***
            
            ```python
            # doctest_testfile.py
            import doctest
            
            if __name__ == '__main__':
                doctest.testfile('doctest_in_help.txt')
            ```
