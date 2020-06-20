'''return a string that has upperCase->lowerCase and lowerCase->upperCase
     e.g., 'I am Sam I am!" would become "i AM sAM iAM!"
def swap_case(s):

    return_string = ""

    for i in range(len(s)):
        if s[i].islower():
            return_string += s[i].upper()
        elif s[i].isupper():
            return_string += s[i].lower()
        else:
            return_string += s[i]

    return return_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
