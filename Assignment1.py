'''
1] Create a calculator class having add, subtract, multiply and divide methods in it.
Write a Test Class to perform unit testing on every unit considering all the cases.
Create below testcase methods:-
test_Add(), test_Sub(), test_Mul() and test_Divide()
'''
import unittest


class Calculation(object):
    def addition(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a // b

class CalculationTestCase(unittest.TestCase):
    def test_add(self):
        calc = Calculation()
        result = calc.addition(3, 8)
        self.assertEqual(result, 11)

    def test_subtract(self):
        calc = Calculation()
        result = calc.subtract(7, 3)
        self.assertEqual(result, 4)

    def test_multiply(self):
        calc = Calculation()
        result = calc.multiply(12, 5)
        self.assertEqual(result, 60)

    def test_divide(self):
        calc = Calculation()
        result = calc.divide(12, 5)
        self.assertEqual(result, 2)


'''
# 2] Create a test cases to check string conditions for the given methods.
# test_upper(), test_isUpper(), test_split()
# '''


# class Test(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('foo'.islower())

#     def test_split(self):
#         s = "Hello World"
#         self.assertEqual(s.split(), ['hello', 'world'])

#         with self.assertRaises(TypeError):
#             s.split(2)

'''
3] Write test cases and Implementation for below methods.
•	Check for valid Email Address passed to method:
test_isValidEmail() 	
•	Check if given word is Palindrome:
test_isPalindrome()

'''
import re
class check:
    def __init__(self,str1):
        self.str1=str1

    def ispalindrome(self):

        str2 = self.str1[:: -1]

        if self.str1 == str2:
            return True
        else:
            return False

    def validateeamil(self):

        email_validate = '^[a-z0-9]*[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        searchobj = re.search(email_validate, self.str1)

        if searchobj != None:
            return True
        else:
            return  False
			
class test_check(unittest.TestCase):

    def test_ispalindrome(self):
        str1= check('madam')
        str2= check('Vedhas')

        self.assertEqual(check.ispalindrome(str1),True)
        self.assertEqual(check.ispalindrome(str2),False)

    def test_validateemail(self):
        str1= check('DhinchakPooja@gmail.com')
        str2= check('thinkever$gmail.com')

        self.assertEqual(check.ispalindrome(str1),True)
        self.assertEqual(check.ispalindrome(str2),False)


if __name__ == '__main__':
    unittest.main()
