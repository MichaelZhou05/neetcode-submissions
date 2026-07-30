class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l= 0
        hm = defaultdict(int)
        longest = 0
        for r,n in enumerate(s) :
            hm[n] += 1
            length = r-l+1
            print(length)
            if (length) - max(hm.values()) <= k :
                print(hm)
                longest = max(longest, length)
                r +=1
            else: 
                while((r-l+1) - max(hm.values() ) > k):
                    hm[s[l]] -= 1
                    l+=1
        return longest
        