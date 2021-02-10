import unittest
from Assignment2 import AgeCalculator

class test_AgeCalculator(unittest.TestCase):

    def test_findAge(self):
        str1= AgeCalculator('20/01/1998')
        str2 = AgeCalculator('10/11/2010')
        str3 = AgeCalculator('11/12/1918')
        str4 = AgeCalculator('15/11/2032')
        self.assertEqual(AgeCalculator.findAge(str1),22)
        self.assertEqual(AgeCalculator.findAge(str2),0)
        self.assertEqual(AgeCalculator.findAge(str3),"InvalidDateException")
        self.assertEqual(AgeCalculator.findAge(str4),False)


if __name__== '__main__':
    unittest.main()
