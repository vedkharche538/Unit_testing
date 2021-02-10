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
import re
name_re = '^[\w]+[ ][\w]+$'
phone_re = '^[+][9][1][-][\d]{10}$'
phoneBook = {}
def addContact(name,phone_number=" "):
    if re.search(name_re,name) and re.search(phone_re,phone_number):
        if phone_number not in phoneBook.values():
            phoneBook[name] = phone_number
            print(phoneBook)
            return 1
        else:
            print('%s Number exist already'%(phone_number))
            return 0

    else:
        print('Check name format [First Name][Last Name] or phone number format[+91-98754651358].........')
        return 0

class NoDataFoundException(Exception):
    pass


def searchContact(name):
    try:
        if name not in phoneBook.keys():
            raise NoDataFoundException
        print (name," : ",phoneBook[name])
        return(phoneBook[name])
    except NoDataFoundException as nd:
        print('No data found for this name')
        return -1

    
