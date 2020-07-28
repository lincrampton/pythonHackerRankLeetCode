'''You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.'''
'''plan of attack:  after seeing if can escape on edge cases, find the most common and the spacing required between iterations.  then take the max of the numTimesRepeat-1 (because can bookend at the beginning+end) times the waitPeriod) and the length of the input string'''  
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        tasks_len = len(tasks)
        
        if n==0:
            return tasks_len
        
        if len(set(tasks)) == tasks_len:
            return tasks_len
        
        # am only here bcuz i cannot exit on edge cases
        import collections
    
        task_counts = list(collections.Counter(tasks).values())
        task_max_repeat = max(task_counts)  # have to space out the max
        count_max_task_repeat = task_counts.count(task_max_repeat) # are there more than one that need big spacing
        return max(tasks_len, ( (task_max_repeat-1)*(n+1) +count_max_task_repeat) )

input1 = ["A", "A", "A", "B", "B", "B"]
n1 = 0
output1 = 6
input0 = ["A", "A", "A", "B", "B", "B"]
n0 = 2
output0 = 8
print(leastInterval(input1, n1), \"should return\", output1)
print(leastInterval(input0, n0), \"should return\", output0)
