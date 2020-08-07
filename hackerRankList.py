'''insert i e: 
	1	Insert integer  at position .
	2	print: Print the list.
	3	remove e: Delete the first occurrence of integer .
	4	append e: Insert integer  at the end of the list.
	5	sort: Sort the list.
	6	pop: Pop the last element from the list.
	7	reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.  '''

#if __name__ == '__main__':

	arr = []

	for i in range(int(input())):

		cmd  = input().split()
		if len(cmd) > 1:
			for n in range(1,len(cmd)):
				cmd[n] = int(cmd[n])
		

		if cmd[0] == 'insert':
			arr.insert(cmd[1], cmd[2])
		elif cmd[0] == 'print':
			print(arr)
		elif cmd[0] == 'remove':
			arr.remove(cmd[1])
		elif cmd[0] == 'append':
			arr.append(cmd[1])
		elif cmd[0] == 'sort':
			arr.sort()
		elif cmd[0] == 'pop':
			arr.pop()
		elif cmd[0] == 'reverse':
			arr.reverse()
		else:
			pass
	
