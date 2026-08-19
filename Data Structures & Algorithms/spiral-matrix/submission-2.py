class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        leftBound, rightBound = 0,len(matrix[0])-1
        topBound, botBound = 0,len(matrix)-1
        
        ret = []
        while  leftBound<=rightBound and topBound<=botBound:

            #full loop
            r,c = leftBound,topBound
            for c in range(leftBound,rightBound+1):
                ret.append(matrix[r][c])
            topBound += 1

            c = rightBound
            for r in range(topBound,botBound+1):
                ret.append(matrix[r][c])
            rightBound -=1
            
            if (leftBound > rightBound or topBound > botBound):
                break

            r = botBound
            for c in range(rightBound,leftBound-1,-1):
                ret.append(matrix[r][c])
            botBound -= 1
            

            c = leftBound
            for r in range(botBound,topBound-1,-1):
                ret.append(matrix[r][c])
            leftBound +=1
            
            

        return ret