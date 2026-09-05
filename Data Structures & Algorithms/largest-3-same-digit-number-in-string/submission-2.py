class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s = set()
        large = ""

        for i in range(1, len(num)-1):
            if num[i-1] == num[i] == num[i+1]:
                if num[i] > str(large):
                    large = num[i]
        
        return large * 3