## Finding the Percentage ##
# input format: 
#     first line = numRecords
#     nextLine thru numRecords = studentName and 3 scores
#     lastLine is studentName
# program needs to output the average score corresponding to this name, format to 2 decimal places

testscores = {}
for _ in range(int(input())):
    linzline = input().split()
    testscores[linzline[0]] = list(map(float, linzline[1:]))
print( '{:.2f}'.format(sum(testscores[input()])/3) )
