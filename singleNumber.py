#Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

# since a set is unique, turn the input array into a set, triple that set 
# and subtract the sum of that set from the sum of the original array
# and then divide the answer in two, ensuring it is not floating point

        return (3 * sum(set(nums)) - sum(nums))//class



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# or if you want to see the whole Enchilada

class SolutionAba:
    def singleNumber(nums):
        return (3 * sum(set(nums)) - sum(nums))//2

        
Sol = SolutionAba
input1 = [0,1,0,1,0,1,99]
desiredOutput1 = 99
input2 = [2,2,3,2]
desiredOutput2 = 3
print(Sol.singleNumber(input1), desiredOutput1)
print(Sol.singleNumber(input2), desiredOutput2)
