'''Given an integer, , print the following values for each integer  from  to :
Decimal   Octal   Hexadecimal (capitalized)   Binary'''
def print_formatted(number):
    width = len('{:b}'.format(number))  # because this will be the longest
    for i in range(1,number+1):
        print(str.rjust(str(i),width),str.rjust(str(oct(i)[2:]),width),str.rjust(str(hex(i).upper()[2:]),width),str.rjust(str(bin(i)[2:]),width))
print_formatted(21)
