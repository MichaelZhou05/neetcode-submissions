class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}  # character count array -> list of strings
        
        for s in strs:
            # Count occurrences of each character
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            # Convert count to tuple (to make it hashable)
            count_tuple = tuple(count)
            
            # Get existing list or create new one, then append current string
            if count_tuple in hm:
                hm[count_tuple].append(s)
            else:
                hm[count_tuple] = [s]
        
        # Return the groups
        return list(hm.values())