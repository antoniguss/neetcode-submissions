from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodUpTo = [0]*(len(nums))
        prodFrom = [0]*(len(nums))

        prodUpTo[0] = nums[0]
        for i, n in enumerate(nums[1:], 1):
            prodUpTo[i] = prodUpTo[i-1] * n

        prodFrom[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            prodFrom[i] = prodFrom[i+1] * nums[i]

        result = [1]*len(nums)
        for i in range(len(nums)):
            if i > 0:
                result[i] *= prodUpTo[i-1]
            if i < len(nums) - 1:
                result[i] *= prodFrom[i+1]

        # print(prodUpTo)
        # print(prodFrom)

        return result




        