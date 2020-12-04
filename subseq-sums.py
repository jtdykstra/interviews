"""
[1,1,1,2,2,3,1]
[1,2,3,5,7,10,11]
"""

class Solution:
    def subarraySum(self, nums, k):
        h = {}
        
        result = 0
        total = 0
        for i, v in enumerate(nums):
            h[i] = total
            total += v
        h[i+1] = total
        print(h)
        
        for i, v in enumerate(nums):
            for j in reversed(range(0,i+1)):
                print(str(i) + " " + str(j))
                print("h[i] " + str(h[i]))
                print("h[j] " + str(h[j]))
                if (h[i+1] - h[j] == k):
                    result += 1
        
        return result

sol = Solution()
print(sol.subarraySum([1,1,1], 2))
print(sol.subarraySum([1,2,1,2,1], 3))

"""
k = 3
[1,  2,  1,  2,  1]
[0,  1,  3,  4,  6, 7]
"""
