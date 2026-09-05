class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check if they have same lengths or not
        if len(s) != len(t):
            return False
        
        # now check and update the occurances of the chars
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1 # update the count of the char occuring by 1.
            # even if it returns 0 add 1 to it to make the count 0 again in below code
        
        for char in t:
            # if char is not in count or if it is occuring for 0 times
            if char not in count or count[char] == 0:
                return False
            # or subtract 1 from the occurance of the character
            count[char] -= 1
        
        return True




        