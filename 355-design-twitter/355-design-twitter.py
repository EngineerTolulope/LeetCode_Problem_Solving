class Twitter:

    def __init__(self):
        self.time = 0
        self.user_followers = defaultdict(set)  # user id : set of followers
        self.user_tweets = defaultdict(list)    # user id : list of tweets

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result, min_heap = [], []
        self.user_followers[userId].add(userId)
        
        for followee_id in self.user_followers[userId]:
            if followee_id in self.user_tweets:
                end_index = len(self.user_tweets[followee_id]) - 1
                time, tweet_id = self.user_tweets[followee_id][end_index]
                min_heap.append((time, tweet_id, followee_id, end_index - 1))
        
        heapq.heapify(min_heap)
        while min_heap and len(result) < 10:
            time, tweet_id, followee_id, end_index = heapq.heappop(min_heap)
            result.append(tweet_id)
            if end_index >= 0:
                time, tweet_id = self.user_tweets[followee_id][end_index]
                heapq.heappush(min_heap, (time, tweet_id, followee_id, end_index - 1))
        return result
                
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_followers[followerId]:
            self.user_followers[followerId].remove(followeeId)       


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)