class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        for b in range(len(prices)):
            for s in range(b+1, len(prices)):
                maxProf = max(prices[s] - prices[b], maxProf)
                
        return maxProf

                

        