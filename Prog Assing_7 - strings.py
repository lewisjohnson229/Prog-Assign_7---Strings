# Author: Lewis Johnson
# Program: Prog Assign_7 - Strings
# Date: Oct. 24, 2026
# Git hub link https://github.com/lewisjohnson229/Prog-Assign_7---Strings/blob/main/Prog%20Assing_7%20-%20strings.py

# Get a phone number from the user in the format XXX-XXX-XXXX.
# The user can type uppercase letters, lowercase letters, or both.
# Keep asking until the user enters the right amount.
while True:
    phone_number = input('Enter a telephone number (XXX-XXX-XXXX, any letter case): ')

    # Count the characters without the hyphens for the user.
    if len(phone_number.replace('-', '')) == 10:
        # Leave the loop when the length is correct.
        break

    # Explain the problem for the user before asking again.
    print('Please enter 10 characters, not counting the hyphens.')

# Make the letters uppercase so capitalization does not matter for the user.
# This keeps any numbers and hyphens the user already typed.
translated_number = phone_number.upper()

# These are the letter groups on a phone keypad, in order from 2 to 9.
letter_groups = ('ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')
# Start at 2 because 0 and 1 do not have letters on the keypad.
digit = 2

# Go through the letter groups one at a time.
for group in letter_groups:
    # Go through each letter in the current group.
    for letter in group:
        # Change every matching letter to its keypad number.
        # str(digit) makes the number text so replace() can use it.
        # Save the updated string because replace() gives back a new one.
        translated_number = translated_number.replace(letter, str(digit))
    # Move to the next keypad number when this group is finished.
    digit += 1

# Show the finished phone number outcome
print('Numeric telephone number:', translated_number)
