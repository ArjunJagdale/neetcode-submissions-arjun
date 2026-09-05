class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index = 0
        p = 0

        for i in range(len(prices)):
            if prices[i] > prices[index]:
                p += prices[i] - prices[index]
            
            index = i
        
        return p