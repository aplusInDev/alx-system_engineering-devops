import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Recursive function that queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get('data')
    after = data.get('after')
    children = data.get('children')
    for child in children:
        title = child.get('data').get('title').lower()
        for word in word_list:
            if word.lower() in title:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f'{word}: {count}')
