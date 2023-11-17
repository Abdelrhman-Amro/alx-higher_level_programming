#!/usr/bin/python3
"""print text in specific format"""


def text_indentation(text):
    """
        prints a text with 2 new lines after
        each of these characters: . ? and :

        Args:
            text (str): text to print

        Rasies:
            TypeError: text must be a string

        Notes:
            There should be no space at the beginning
            or at the end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    skip = 1
    for c in text:
        if skip == 1 and c == ' ':
            continue
        skip = 0
        print(c, end='')
        if c in '.?:':
            print(end='\n\n')
            skip = 1
