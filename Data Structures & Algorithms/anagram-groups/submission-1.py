class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {} #char count array -> index array 
        ret = []

        for i, str1 in enumerate(strs) :
            count = [0] *26
            for c in range(len(str1)) :
                count[ord(str1[c]) - ord('a')] += 1

            if tuple(count) in hm :
                hm.get(tuple(count)).append(i)
            else:
                hm[tuple(count)] = [i]
       
        for n in hm :
            val = []
            for j in hm.get(n) :
                val.append(strs[j])
            ret.append(val)
        
        return ret