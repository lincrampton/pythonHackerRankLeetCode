'''given a string and a max_width, return a paragraph string with lines of length max_width'''
import textwrap

def wrap(string, max_width):

    new_string=""
    for c in range(0, len(string), max_width):
        new_string += string[c : c+max_width] + "\n"

    return(new_string)
