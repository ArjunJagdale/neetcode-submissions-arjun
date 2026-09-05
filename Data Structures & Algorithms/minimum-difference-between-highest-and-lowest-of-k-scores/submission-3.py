class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        MAX_VAL = 100000
        frq = [0] * (MAX_VAL + 1)

        for num in nums:
            frq[num] += 1
        
        left = count = 0
        ans = float("inf")

        for right in range(MAX_VAL + 1):
            count += frq[right]

            while count >= k:
                ans = min(ans, right - left)
                count -= frq[left]
                left += 1
        
        return ans
