import unittest # Importint the unittest module
from user import user #Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''


#class user:
    """
    Class that generates new instances of the user.
    """


def __init__(self, first_name, last_name, phone_number, email): # docstring removed for simplicity


 def setUp(self):
    '''
    set up method to run before each test Cases.
    '''
    self.new_user = user("koyoo","maxwell","0204405922","koyoomaxwel@gmail.com") #create user object

def test_init(self):
    '''
    test_init test case to test if the user object is initialized properly
    '''

    self.assertEqual(self.new_user.first_name,"koyoo")
    self.assertEqual(self.new_user.last_name,"maxwell")
    self.assertEqual(self.new_user.email,"koyoomaxwel@gmail.com")



    if __name__ == '__main__':
      unittest.main()
