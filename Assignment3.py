'''
1.	Write a code to add the contacts in the phone book which is a dictionary. 
addContact(name, phone_number)
Test Cases to implement: -
•	Check if name contains firstname and last name
		e.g.: - asif immanad
•	Check if phone number is valid
Valid phone number format: - +91-98XXXXXX00
•	Check if no duplicate phone numbers in dictionary
'''
import unittest
class info(unittest.TestCase):
    dic = dict()
    def addContact(self,name,phone_number):
        self.assertIs(name,'asif immanad',"Not matched!!")
        #--------------------or--------------------
        self.assertSequenceEqual(name,'asif immanad','Not matched.....')
        dic['Name']=name
        dic['Phone_number']= phone_number

        for i in dic['Phone_number']:
            self.assertNotEquals(i,phone_number,'Duplicate Number found')


i = info()
i.addContact('asif immanad',+919975314545)