# array  nums  has n+1  integers where each is between 1..n inclusively.
# find the duplicate num (it may be duplicated more than once)

def findDuplicate(nums):
    return (sum(nums) -  sum(set(nums)))//(len(nums) - len(set(nums)))

# takes advantage of uniqueness of set
# if nums is xyxzabxc (= 3*x+y+z+a+b+c) then  set nums is xyzabc
# and sum of nums is 3*x+y+z+a+b+c) 
# set(sum) of nums is  x+y+z+a+b+c
# subtract the sum(set) for the sum and you get 2x
# subtract the length of set(nums) from the length of nums and you get 2

