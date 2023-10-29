class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
        

solution = Solution()

print(solution.twoSum([2,7,11,15], 9))
