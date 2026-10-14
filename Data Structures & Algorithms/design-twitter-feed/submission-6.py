import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        if not userId in self.users:
            self.users[userId] = {}
            self.users[userId]['tweets'] = {}
            self.users[userId]['times'] = []

        tweets = self.users[userId]['tweets']
        times = self.users[userId]['times']
        
        times.append(self.time)

        if(len(times) > 10):
            times.pop(0)
        tweets[self.time] = tweetId

    def getNewsFeed(self, userId: int) -> List[int]:
        if not userId in self.users:
            self.users[userId] = {}
            self.users[userId]['tweets'] = {}
            self.users[userId]['times'] = []

        heap = []

        tweets = {} #time, tweetId

        heapq.heapify(heap)

        times = self.users[userId]['times']
        ftweets = self.users[userId]['tweets']

        for t in times:
            tweets[t] = ftweets[t]
            t *= -1
            heapq.heappush(heap, t)

        if 'followed' in self.users[userId]:
            for f in self.users[userId]['followed']:
                times = self.users[f]['times']
                ftweets = self.users[f]['tweets']

                for t in times:
                    tweets[t] = ftweets[t]
                    t *= -1
                    heapq.heappush(heap, t)

        news = []
        for _ in range(10):
            if(len(heap) != 0):
                time = heapq.heappop(heap)
                time *= -1
                news.append(tweets[time])
        return news


    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.users:
            self.users[followerId] = {}
            self.users[followerId]['tweets'] = {}
            self.users[followerId]['times'] = []

        if not 'followed' in self.users[followerId]:
            self.users[followerId]['followed'] = {}
        self.users[followerId]['followed'][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.users:
            self.users[followerId] = {}
            self.users[followerId]['tweets'] = {}
            self.users[followerId]['times'] = []
        elif not 'followed' in self.users[followerId]:
            self.users[followerId]['followed'] = {}
        elif followeeId in self.users[followerId]['followed']:
            self.users[followerId]['followed'].pop(followeeId)




