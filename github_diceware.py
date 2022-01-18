#!/usr/local/bin/python3
# diceware.py - Generates a diceware passphrase using the EFF long word list.
# In place of physical dice, it uses the python library quantumrandom to get
# true random numbers from quantum fluctation measurements inside a vacuum
# chamber at Australia National University where they provide the data on a
# server.

# TODO: Get this file ready for github by doing things like prompting the user
# for the wordlist file path instead of hard coding it. Push it to github and
# then post it in a python reddit.

# Allow less than 6 words but provide a warning for passwords.

import sys
import quantumrandom
import pyinputplus as pyip

def print_nnl(input):
    # print no new line
    sys.stdout.write(input)
    sys.stdout.flush()

def main():
    print("Welcome to the diceware passphrase script. I will generete a "\
    "diceware passphrase for you quickly and easily on your machine while "\
    "still using random numbers, perhaps even more random than physical dice.")
    # Open the EFF word list and read it.
    file_path = "/home/zachary/zachary/Documents/eff_large_wordlist_diceware.txt"
    try:
        with open(file_path, "r") as word_list_file:
            file_contents = word_list_file.readlines()
    except Exception as e:
        print("Error opening file: {}".format(str(e)))

    # Split the numbers and words and put them in a dictionary to be looked
    # up later.
    word_list = {}
    for line in file_contents:
        word = line.split()
        word_list[word[0]] = word[1]

    # Prompt the user for their desired passphrase length. Sufficient security
    # dictates at least 6 words, recommended 8, and using more than 10 words
    # is probably redudant. I use the pyinputplus library to easily validate
    # user input.
    passphrase_length = pyip.inputNum("\nPlease enter how many words you "\
    "would like in your passphrase (recommended 8): ", min=6, lessThan=11)

    # Prepare a list to receive the quantum data.
    quantum_data = []

    # Downloading the quantum data:
    # Get an NumPy array of 16 bit unsighned integers and convert it to a list.
    try:
        print_nnl("Rolling quantum dice...")
        quantum_data = quantumrandom.uint16().tolist()
    except Exception as e:
        print("Error: {}".format(str(e)))
    else:
        print("[OK]")

    # Convert the ints to strings.
    quantum_data = [str(i) for i in quantum_data]

    # Prepare a list to store the "dice numbers" you would get if you were
    # rolling physical dice.
    dice_numbers = []

    # The numbers on the EFF word list are formatted for 6 sided dice and the
    # quantum server dumps a list of garbage numbers, so we have to filter them.
    unwanted_numbers = ['7', '8', '9', '0']

    # Loop through the raw data
    for quantum_number in quantum_data:
        # 1. We only want strings that are 5 long so ignore everything else.
        if len(quantum_number) != 5:
            continue
        else:
            # 2. If a string has a number greater than 6,
            #   skip and go to the next.
            if any(number in quantum_number for number in unwanted_numbers):
                continue
            else:
                # 3. Otherwise the number should be good so add it.
                if len(dice_numbers) < passphrase_length:
                    dice_numbers.append(quantum_number)
        # Once we have enough strings for the passphrase, stop looping.
        if len(dice_numbers) == passphrase_length:
            break

    readable_passphrase = ""
    passphrase = ""
    # Use the numbers to look up the words and add them to the passphrase.
    for number in dice_numbers:
        readable_passphrase += word_list[number] + " "
    for number in dice_numbers:
        passphrase += word_list[number]

    # Display the passphrase.
    print("Passphrase (readable): " + readable_passphrase)
    print("Passphrase (for copying): " + passphrase)

if __name__ == "__main__":
    main()
