class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsMap = defaultdict(list) #count tuple -> list of words

        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord('a')] += 1
            
            anagramsMap[tuple(count)].append(word)
        
        ret = []

        for arr in anagramsMap.values():
            ret.append(arr)
        
        return ret
