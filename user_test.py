import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user behaviours.

    Args:
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

    def test_save_user(self):
        '''
        test_save_user test case to test if the  user object is saved into the user list
        '''
        self.new_user.save_user() # save new user
        self.assertEqual(len(User.user_list),1)


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        User.user_list = []

            # other  test cases here

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("a","b","c","d") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)




if __name__ == '__main__':
    unittest.main()