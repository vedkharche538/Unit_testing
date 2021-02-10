import unittest
import ass1
class TestAddContact(unittest.TestCase):
    def test_addContact(self):
        self.assertEqual(ass1.addContact('Vedhas',"+91-98478953210"),1,"Contact should be added successfully")
        self.assertEqual(ass1.addContact('Vedhas',"98478953210"),0,"Invalid Format")
        self.assertEqual(ass1.addContact('Vedhas', "+91-98478953210"), 0, "Invalid Format")
        self.assertEqual(ass1.addContact('Vedhas',"+91-98478953210"),0,"Duplicate contact")


    def test_searchContact(self):
        self.assertEqual(ass1.searchContact('Vedhas'),'+91-98478953210',"Phone number should be returned")
        self.assertEqual(ass1.searchContact('Vedhas'),-1,"No data found exception should be raised")

if __name__=='__main__':
    unittest.main()