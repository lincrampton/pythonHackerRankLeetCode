'''A complex number can be represented as a string on the form "real+imaginaryi" where:
real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number 
that represents their multiplications.'''
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        real1, img1 = map(int, num1[:-1].split('+'))
        real2, img2 = map(int, num2[:-1].split('+'))
        
        return '%d+%di' % ( (real1 * real2) - (img1 * img2),  (real1 * img2) + (img1 * real2) )
