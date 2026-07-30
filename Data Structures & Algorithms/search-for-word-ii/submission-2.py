import copy
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            index = ord(i) - ord('a')
            if curr.children[index] == None :
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for i in word: 
            index = ord(i) - ord('a')
            if not curr.children[index] :
                return False
            curr = curr.children[index]
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix: 
            index = ord(i) - ord('a')
            if not curr.children[index] :
                return False
            curr = curr.children[index]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ret = []
        preTree = PrefixTree()
        for x in words: 
            preTree.insert(x)
        

        def dfs(r,c, str1) :
            if r<0 or c<0 or r >= len(board) or c >= len(board[0]) or cpy[r][c] == '#':
                return

            str1 += (cpy[r][c])
            if preTree.startsWith(str1) :
                val = cpy[r][c]
                cpy[r][c] = '#'
                if preTree.search(str1) and str1 not in ret:
                    ret.append(str1)
                dfs(r+1, c, str1)
                dfs(r,c+1, str1)
                dfs(r-1, c, str1)
                dfs(r, c-1, str1)
                cpy[r][c] = val
            else:
                return
            

        for n,i in enumerate(board) :
            for m in range(len(i)) :
                cpy = copy.deepcopy(board)
                dfs(n,m,"")
        return ret

        

