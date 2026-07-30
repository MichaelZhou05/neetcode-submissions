class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str1 in strs:
            res += str(len(str1)) + str1
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s) :
            length = int(s[i])
            res.append(s[i+1 : i + 1 + length])
            i = i + 1 + length
        
        return res
