class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        s = 0

        while i < j:
            n = j - i
            if heights[i] < heights[j]:
                s = max(s, n * heights[i])
                i += 1

            else:
                s = max(s, n * heights[j])
                j -= 1
        
        return s