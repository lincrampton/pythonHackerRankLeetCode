'''Given a non-empty array of digits representing a non-negative integer, plus one to the integer.  '''
# class Solution6july:
def plusOne(digits):
    if digits[-1] != 9:
        digits[-1] += 1
    else:
        digits = list(str(int("".join(map(str,digits)))+1))

    return digits


input1 = [1,2,3]
output1 = [1,2,4]

input2 = [4,3,2,1]
output2 = [4,3,2,2]
                       
print(plusOne(input1))
print(plusOne(input2))
