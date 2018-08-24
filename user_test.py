import unittest # Importing unittest module
from user import User #IMporting the user class


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user behaviours.

    Argsaa:
          unitest.TestCase: TestCase that helps in creating test cases
    '''

def setUp(self):
    '''
    set up method to run before each test cases.
    '''
    self.new_user = User("koyoo","maxwel","0204405922","koyoomaxwel@gmail.com") #create user object

def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.first_name,"koyoo")
    self.assertEqual(self.new_user.last_name,"maxwel")
    self.assertEqual(self.new_user.phone_number,"0204405922")
    self.assertEqual(self.new_user.email,"koyoomaxwel@gmail.com")

    if __name__ == '__main__':
        unittest.main()