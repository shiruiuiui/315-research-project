def extract_hashtags(post):
    """
    Given a tweet return a list of hashtags in the tweet.
    """
    words = post.lower().split() # creates a list of words
    hashtags = [w for w in words if w[0] == '#']
    return hashtags