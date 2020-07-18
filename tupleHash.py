# read in a number 'n' which tells you how many entries on next line
# on next line, read in integers
# then turn into a tuple
# then print the hash of this tuple

integer_list = map(int, input().split())
linz_tuple = ()

for _ in integer_list:
    linz_tuple += ( _, )
print(hash(linz_tuple))
