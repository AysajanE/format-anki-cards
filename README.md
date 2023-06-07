# Anki Card Formatter

Anki Card Formatter is a Python script that reformats content of a `.txt` file, specifically for Anki cards. It reads an input file, considers only the lines containing 'Front' and 'Back', and then writes the reformatted content into a new output file.

## Features

- Reads from an existing .txt file.
- Considers lines containing 'Front' and 'Back' words.
- The output file name is derived from the input file name, prefixed with "reformatted".
- Output format is `question;answer`, useful for import into Anki or other flashcard software.

## Usage

This script is designed to be run from the command line. Here's the usage:

```shell
python reformat_anki_cards.py input_file.txt
```

This will create a new file called reformattedinput_file.txt in the same directory as the script, containing the reformatted content.

## Requirements
This script requires Python 3.6 or later.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
