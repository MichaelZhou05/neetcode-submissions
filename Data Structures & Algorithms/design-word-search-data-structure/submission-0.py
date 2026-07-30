class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for x in word :
            index = ord(x)-ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr=curr.children[index]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root

        def helper(root, word):
            curr = root

            for x in word :
                if x == '.' :
                    newWord = word[word.index('.')+1:]
                    for i in range(25) :
                        if curr.children[i] and helper(curr.children[i], newWord) :
                            return True
                    return False
                else: 
                    index = ord(x)-ord('a')
                    if not curr.children[index]:
                        return False
                    curr = curr.children[index]
            return curr.endOfWord

        for x in word :
            if x == '.' :
                newWord = word[word.index('.')+1:]
                for i in range(25) :
                    if curr.children[i] and helper(curr.children[i], newWord) :
                        return True
                return False
            else: 
                index = ord(x)-ord('a')
                if not curr.children[index]:
                    return False
                curr = curr.children[index]
        return curr.endOfWord


       
                        
        
