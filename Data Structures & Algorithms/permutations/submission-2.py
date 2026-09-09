class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for num in nums: 
            newPermutations = []
            for arr in permutations:
                for i in range(len(arr)):
                    newPermutations.append(arr[:i]+[num]+arr[i:])
                newPermutations.append(arr + [num])
            
            permutations = newPermutations
        
        return permutations



            

