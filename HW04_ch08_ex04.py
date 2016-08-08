#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    The function correctly returns True after it encounters the first character that is in smaller case and does not evaluate the remaining characters in the string.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    The function correctly returns 'True' (string) after it encounters the first character that is in smaller case and does not evaluate the remaining characters in the string
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
    The function returns True only if the last character in the string is in smaller case else if it is in upper case it returns False since 'flag' variable is overwritten each time in the for loop.
    The return statement, if written within the for loop after checking if flag value is True would return the expected result.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    The function correctly returns True if there are one or more lower case charaters in the string that is passed
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    The function checks if all the characters in a string are in smaller case and not just any one of the characters.
    It returns false as soon as it encounters a character in upper case.
    """
    for c in s:
        if not c.islower():
            return False
    return True

###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print(any_lowercase3('Pluto'))
    print(any_lowercase3('PlutO'))
    print(any_lowercase5('python'))
    print(any_lowercase5('pythoN'))
    print(any_lowercase5('Python'))

if __name__ == '__main__':
    main()
