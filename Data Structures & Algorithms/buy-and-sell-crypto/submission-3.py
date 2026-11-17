class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProf = 0
        for i, p in enumerate(prices):
            minPrice = min(p, minPrice)
            maxProf = max(p - minPrice, maxProf)
        return maxProf
                

                

        