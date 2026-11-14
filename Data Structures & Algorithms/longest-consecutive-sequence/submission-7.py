class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxLen = 0
        for n in nums:
            if (n-1) in numSet:
                continue
            i = n
            l = 1
            while (i+1) in numSet:
                i += 1
                l += 1
            if i - n + 1 > maxLen:
                maxLen = l


        return maxLen

