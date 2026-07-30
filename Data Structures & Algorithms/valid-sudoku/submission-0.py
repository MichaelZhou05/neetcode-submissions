class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashRow = set()
        hashCol = set()
        hashSq = defaultdict(set)
        numSq = defaultdict(list)

        for rows in range(9) :
            nums = board[rows].copy()
            while "." in nums : nums.remove(".")
            if len(nums) != len(set(nums)) :
                print("row wrong")
                return False 
        
        for cols in range(9) :
            hashCol.clear()
            nums = []
            for rows in range(9) :
                val = board[rows][cols]
                if val != "." :
                    hashCol.add(val) 
                    nums.append(val)
            if len(nums) != len(hashCol) :
                print("col wrong")
                return False 
                

        for rows in range(9) :
            for cols in range(9) :
                val = board[rows][cols]
                if val != "." :
                    hashSq[(rows//3,cols//3)].add(val)
                    numSq[(rows//3, cols//3)].append(val)

        for rows in range(3) :
            for cols in range(3) :
                if len(hashSq[(rows,cols)]) != len(numSq[(rows,cols)]) : return False

        return True

