class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_p = 0
        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
            else:
                p = prices[j] - prices[i] # 4
                max_p = max(max_p, p) # 4
            j += 1
        
        return max_p
            


