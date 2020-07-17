# Given a non-empty array of integers, return the k most frequent elements.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections
        
        # return zip(*collections.Counter(nums).most_common(k))[0]
			# for some reason, zipping it didn't work)

        return (ans for (ans, _) in collections.Counter(nums).most_common(k))

