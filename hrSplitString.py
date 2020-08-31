'''Read a given string, change the character at a given index and then print the modified string.
The first line contains a string, The next line contains an integer n, denoting the index location and a character c separated by a space.'''


def mutate_string(string, position, character):
    # string = string[:position] + character + string[position+1:]
    # return string
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
