import string
import pyperclip
from random import choice

class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] #Empty user list

    def __init__(self,username,password):
        """
        __init__ method that defines properties for our objects

        Args:
            username: New user username.
            password: New user password.
        """

        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method saves objects into list
        """
        User.user_list.append(self)


    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matched that username.
        Args:
        username: username to search for
        Returns:
         user  that matched the username.
        '''

        for user in cls.user_list:
            if user.username == username:
                return user
 

    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the user list.
        Args:
        username: Username to search if it exists
        Returns :
        Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.username == username:
                    return True

        return False    

class Credential:
    """
    Class that generates new instances of credential
    """

    credential_list = [] #Empty credential 

    def __init__(self,acc_name,login_name,password):
        """
        __init__ method that defines properties for our objects

        Args:
            acc_name: New credential acc_name.
            login_name: New credential login_name.
            password: New credential password.
        """

        self.acc_name = acc_name
        self.login_name = login_name
        self.password = password

    def save_credential(self):
        """
        save_credential method saves objects into list
        """
        Credential.credential_list.append(self)

    def del_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_acc_name(cls,acc_name):
        '''
        Method that takes in a number and returns a credential that matches that account name.

        Args:
        acc_name: Account name to search for
        Returns :
        Credential of account that matches the account name and details.
        '''

        for credential in cls.credential_list:
            if credential.acc_name == acc_name:
                return credential
    @classmethod
    def credential_exist(cls,acc_name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
        acc_name: Account name to search if it exists
        Returns :
        Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.acc_name == acc_name:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
