'''Write a program that outputs the string representation of numbers from 1 to n.  But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        def zzFunc(i):
            if i % 15 == 0:
                return "FizzBuzz"
            if i % 3 == 0:
                return "Fizz"
            if i % 5 == 0:
                return "Buzz"
            return str(i)
        
        return [ zzFunc(num) for num in range(1, n+1) ]
