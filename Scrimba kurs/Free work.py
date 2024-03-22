class Solution:
    def __init__(self, strs) -> str:
        self.strs=strs

    def longestCommonPrefix(self, strs):
        common_pref=""
        while(True):
            for st in strs:
                if st[:len(common_pref)+1]!=common_pref:
                    return(common_pref)
        
            common_pref+=(strs[0])[len(common_pref)]


words_1=Solution(["flower","flow","flight"])

print(words_1.longestCommonPrefix(self))