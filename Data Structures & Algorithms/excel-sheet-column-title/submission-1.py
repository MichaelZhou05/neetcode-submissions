class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 3--> * 10 + 1

        # A = 1--> * 26
        # AZ = 1*26 + 26  = 2*26 =  52
        # BA = 2*26 + 1
        ret = []
        letters = [chr(ord('@') + i) for i in range(26)]
        letters[0] = 'Z'
        while columnNumber:
            print(columnNumber )
            ret.append(letters[columnNumber%26])
            if columnNumber > 26:
                columnNumber = columnNumber //26
            else: 
                columnNumber = 0
        ret.reverse()
        print(ret)
        return "".join(ret)