# author: G<iorgio
# date: 24.12.2023

import re

def transform_code():
    # Specify the input and output files
    input_file = "main.goofy"
    output_file = "data/script.py"

    # Specify word replacements (old_word: new_word)
    word_replacements = {
        "what if": "if",
        "is": "=",
        " equals ": "==",
        "banana ": "",
        "hearmeout": "def",
        "nvm": "else",
        "say": "print",
        "repeat": "for",
        "times": "in range",
        "as long as": "while ",
        "aint": "!=",
        "but also": " , ",
        "gimme": "return ",
        "hold on": "#",
            
        "print": "print? bro is trying to do python",
        "if": "if? are you serious? u must use `what if`",
        "else": "else? bro is trying to do python",
        "for": "for? why python bro? its goofy",
        "while": "while? why python bro? its goofy",
        ",": "why python bro? its goofy",
        "return": "this aint python but your code is goofy",
        "#": "this aint python but your code is goofy",
    }
    
    try:
        # Open the input file for reading
        with open(input_file, 'r') as f:
            # Read the content of the file
            content = f.read().lower()

        # Define a regular expression pattern to match words outside of strings
        pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, word_replacements.keys())) + r')\b(?![^"]*"(?:[^"]*"[^"]*")*[^"]*$)')
        content = pattern.sub(lambda match: word_replacements[match.group(0)], content)
        

        with open(output_file, 'w') as f:
            # Write the modified content to the output file, wrapped in def run():
            f.write("from math import *\n")
            f.write("def run():\n")
            
            # Indent each line of content
            indented_content = "    " + content.replace("\n", "\n    ")
            f.write(f"{indented_content}\n\n")

        # Import and run the transformed code
        from data.script import run
        run()
        
    except FileNotFoundError:
        print("Error: The `main.goofy` file ain't existin'")

if __name__ == "__main__":
    # Call the transform_code function if the script is executed
    transform_code()
