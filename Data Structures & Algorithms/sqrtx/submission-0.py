class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        res = 0

        while l <= r:
            m = l + (r - l) // 2

            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                res = m
            else:
                return m
        
        return res

"""
1 2 3 4 5 6 7 8 9
    l
    r
  
"""