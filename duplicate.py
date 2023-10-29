class Solution(object):
    def containsDuplicateHash(self, nums):
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        print(seen)
        return False


    def containsDuplicateSet(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for index, num in enumerate(nums):
            if num in seen and abs(index - seen[num]) <= k:
                return True
            else:
                seen[num] = index
                print(seen)

        return False


solution = Solution()

