class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix) * len(matrix[0]) -1
        
        while l<=r :
            mid = (l+r)//2


            row =  mid//len(matrix)
            col = mid%len(matrix)

            if matrix[row][col] == target :
                return True
            elif target < matrix[row][col] :
                r = mid-1
            else :
                l = mid+1
        
        return False