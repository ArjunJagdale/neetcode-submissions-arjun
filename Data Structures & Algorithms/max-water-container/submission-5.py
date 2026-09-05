class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        s = 0
        while i < j:
            n = j - i
            if heights[i] < heights[j]:
                s = max(s, heights[i] * n)
                i += 1
            else:
                s = max(s, heights[j] * n)
                j -= 1
        
        return s
