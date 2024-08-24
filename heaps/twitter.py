import heapq


class Twitter:  # LeetCode Q.355.
    def __init__(self):
        self.followers_table = dict()
        self.tweets_table = dict()
        self.tweet_order = 1

    def post_tweet(self, user_id: int, tweet_id: int):
        if user_id not in self.tweets_table.keys():
            self.tweets_table.update({user_id: []})

        # Tweet format: (order, ID).
        self.tweets_table[user_id].append((self.tweet_order, tweet_id))
        self.tweet_order += 1  # Increment for next tweet.

    def get_news_feed(self, user_id: int):
        tweets_lists = []
        if user_id in self.followers_table.keys():
            for followee_id in self.followers_table[user_id]:
                if followee_id in self.tweets_table.keys():
                    tweets_lists.append(self.tweets_table[followee_id])

        if user_id in self.tweets_table.keys():
            tweets_lists.append(self.tweets_table[user_id])

        min_heap = []  # Keep track of smallest tweets across all tweets lists.
        for list_idx, tweets_list in enumerate(tweets_lists):
            if tweets_list:  # Initialize heap of each non-empty list's 1st tweet.
                # Tuple: (tweet tuple, list's idx, tweet's idx in list).
                heapq.heappush(min_heap, (tweets_list[0], list_idx, 0))

        sorted_tweets = []
        while min_heap:
            tweet, list_idx, tweet_idx = heapq.heappop(min_heap)  # Currently smallest.
            sorted_tweets.append(tweet)

            if tweet_idx < len(tweets_lists[list_idx]) - 1:
                # Current tweet's right side neighbor exists.
                next_tweet = tweets_lists[list_idx][tweet_idx + 1]
                heapq.heappush(min_heap, (next_tweet, list_idx, tweet_idx + 1))

        # Reverse list to select top 10 latest. Only need to return IDs.
        return [tweet_id for _, tweet_id in sorted_tweets[::-1][:10]]

    def follow(self, follower_id: int, followee_id: int):
        if follower_id not in self.followers_table.keys():
            self.followers_table.update({follower_id: set()})
        self.followers_table[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int):
        if follower_id in self.followers_table.keys():
            self.followers_table[follower_id].discard(followee_id)
