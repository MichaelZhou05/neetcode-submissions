class CountSquares:


    # x set(1,2,4,5)
    # 

    def __init__(self):
        self.points = defaultdict(int) #[px,py] -> num of overlap
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = self.points[tuple(point)]+1
        

    def count(self, point: List[int]) -> int:
        ret = 0
        Qx,Qy = point 
        for px,py in self.points.keys():
            if Qx == px or Qy == py or abs(Qx-px) != abs(Qy-py):
                continue
            ret += self.points.get((px,py),0) * self.points.get((Qx,py),0) * self.points.get((px,Qy),0)

        return ret
 
