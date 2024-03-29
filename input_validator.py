
valid_name = False      # sets up boolean for while loop

# while loop that takes user input of name and checks it is valid i.e. there are no numerical characters.
# while loop repeats until a valid name is entered.
while not valid_name:
    user_name = str(input("Please enter your first name: "))
    if user_name.isalpha():
        print("First name accepted.")
        valid_name = True
    else:
        print("Invalid first name. Please try again.")

# repeat of the above for surname this time.
valid_surname = False

while not valid_surname:
    user_surname = str(input("Please enter your surname: "))
    if user_surname.isalpha():
        print("Surname accepted.")
        valid_surname = True
    else:
        print("Invalid surname. Please try again.")

valid_phone = False

# while loop to confirm inputted phone number is in correct form.
while not valid_phone:
    user_phone = str(input("Please enter your phone number in the format 07XXX XXXXXX: "))
    # remove any spaces from user_phone to make more consistent and easy to work with
    stripped_number = user_phone.replace(" ", "")
    number_length = len(stripped_number)
    includes_letters = False
    wrong_start = False
    wrong_length = False

    # check that input only contains numerical digits. Print matching error message if not true.
    if not stripped_number.isdigit():
        print("Phone number can not include alphabetical or special characters. Please try again.")
        includes_letters = True
    # check that number begins with 07. Print matching error message if not true.
    if stripped_number[0:2] != "07":
        print("UK phone number must begin with '07'. Please try again.")
        wrong_start = True
    # check that exactly 11 digits have been entered. Print matching error message if not true.
    if number_length != 11:
        print("Phone number is the incorrect number of digits. Please enter a UK phone number in the format 07XXX XXXXXX. Please try again.")
        wrong_length = True


    # if no errors found above, accept phone number and break out of loop.
    if not (includes_letters or wrong_start or wrong_length):
        print("Phone number accepted.")
        valid_phone = True
    
valid_email = False

while not valid_email:
    user_email = input('Please enter your email here: ')
    # Check for presence of a @ character
    no_at = False
    no_full_stop = False
    if '@' not in user_email:
        print("Email not accepted. Email address must include an '@' symbol")
        no_at = True
    else:
        # input definitely includes a @ character
        at_index = user_email.index('@')
        # Check for full stop after the @ character
        if '.' not in user_email[at_index:]:
            no_full_stop = True
            print("Email not accepted. Email domain must include a full stop ('.')")

    if not (no_at or no_full_stop):
        print('Email address accepted.')
        valid_email = True


# Password
valid_password = False

while not valid_password:
    user_password = input("Please enter a password. Password must include a capital letter and a number: ")
    password_check = input("Please re-enter your password to confirm: ")

    # check passwords entered match
    non_match= False
    if user_password != password_check:
        print("Passwords must match. Please try again.")
        non_match = True

    # check there is a number in the password
    no_number = False
    if not any(char.isdigit() for char in user_password):
        print("Password must contain a number. Please try again.")
        no_number = True

    # check there is a capital letter
    no_capital = False
    if not any(char.isupper() for char in user_password):
        print("Password must contain a capital letter. Please try again.")
        no_capital = True
    
    # if inputted password has a capital and a number, and both inputted passwords match, break out of while loop
    if not(non_match or no_number or no_capital):
        print("Password accepted.")
        valid_password = True
        
    
print("You have provided the following details:")
print(f"Name: {user_name} {user_surname}")
print(f"Phone Number: {user_phone}")
print(f"Email Address: {user_email}")
hidden_password = ''.join(['*' for char in user_password])
print(f"Password: {hidden_password}")
print("Thank you for using the input validator.")