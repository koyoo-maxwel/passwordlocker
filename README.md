# [PasswordLocker](**)
**Password locker is a simple python app that generates passwords for different user accounts**
### aug 23rd, 2018
#### By **[koyoo-maxwel](http://juantechno.com/maxwell-koyoo/)**

## Description
Password Locker is an application that helps users generate and store passwords on their multiple accounts.
The password locker runs on the terminal and uses short codes to navigate through it.
When starting up the application, the user is met with the following shortcodes:

    1. cc - Creates a new account
    2. ss - Sign in
    3. ex - Exit the application

The user will be met with the following commands while signing in:

    1. ad - Add password
    2. vp - View passwords
    3. cp - Copy password to clipboard
    4. lo - Log out

## Specifications
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Create new account | Type: cc <br>Username: ()name <br>Password: pass | User (name) has been created.<br>Log in to Continue |
| Sign in | Type: ss <br>Username: (enter-username)<br>Password: pass | Welcome (username--)! What would you like to do? |
| Add Password | Type: ad <br>Website: mywebsite.com <br>Length of password: 10 | **Generates a password with x length**<br>Your password for mywebsite.com (---) |
| View list of passwords | Type: vp | Generates a lists of websites and passwords |
| Copy Password to clipboard | Type: cp <br>Enter index: 1 | Password 1 on the list has been copied and is ready for pasting |
| Log Out | Type: lo | **Logs out the user** <br>Goodbye `name`! |
| Exit Application | Type: ex | **Closes the application** <br>Goodbye!! |


##  Prerequiites

    - Python 3.6 required

## Set-up and Installation
    - Clone the Repo [password-locker](https://github.com/koyoo-maxwel/password-locker.git)
    - Install python 3.6
    - Run `python3.6 run.py`

## Known bugs
No known errors if found drop a message on my profile

## Technologies used
    - Python 3.6

## Support and contact details
Contact me on developer. koyoomaxwel@gmail.com for any comments, reviews or advice.
[koyoo-maxwel](http://juantechno.com/maxwell-koyoo/)

### License
[Copyright] (c)**koyoo-maxwel**

[MIT License](LICENSE)

Copyright (c) 2018 koyoo maxwel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sub-license, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
