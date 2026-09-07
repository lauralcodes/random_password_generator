# Random Password Generator
# This program generates a random password based on user preferences.
# Get user input for:
#   password length
#   character types to include:
#      - uppercase letters
#      - lowercase letters
#      - special characters
#      - digits
# get all available characters based on user input
# randomly select characters from the available characters to create a password of the desired length
# ensure that the password contains at least one character from each selected character type
# ensure the length is valid (between 8 and 128 characters)   

import random
import string



def design_pw():
   
    try:
        pw_length = int(input(" Enter the password length? ").strip())
        if  pw_length < 8 or pw_length > 128: # validate the length
            print( "Password length should be between 8-128")
            #return pw_length
    except ValueError:
        print("Please enter a valid number.")

    while True:
        include_uppercase = input ("Do you want to include upper case letters: Yes/No ").strip().lower()
        if include_uppercase != "yes" and include_uppercase != "no":
            print("Please enter either 'yes' or 'no'.")
        else:
            break
        #return include_uppercase

    while True:
        include_lowercase = input ("Do you want to include lower case letters: Yes/No ").strip().lower()
        if include_lowercase != "yes" and include_lowercase != "no":
            print("Please enter either 'yes' or 'no'.")
        else:
            break
        #return include_lowercase

    while True:
        include_sp_characters = input ("Do you want to include special characters: Yes/No ").strip().lower()
        if include_sp_characters != "yes" and include_sp_characters != "no":
            print("Please enter either 'yes' or 'no'.")
        else:
            break
        #return include_sp_characters

    while True:
        include_digits = input ("Do you want to include digits: Yes/No ").strip().lower()
        if include_digits != "yes" and include_digits != "no":
            print("Please enter either 'yes' or 'no'.")
        else:
            break
        #return include_digits

    lower_collection = string.ascii_lowercase if include_lowercase == "yes" else ""  # inline IF statement or a Ternary statement
    upper_collection = string.ascii_uppercase if include_uppercase == "yes" else ""
    sp_character_collection = string.punctuation if include_sp_characters == "yes" else ""
    digits_collection = string.digits if include_digits == "yes" else ""

    all_desired_characters = lower_collection + upper_collection + sp_character_collection + digits_collection

    requires_characters =[]
    if include_uppercase == "yes":
        requires_characters.append (random.choice(upper_collection))
    if include_lowercase == "yes":
        requires_characters.append (random.choice(lower_collection))
    if include_sp_characters == "yes":
        requires_characters.append (random.choice(sp_character_collection))
    if include_digits == "yes":
        requires_characters.append (random.choice(digits_collection))

    remaining_length = pw_length - len(requires_characters)

    password = requires_characters

    for _ in range(remaining_length):
        remaining_characters = random.choice(all_desired_characters)
        password.append(remaining_characters)

    random.shuffle(password)

    final_string_password = "".join(password)       # here combine all the characters which has separated bu ""

    print(final_string_password)



design_pw()





