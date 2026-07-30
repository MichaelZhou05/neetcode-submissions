class Twitter:

    def __init__(self):
        self.fList = defaultdict(list) # id -> [id,id,id]
        self.posts = defaultdict(list)
        self.time = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.time, tweetId])
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        ls1 = self.posts[userId]
        copy = ls1.copy()
        for i in self.fList[userId] :
            copy.extend(self.posts[i])
        
        heapq.heapify(copy)
        max10 = heapq.nlargest(min(len(copy),10), copy)
        return [x[1] for x in max10]

             


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId not in self.fList[followerId] :
            self.fList[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        print(self.fList[followerId])
        if followeeId in self.fList[followerId] :
            self.fList[followerId].remove(followeeId)
        print(self.fList[followerId])
        
