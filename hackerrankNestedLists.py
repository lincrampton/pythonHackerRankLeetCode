#Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

#Input Format:  The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

testscores = [[ input(), float(input())] for i in range(int(input()))]
sorted_scores = sorted(set([x[1] for x in testscores]))
for name in sorted(x[0] for x in testscores if x[1] == sorted_scores[1]):
    print(name)
    
