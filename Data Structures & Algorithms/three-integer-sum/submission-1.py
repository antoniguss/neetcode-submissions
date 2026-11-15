class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()

        for i,n in enumerate(nums):
            target = -n
            l = i+1
            r = len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum == target:
                    result.add(tuple([n, nums[l], nums[r]]))
                    l += 1
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
        
        return list(result)



        