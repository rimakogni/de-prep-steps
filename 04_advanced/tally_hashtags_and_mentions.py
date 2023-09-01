"""
This function receives a `tweet` that will contain a number of mentions and hashtags as on Twitter, sorry 'X'. 
A hashtag is marked by `#` and a mention is marked by `@`.

The function should return a dictionary describing the number of hashtags and mentions found in the string:
Example:
tweet = "So excited to start at @northcoders on Monday! #learntocode #codingbootcamp"
tally_hashtags_and_mentions(tweet) # returns {'hashtags': 2, 'mentions': 1}
"""

def tally_hashtags_and_mentions(tweet):
    # Your code here
    pass


def test_empty_tweet():
    assert tally_hashtags_and_mentions('') == {'hashtags': 0, 'mentions': 0}


def test_single_hashtag():
    assert tally_hashtags_and_mentions('#omg') == {'hashtags': 1, 'mentions': 0}


def test_single_mention():
    assert tally_hashtags_and_mentions('@paul_c') == {'hashtags': 0, 'mentions': 1}


def test_tweet_containing_single_hashtag():
    tweet = 'Best place to learn #python?'
    assert tally_hashtags_and_mentions(tweet) == {'hashtags': 1, 'mentions': 0}


def test_tweet_containing_single_mention():
    tweet = 'Need coding help, paging @Danika ...'
    assert tally_hashtags_and_mentions(tweet) == {'hashtags': 0, 'mentions': 1}


def test_tweet_containing_several_hashtags_and_mentions():
    tweet1 = 'So excited to start at @northcoders on Monday! #learntocode #codingbootcamp'
    assert tally_hashtags_and_mentions(tweet1) == {'hashtags': 2, 'mentions': 1}
    tweet2 = 'Thanks to @Alex and @Cat for helping with my #python #coding'
    assert tally_hashtags_and_mentions(tweet2) == {'hashtags': 2, 'mentions': 2} 