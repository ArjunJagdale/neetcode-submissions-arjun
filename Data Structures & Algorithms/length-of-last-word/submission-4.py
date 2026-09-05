class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 1

        if len(s) <= 1:
            return count
            
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                return count - 1
            count += 1
            
        
        
                