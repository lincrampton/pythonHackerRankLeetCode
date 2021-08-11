'''array of doubled pairs
Given an array of integers arr of even length, return true if 
and only if it is possible to reorder it such that 
arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2
'''
def canReorderDoubled(arr):
    c = collections.Counter(arr)
    for x in sorted(c, key=abs):
        if c[x] > c[2 * x]:
            return False
        c[2 * x] -= c[x]
    return True

input1f = [1,2,4,16,8,4]
input2t = [4,-2,2,-4]
input3f = [2,1,2,6]
input4f = [3,1,3,6]

print('should return false and does return', canReorderDoubled(input1f))
print('should return true and does return', canReorderDoubled(input2t))
print('should return false and does return', canReorderDoubled(input3f))
print('should return false and does return', canReorderDoubled(input4f))
