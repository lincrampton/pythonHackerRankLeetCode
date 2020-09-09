'''Compare two version numbers version1 and version2.  If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.  You may assume that the version strings are non-empty and contain only digits and the . character.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.'''

class Solution9sept:
    def compareVersion(self, version1, version2):
        
        import itertools

        version1_l = [int(v) for v in version1.split(".")]
        version2_l = [int(v) for v in version2.split(".")]
        
        for v1, v2 in itertools.zip_longest(version1_l, version2_l, fillvalue=0):
            if v1 > v2:
                return 1
            elif v2 > v1:
                return -1
        
        return 0

Sol = Solution9sept()
input1a = "0.1"
input1b = "1.1"
output1 = -1

input2a = "1.0.1"
input2b = "1"
output2 = 1

print(Sol.compareVersion(input1a, input1b), '=', output1)
print(Sol.compareVersion(input2a, input2b), '=', output2)
