class Solution:
    def calPoints(self, operations: List[str]) -> int:
        for i,val in enumerate(operations):
            if val == "C": 
                operations.pop(i)
                operations.pop(i-1)
                i -= 2
        print(operations)
        ret = 0 
        if len(operations) <=0 : return 0
        prev1, prev2 = operations[0], operations[1]

        for i,val in enumerate(operations):
            if val == "+":
                ret += prev1 + prev2
                prev1, prev2 = prev2, prev1 + prev2
            elif val == "D":
                ret += prev2 * 2
                prev1 = prev2
                prev2 = prev2 * 2
            else:
                ret += int(val)
                prev1 = prev2
                prev2 = int(val)
            
                
            
        return ret
