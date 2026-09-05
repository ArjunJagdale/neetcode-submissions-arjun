class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "|" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i # both i and j are same initially

            while s[j] != "|": # till the j reaches the | keep incrementing
                j += 1
            
            # once we have reached the position i where i + 1 == "|"
            # get the length of current word, which before the "|"

            length = int(s[i:j])
            # now we have to increament i and j to be at start and end of the word
            i = j + 1
            j = length + i

            res.append(s[i:j])

            i = j 
        
        return res
