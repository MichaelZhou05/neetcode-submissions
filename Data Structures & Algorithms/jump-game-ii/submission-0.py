class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        que = []

        que.append([0,0])

        while que :
            index, jump = que.pop(0)
            length = nums[index]

            if index + length >= n-1 :
                return jump + 1
            
            for x in range(length,0,-1):
                que.append([index+x, jump+1])
        


            

