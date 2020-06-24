# Unique Binary Search Trees
# Find the number of binary search trees that store the values 1..n

class Solution:
    def numTrees(self, n: int) -> int:
        tree_count = {0: 1, 1: 1}   #start the dictionary with values for tree_count[0] and tree_count[1]

	for i in range(1, n):       #start at tree_count[2] 
            tree_count[i + 1] = sum([tree_count[k - 1] * tree_count[i + 1 - k] for k in range(1, i + 2)])
        return tree_count[n]
        
""" -=-=-=-=-=-
# Although it is really tempting to do recursively on one line, it gets real big real quick
def numTrees(self, n: int) -> int:
		return sum(numTrees(i) * numTrees(n - i - 1) for i in range(n)) if n else 1

    import time
    start_time = time.time()
    tree_sum = sum(numTrees(i) * numTrees(n - i - 1) for i in range(n)) if n else 1
    elapsed_time = time.time() - start_time
    return(elapsed_time)
	# for n=12, it took 1.1990642547607422 seconds
	# for n=13, it took 3.5041592121124268 seconds
	# for n=14 trees, it took 10.345100164413452 seconds
	# for n=15, it took 32.13046646118164 seconds
	# for n=16, it took 94.74207425117493 seconds
	# for n=17, it took 288.3008472919464 seconds

	# at which point I gave up and started to look at lru_cache, whic didn't provide any real improvement for cache_sizes of None, 128, 256, 512, 1024, 2048, or 65536 (2^16)
        
