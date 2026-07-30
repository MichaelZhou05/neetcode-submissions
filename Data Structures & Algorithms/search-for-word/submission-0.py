class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r,c,word):
            if not len(word):
                return True
            if r<len(board) and c < len(board[0]) and board[r][c] == word[0]:
                newWord = word[1:]
                return dfs(r,c+1, newWord) or dfs(r+1,c, newWord) or dfs(r,c-1, newWord) or dfs(r-1,c, newWord)
            
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i,j,word) :
                    return True
        
        return False
                