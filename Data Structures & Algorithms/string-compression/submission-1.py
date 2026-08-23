class Solution:
    def compress(self, chars: List[str]) -> int:
        startingChar = chars[0]
        i = 0 #read index
        repeats = 0

        j = 0       #write index

        while i<len(chars):
            if chars[i] == startingChar:
                i += 1
                repeats += 1
            else:                           #char[i] is different
                if repeats > 1:
                    compressed = startingChar + str(repeats)
                    for k in range(len(compressed)):
                        chars[j] = compressed[k]
                        j+=1
                        print(j)
                else:
                    chars[j] = startingChar
                    j+= 1
                
                startingChar = chars[i]
                repeats = 1
                i += 1

        
        if repeats > 1:
            compressed = startingChar + str(repeats)
            for k in range(len(compressed)):
                chars[j] = compressed[k]
                j+=1
                print(j)
        else:
            chars[j] = startingChar
            j+= 1

        return j

            