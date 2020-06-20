''' first argument is the number of digits included in the permutation
	if the first argument is 3, then digits 1,2,3 permuted
	if the first argument is 5, then make all permutations of 1,2,3,4,5
    second argument is the desired permutation number  
	(assume permutations in ascending order)

    brute force would be to make all permutations, sort and pick off the one
   
    chose to understand that there are (n-1)! permutations 
    and strip off the permutations not needed '''

	
class SolutionXYZ:
    def getPermutation(self, n: int, k: int) -> str:
         # n is number of digits; k is desired permutation #
        
        if not n or not k:
            return ""
        
        if n==1:
            return str(n)
        
        def factorial(x):
            return 1 if x<2 else x*factorial(x-1)
        
        number_list = list(range(1,n+1))          # all the possible numbers
        kth_permut = ""                           # the k_th permutation to be returned
        
        for num in range(n,0,-1):
            fact_num_minus1 = factorial(num-1)    # calculate once and store
            digit = (k-1)//fact_num_minus1
            k -= digit*fact_num_minus1
            kth_permut += str(number_list[digit])
            number_list.remove(number_list[digit])
        return kth_permut

Sol = SolutionXYZ
print(Sol.getPermutation(3,3))
print(Sol.getPermutation(4,9))
print(Sol.getPermutation(1,270))
