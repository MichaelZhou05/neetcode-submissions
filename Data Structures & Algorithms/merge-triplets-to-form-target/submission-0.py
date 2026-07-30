class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        l1,l2,l3 = False, False, False

        t1,t2,t3 = target

        for ls in triplets: 
            if ls[0] == t1 and ls[1] <= t2 and ls[2] <= t3 :
                l1 = True
            if ls[0] <= t1 and ls[1] == t2 and ls[2] <= t3 :
                l2 = True
            if ls[0] <= t1 and ls[1] <= t2 and ls[2] == t3 :
                l3 = True
        

        return l1 and l2 and l3
