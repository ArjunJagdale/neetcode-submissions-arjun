class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num

        while l <= r:
            mid = (l+r) // 2
            sq = mid * mid

            if sq > num:
                r = mid - 1
            elif sq < num:
                l = mid + 1
            else:
                return True
        
        return False