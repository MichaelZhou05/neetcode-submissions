class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 3--> * 10 + 1

        # A = 1--> * 26
        # AZ = 1*26 + 26  = 2*26 =  52
        # BA = 2*26 + 1
        ret = []
        while columnNumber:
            char = ord('A')-1+(columnNumber % 26)
            if char < 0: ret.append('Z')
            else: ret.append(chr(char))
            columnNumber = columnNumber//26
        ret.reverse()
        return "".join(ret)