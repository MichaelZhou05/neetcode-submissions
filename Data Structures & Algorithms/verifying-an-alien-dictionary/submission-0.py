class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {char:i+1 for i,char in enumerate(order)}

        wordNum = []
        maxLength = max(len(word) for word in words)

        for i in range(1,len(words)):
            minLength = min(len(words[i]),len(words[i-1]))
            j=0
            while j < minLength:
                char1,char2 = words[i-1][j], words[i][j]
                if orderMap[char1] < orderMap[char2]:
                    break
                elif orderMap[char1] == orderMap[char2]:
                    j+= 1
                else:
                    return False
                if j == minLength-1 and len(words[i-1]) > len(words[i]): return False    
        

        return True


        