import os
import sys
import re

def reformat_anki_cards(input_file):
    """
    This function reformats the content of a .txt file.
    It specifically extracts lines containing 'Front' and 'Back', then reformats them into a new file.

    Args:
        input_file (str): The path of the input .txt file to be reformatted.

    Returns:
        None. A new file will be created with reformatted content.
    """

    # Output file name will be 'reformatted' + input file name
    output_file = 'reformatted_' + os.path.basename(input_file)

    with open(input_file, 'r') as in_file:
        # Read the file line by line
        lines = in_file.readlines()

    with open(output_file, 'w') as out_file:
        for line in lines:
            # Check if both 'Front' and 'Back' are present in the same line
            if 'Front' in line and 'Back' in line:
                # Split the line at '**Back**: ' to separate the question and answer
                front_part, back_part = line.split('**Back**: ')
                # Further split to extract question and answer
                question = front_part.split('**Front**: ')[1].strip()
                answer = back_part.strip()
            else:
                # If 'Front' and 'Back' are in different lines, just process them as earlier
                if 'Front' in line:
                    question = line.split(':', 1)[1].strip()
                elif 'Back' in line:
                    answer = line.split(':', 1)[1].strip()
                else:
                    continue # Skip lines that don't have either 'Front' or 'Back'
            # Write the reformatted line to the output file
            out_file.write(f"{question};{answer}\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the input file name")
    else:
        input_file = sys.argv[1]
        reformat_anki_cards(input_file)
