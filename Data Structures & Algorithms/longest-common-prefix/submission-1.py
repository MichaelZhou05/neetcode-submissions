class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestIndex = 0
        currChar = None
        i = 0 
        while i < len(strs):
            print(i)
            if longestIndex >= len(strs[i]):
                return strs[i]
            if i == 0:
                currChar = strs[0][longestIndex]
            if strs[i][longestIndex] != currChar:
                return strs[0][:longestIndex]
            if i == len(strs)-1:
                print("reset")
                longestIndex += 1
                i = -1
            i += 1

        return strs[0][:longestIndex]