class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[x] - cost[x] for x in range(len(gas))]
        
        if sum(diff) < 0: return -1

        currSum = 0
        start = 0
        i = 0
        while i < len(diff):
            currSum += diff[i]
            if currSum < 0 :
                currSum = 0
                start = i + 1
            i += 1
        
        return start
            
            
            