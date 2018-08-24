import unittest # Importing the unittest module
from user import user # Importing the user class

class TestUsert(unittest.TestCase):
    
    '''
    Test class that defines test cases for the use class behaviour.

    Args:
        unitest.TestCase: TestCase class that helps in creating test cases
    '''


def setup(self):
    '''
     set up method to run before each cases.
    '''
    self.new_user = user("koyoo","maxwell","0204405922","koyoomaxwel@gmail.com") # create user object

    def rest_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"koyoo")
        self.assertEqual(self.new_user.last_name,"maxwell")
        self.assertEqual(self.new_user.phone_number,"0204405922")
        self.assertEqual(self.new_user.email,"koyoomaxwel@gmail.com")

        if __name__ == '__main__':
            unittest.main()
