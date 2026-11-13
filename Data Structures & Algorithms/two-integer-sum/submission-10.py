class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in found:
                return [found[diff], i]
            found[v] = i
