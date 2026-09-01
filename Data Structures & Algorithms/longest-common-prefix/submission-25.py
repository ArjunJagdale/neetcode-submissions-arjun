class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])): # iterate over the first word of the arr
            for s in strs: # iterate over the words in array
                if i == len(s) or s[i] != strs[0][i]:
                    # check if current index equals len of curr word or current word[i] does not eq to first word[i]
                    return s[:i] # return all the chars in that word till current index
        
        return strs[0] # return whole first word