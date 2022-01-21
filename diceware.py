import sys
import quantumrandom
import pyinputplus as pyip
from ConsoleColor import ConsoleColor

# Function to print with no new line
def print_nnl(input):
    sys.stdout.write(input)
    sys.stdout.flush()

def main():
    color_message = ConsoleColor()

    print("Welcome to the diceware passphrase script. This script gets true"\
    " random numbers from quantum fluctations measured in a vacuum chamber "\
    "located at Australia National University.")
    # Open the EFF word list and read it.
    file_path = "eff_large_wordlist_diceware.txt"
    try:
        with open(file_path, "r") as word_list_file:
            file_contents = word_list_file.readlines()
    except Exception as e:
        print("Error opening file: {}".format(str(e)))

    # Split the numbers and words and put them in a dictionary.
    # TODO: Might need to strip the newline characters off the words
    word_list = {}
    for line in file_contents:
        word = line.split()
        word_list[word[0]] = word[1]

    passphrase_length = pyip.inputNum("\nPlease enter how many words you "\
    "would like in your passphrase (recommended 8): ", min=6, lessThan=11)

    quantum_data = []

    # Get a NumPy array of 16 bit unsighned integers and convert it to a list.
    try:
        print_nnl("Rolling quantum dice...")
        quantum_data = quantumrandom.uint16().tolist()
    except Exception as e:
        print("Error: {}".format(str(e)))
    else:
        print(color_message.ok())

    # Convert the ints to strings
    quantum_data = [str(i) for i in quantum_data]

    dice_numbers = []
    unwanted_numbers = ['7', '8', '9', '0']
    discarded_numbers = 0

    for quantum_number in quantum_data:
        if len(quantum_number) != 5:
            discarded_numbers += 1
            continue
        else:
            if any(number in quantum_number for number in unwanted_numbers):
                discarded_numbers += 1
            else:
                if len(dice_numbers) < passphrase_length:
                    dice_numbers.append(quantum_number)
        if len(dice_numbers) == passphrase_length:
            break

    passphrase_readable = ""
    passphrase = ""

    for number in dice_numbers:
        passphrase_readable += word_list[number] + " "
    for number in dice_numbers:
        passphrase += word_list[number]

    print("Passphrase (readable): " + passphrase_readable)
    print("Passphrase (for copying): " + passphrase)

if __name__ == "__main__":
    main()
