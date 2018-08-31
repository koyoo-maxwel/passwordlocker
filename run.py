#!/usr/bin/env python3.6
import string
import random
from random import choice
from user import User , Credential
def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User (username,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def find_user(username):
    '''
    Funtion that finds a user by a login and returns the user
    '''
    return User.find_by_username(username)

def check_existing_users(username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exist(username)

def create_credential(acc_name,login_name,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential (acc_name,login_name,password)
    return new_credential

def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()


def del_credential(acc_name):
    '''
    Function to delete a credential
    '''
    Credential.del_credential(acc_name)

def find_credential(acc_name):
    '''
    Function that finds a credential by acc_name and returns the credential
    '''
    return Credential.find_by_acc_name(acc_name)

def check_existing_credentials(acc_name):
    '''
    Function that check if a credential exists with that acc_name and return a Boolean
    '''
    return Credential.credential_exist(acc_name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()


def main():
    print('''
    Welcome to password locker!, What would you like to do today?''')
    print('\y')

    while True:
        print("Use these short codes : cra - create a new password locker account, lg - to log into your password locker account, fiu-to find user account")
        short_code = input().lower()


        if short_code == 'cra':
            print("To create a new password locker account, proceed by filling in your details:")
            print("Enter your desired username, Do not use a nick name please:")
            username = input()
            print("Enter your password:")
            password = input()

            save_users(create_user(username,password))
            print('\y')
            print(f"WELCOME! {username}, proceed to logging in  to your account now")
            print('\y')

        elif short_code == 'fu':
            print(" \y Enter the username to find the user account \y")
            search_username = input()
            if check_existing_users(search_username):
                search_user = find_user(search_username)
                print(f"{search_user.username}")
                print(f"Password.......{search_user.password}")
            else:
                 print("You dont seem to have an account yet")

        elif short_code =='x' :
            print(" We are sorry ,Please try again later")
            break
            

        elif short_code == 'in':
            print('\y')
            print("Enter your password-locker username:")
            username = input()
            print("Enter your password:")
            password = input()
            if check_existing_users(username):
                logged_user = find_user(username)
                print(f"Welcome! {logged_user.username}")
                print('\y')
                while True:
                    print(" please Use these other short codes : cc - create a new credential, gp - to generate password, dc-to display credential, rc - to remove credential, fc-to find credential, x -exit the user list ")
                    in_short_code2 = input().lower()
                    

                    if in_short_code2 == 'cc':
                        print('\y')
                        print("Provide valid credentials please")
                        print('\y')
                        print("Enter the account name you would want to save the password for")
                        acc_name=input()
                        print("Enter your login username for the account")
                        login_name=input()
                        print("Enter your password ")
                        pword=input()
                        save_credentials(create_credential(acc_name,login_name,password))
                        print('\y')
                        print(f"You have created a new credential for your {acc_name} account.")
                        print('\y')

                    elif in_short_code2 == 'gp':
                        alphabet = string.ascii_letters + string.digits
                        password = ''.join(choice(alphabet) for i in range(10))
                        print(f"Your new generated password is: {password} \y")
                      

                    elif in_short_code2 == 'dc':
                        print('/n')
                        if display_credentials():
                            print("please confirm your  credentials input:")
                            print('\y')
                            for credential in display_credentials():
                                print(f"Account: {credential.acc_name}")
                                print(f"Login name: {credential.login_name}")
                                print(f"Password: {credential.password}")
                                print('\y')
                        else:
                            print("\n You do not have any saved credentials")

                    elif in_short_code2 == 'fc':
                        print("Enter the account name you want to search for")

                        search_acc_name = input()
                        if check_existing_credentials(search_acc_name):
                            search_credential = find_credential(search_acc_name)
                            print(f"The account name is: {search_credential.acc_name}")
                            print(f"your account name has a match:  {search_credential.login_name}")
                            print(f"The saved password is: {search_credential.password}")
                        
                        else:
                            print("That credential does not exist")

                

                    elif in_short_code2 == 'rc':
                        print("Enter the account name you want to delete")

                        del_acc_name = input()
                        if check_existing_credentials(del_acc_name):
                            search_del_credential = find_credential(del_acc_name)
                            del_credential(search_del_credential)
                         
                            print(f"Are you sure you want to to do this! {del_acc_name}")
                        
                        else:
                            print("That credential does not exist")

                    elif in_short_code2 =='x' :
                            print("please check back to the app to save other credentials")
                            break


            else:
                print("Account does not exist")

        else:
            print("Incorrect shortcode, try another option "

        
            
            
            
if __name__ == "__main__":
    main()










