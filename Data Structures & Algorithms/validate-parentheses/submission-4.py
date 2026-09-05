class Solution:
    def isValid(self, s: str) -> bool:
        brac = {")":"(", "]":"[", "}" : "{"}
        stack = []
        for ch in s:
            if ch in brac.values():
                stack.append(ch)
            elif not stack or stack.pop() != brac[ch]:
                return False
        
        return not stack


            