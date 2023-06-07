import os
import sys

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

    # Filter the lines to only include those with 'Front' or 'Back' in them
    lines = [line for line in lines if 'Front' in line or 'Back' in line]

    with open(output_file, 'w') as out_file:
        for i in range(0, len(lines), 2): # Assuming each 'Front' line is followed by a 'Back' line
            # Split the line at the colon and strip any leading or trailing whitespace
            question_line = lines[i]
            answer_line = lines[i+1]

            # Split the line at the colon and strip any leading or trailing whitespace
            question = question_line.split(':', 1)[1].strip()
            answer = answer_line.split(':', 1)[1].strip()

            # Write the reformatted line to the output file
            out_file.write(f"{question};{answer}\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the input file name")
    else:
        input_file = sys.argv[1]
        reformat_anki_cards(input_file)
