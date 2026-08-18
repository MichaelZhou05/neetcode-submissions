class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ret = []
        rightAstroids = []
		
        for val in asteroids:
            if val > 0:
                rightAstroids.append(val)
            else:
                while rightAstroids and abs(val)>rightAstroids[-1]:
                    rightAstroids.pop()
                if not rightAstroids:
                    ret.append(val)
                elif rightAstroids[-1] == abs(val):
                    rightAstroids.pop()
        
        return ret + rightAstroids
