class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ret = []

        mp1 = Counter(s)
        print(mp1)

        s1 = set()

        counter = 0
        for char in s : 
            counter += 1
            s1.add(char)

            if mp1[char] == 1 :
                s1.remove(char)
                if not s1 :
                    ret.append(counter)
                    counter = 0
            else :
                mp1[char] -= 1
            
        return ret