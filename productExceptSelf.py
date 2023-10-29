class Solution(object):
    def productExceptSelf(self, nums):
        res = []
        acc = 1
        for n in nums:
            res.append(acc)
            acc *= n
        acc = 1
        for i in reversed(range(len(nums))):
            res[i] *= acc
            acc *= nums[i]

        return res

    def productExceptSelf2(self, nums):
        answer, lookup = [], {}
        for idx in range(len(nums)):
            num = nums[idx]
            if num not in lookup:
                lookup[num] = Math.prod(nums[:idx] + nums[idx + 1:])
            answer.append(lookup[num])
        return answer


solution = Solution()
print(solution.productExceptSelf(nums=[-1, 1, 0, -3, 3]))
