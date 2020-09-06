'''Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.  (Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?'''



class Solution7sept:
    def largestOverlap(self, A, B):

        if not(A):
            return 0
        
        import numpy as np
        A = np.array(A)
        B = np.array(B)

        dim_orig = len(A)
        dim_padded = 2*dim_orig -1
        B_padded = np.pad(B, dim_orig-1, mode='constant', constant_values=(0, 0))

        max_overlap = 0
        for x_shift in range(dim_padded):
            for y_shift in range(dim_padded):
                kernel = B_padded[x_shift:x_shift+dim_orig, y_shift:y_shift+dim_orig]
                non_zeros = np.sum(A * kernel)
                max_overlap = max(max_overlap, non_zeros)
        return max_overlap

Sol = Solution7sept()
A1 = [[1,1,0],[0,1,0],[0,1,0]]
B1 = [[0,0,0],[0,1,1],[0,0,1]]
out1 = 3
print(Sol.largestOverlap(A1, B1), 'should equal', out1)
