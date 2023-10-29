class Solution(object):
    def topKFrequent(self, nums, k):
        counter = {}
        arr = []
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else: 
                counter[num] = counter.get(num) + 1
        while len(arr) < k:
            arr.append(max(counter, key=counter.get))
            counter.pop(max(counter, key=counter.get))
        return arr

solution = Solution()

print(solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
