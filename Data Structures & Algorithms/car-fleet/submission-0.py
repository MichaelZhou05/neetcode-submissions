class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = defaultdict(int) #position -> index
        eta = [0] * len(position)
        for i in range(len(position)):
            pos[position[i]] = i
            
        for i in range(len(speed)) :
            eta[i] = (target-position[i])/speed[i]
        
        carFleets = 0
        etaStack = []

    
        for n in sorted(pos) :
            index = pos[n]


            while etaStack and eta[index] >= etaStack[-1] :
                etaStack.pop()

            etaStack.append(eta[index])
            
            
        return len(etaStack)