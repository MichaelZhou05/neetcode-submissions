class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []

        if not len(digits):
            return []


        def dfs(index, str1):
            if index >= len(digits):
                ret.append(str1)
                return
            
            num = int(digits[index])
            print("num = " + str(num))

            match num: 
                case 2 | 3 | 4 | 5 | 6 :
                    ascii = ord('a') + (num-2) * 3
                    for i in range(3):
                        newChar = chr(ascii + i)
                        print(newChar)
                        dfs(index +1, str1 + newChar)
                
                case 7:
                    ascii = ord('p')
                    for i in range(4) :
                        newChar = chr(ascii + i)
                        print(newChar)
                        dfs(index +1, str1 + newChar)
                case 8: 
                    ascii = ord('t')
                    for i in range(3) :
                        newChar = chr(ascii + i)
                        print(newChar)
                        dfs(index +1, str1 + newChar)
                
                case 9:
                    ascii = ord('w')
                    for i in range(4) :
                        newChar = chr(ascii + i)
                        print(newChar)
                        dfs(index +1, str1 + newChar)
        dfs(0, "")
        return ret
            
