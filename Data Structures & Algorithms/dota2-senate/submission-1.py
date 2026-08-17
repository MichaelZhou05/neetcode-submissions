class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque([])
        D = deque([])
        for i,char in enumerate(senate):
            if char == 'R':
                R.append(i)
            else:
                D.append(i)
        
        n=len(senate)
        while R and D:
            ri,di = R.popleft(), D.popleft()
            if ri<di:
                R.append(ri+n)
            else:
                D.append(di+n)
        
        return "Radiant" if R else "Dire"



