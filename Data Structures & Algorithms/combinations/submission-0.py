class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        #[1,2,3,4,5,6...n]
        # ^ ^ ^    
        ret = []
        def backtrack(arr,i,k):
            if len(arr) == k:
                nonlocal ret
                ret.append(arr)
                return
            
            nonlocal n
            if i > n:
                return
            
            
            backtrack(arr+[i],i+1,k)
            backtrack(arr,i+1,k)
        
        backtrack([],1,k)
        return ret