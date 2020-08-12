'''Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.'''

class Solution12aug:
	def getRow(self, rowIndex):
		row = [1]     #every row starts with 1
		
		for P in range(1, rowIndex+1):   
			row.append(row[P-1] * (rowIndex-P+1)//P)
	
		return row	


input1 = 3
output1 = [1,3,3,1]

Sol = Solution12aug()
print(Sol.getRow(input1), 'should equal', output1)
