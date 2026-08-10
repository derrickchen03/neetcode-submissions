import heapq
class User:
    
    def __init__(self, userId):
        self.userId = userId
        self.following = set()
        self.tweets = []

class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)
            self.users[userId].tweets.append((self.time, userId, tweetId))
        else:
            self.users[userId].tweets.append((self.time, userId, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []

        toCheck = self.users[userId].following | {userId}

        for uid in toCheck:
            for time, _, tweet in self.users[uid].tweets:
                heapq.heappush(heap, (time, tweet))
                if len(heap) > 10:
                    heapq.heappop(heap)
            
        while heap:
            _, tweet = heapq.heappop(heap)
            feed.append(tweet)
        
        return feed[::-1]


        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[userId] = User(userId)
        if followeeId not in self.users[followerId].following:
            return
        else:
            self.users[followerId].following.remove(followeeId)
