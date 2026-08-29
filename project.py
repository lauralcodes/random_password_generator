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
        if  pw_length < 8 or pw_length > 128:
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




# def main():
#     # Get valid password length
#     while True:
#         try:
#             pw_length = int(input("Enter the length of the password (8-128): ").strip())
#         except ValueError:
#             print("Please enter a valid number.")
#             continue
#         if 8 <= pw_length <= 128:
#             break
#         print("Invalid password! length should be between 8 and 128.")

#     # Ask which character types to include
#     while True:
#         include_uppercase = ask_yes("Do you want to include upper case letters?")
#         include_lowercase = ask_yes("Do you want to include lower case letters?")
#         include_sp_characters = ask_yes("Do you want to include special characters?")
#         include_digits = ask_yes("Do you want to include digits?")

#         if not (include_uppercase or include_lowercase or include_sp_characters or include_digits):
#             print("Select at least one character type.")
#             continue
#         # ensure length can accommodate at least one of each selected type
#         selected_count = sum([include_uppercase, include_lowercase, include_sp_characters, include_digits])
#         if pw_length < selected_count:
#             print(f"Password length must be at least {selected_count} for the selected character types.")
#             # ask for length again
#             while True:
#                 try:
#                     pw_length = int(input(f"Enter a new length (>= {selected_count}): ").strip())
#                 except ValueError:
#                     print("Please enter a valid number.")
#                     continue
#                 if pw_length >= selected_count and 8 <= pw_length <= 128:
#                     break
#                 print("Invalid length.")
#         break

#     pools = []
#     required_chars = []
#     if include_lowercase:
#         pools.append(string.ascii_lowercase)
#         required_chars.append(random.choice(string.ascii_lowercase))
#     if include_uppercase:
#         pools.append(string.ascii_uppercase)
#         required_chars.append(random.choice(string.ascii_uppercase))
#     if include_digits:
#         pools.append(string.digits)
#         required_chars.append(random.choice(string.digits))
#     if include_sp_characters:
#         # Common punctuation characters for passwords
#         pools.append(string.punctuation)
#         required_chars.append(random.choice(string.punctuation))

#     available_chars = "".join(pools)

#     remaining_len = pw_length - len(required_chars)
#     password_chars = required_chars + [random.choice(available_chars) for _ in range(remaining_len)]
#     random.shuffle(password_chars)
#     password = "".join(password_chars)

#     print("Generated password:", password)


# if __name__ == "__main__":
#     main()





