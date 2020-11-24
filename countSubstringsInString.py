'''The user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.'''

def count_substring(string, sub_string):
    return sum(1 for s in range(len(string)) if string.startswith(sub_string, s))
        
    # couldn't find regex module
    # import regex as re
    # return len(re.findall(sub_string, string, overlapped=True))
    # return(string_count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
