class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        visited = {}
        
        def search(i,j) -> bool:
            if i >= len(s) and j >= len(p) :
                return True
        
            if (i,j) in visited:
                return visited[(i,j)]
            
            if j >= len(p):
                visited[(i,j)] = False
                return False
            
            if i >= len(s):
                if j+1 < len(p) and p[j+1] == '*':
                    return search(i,j+2)
                else:
                    return False
            
            if j+1 < len(p) and p[j+1] == '*':
                use = search(i,j+2)
                notUse = None
                if p[j] == s[i] or p[j] == '.':
                    notUse = search(i+1,j)
                visited[(i,j)] = use or notUse
                return visited[(i,j)]
            
            else:
                if p[j] == '.':
                    return search(i+1,j+1)
                elif p[j] != s[i]:
                    visited[(i,j)] = False
                    return False
                else:
                    return search(i+1,j+1)
            
        return search(0,0)

                
            
            




        #    v
        # xyzz
        # .*z
        #  ^
        # t



        #   x y z
        # .
        # *
        # z
    
        # nnn
        # n*


        # we use "*" >1 times when len(p) < len(s)

        #solve case of dot
            # can by anything auto passs
        #solve case of star
            # can be p char before
            # can use "*" again ONLY IF len(p) < len(s)
            # or the next char in p

        #