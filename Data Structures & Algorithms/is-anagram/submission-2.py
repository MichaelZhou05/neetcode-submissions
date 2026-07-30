class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)) :
            return False
        s = list(s)
        t = list(t)
        hs = set(s)
        ht = set(t)
        print(hs)
        print(ht)
        bs = len(hs)
        bt = len(ht)
        hs.update(t)
        ht.update(s)
        return bs==len(hs) & bt == len(ht)