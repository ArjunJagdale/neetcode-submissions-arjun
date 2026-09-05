class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev_str = ''
        string = s.lower()
        
        for i in string:
            if i.isalnum():
                rev_str += i
        
        return rev_str == rev_str[::-1]
            