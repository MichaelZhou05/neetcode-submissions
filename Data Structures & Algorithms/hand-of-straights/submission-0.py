class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        mp1 = defaultdict(int)

        for x in hand: 
            mp1[x] += 1


        while mp1:
            x = min(mp1)
            for i in range(groupSize):
                if x+i not in mp1:
                    return False
                if mp1[x+i] == 1 :
                    del mp1[x+i]
                else :
                    mp1[x+i] -= 1
                
        
        return True
        