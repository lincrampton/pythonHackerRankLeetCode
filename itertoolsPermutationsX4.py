#!/usr/bin/env python
# coding: utf-8


'''--- Itertools.permutations --- done 4 ways
You are given a string S.  Your task is to print all 
possible permutations of size k of the string in 
lexicographic sorted order.

Input Format: A single line containing the space separated 
string S and the integer value k.'''


from itertools import permutations

word, num = input().split(" ")
permutations = list(permutations(word, int(num)))
permutations.sort()

for i in permutations:
    print("".join(i))


# -=-=-=-

from itertools import permutations

word, num = input().split(" ")
permutations = list(permutations(word, int(num)))
permutations.sort()

[print("".join(i)) for i in permutations]


# -=-=-=-

from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')


# -=-=-

s=input().split() 
a=int(s[1]) 
string=s[0] 
from itertools import permutations 
p=list(permutations(sorted(string),a)) 
for x in p: 
    for y in x: 
        print(y,end="") 
    print()
