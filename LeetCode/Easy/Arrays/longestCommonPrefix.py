from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        lst2 = sorted(strs, key=len)

        longest = ""
        first_word = lst2[0]
        i = 0
        
        while i < len(first_word):
            char = first_word[i]

            for j in range(1, len(lst2)):
                if lst2[j][i] != char:
                    return longest
                    break;
            
            longest = longest + char
            i += 1
        
        return longest
        

