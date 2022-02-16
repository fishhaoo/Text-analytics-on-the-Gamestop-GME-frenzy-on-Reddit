import pandas as pd
from pmaw import PushshiftAPI
import datetime as dt
from datetime import datetime

'''
Reddit Scraping
'''
# part 1
api = PushshiftAPI()

before = int(dt.datetime(2021, 12, 1, 0, 0).timestamp())
after = int(dt.datetime(2020, 10, 1, 0, 0).timestamp())

subreddit="wallstreetbets"
limit=50000
comments = api.search_comments(subreddit=subreddit, limit=limit, before=before, after=after, q='(Gamestop)|(gamestop)|(Game stop)|(Game Stop)|(game stop)')
print(f'Retrieved {len(comments)} comments from Pushshift')

comments_df = pd.DataFrame(comments)

#part 2
before1 = int(dt.datetime(2021, 2, 1, 0, 0).timestamp())
after1 = int(dt.datetime(2020, 12, 1, 0, 0).timestamp())

subreddit="wallstreetbets"
limit=100000
comments = api.search_comments(subreddit=subreddit, limit=limit, before=before1, after=after1, q='(Gamestop)|(gamestop)|(Game stop)|(Game Stop)|(game stop)')
print(f'Retrieved {len(comments)} comments from Pushshift')

comments_df1 = pd.DataFrame(comments)


#part 3
before2 = int(dt.datetime(2021, 4, 1, 0, 0).timestamp())
after2 = int(dt.datetime(2021, 2, 1, 0, 0).timestamp())

subreddit="wallstreetbets"
limit=100000
comments = api.search_comments(subreddit=subreddit, limit=limit, before=before2, after=after2, q='(Gamestop)|(gamestop)|(Game stop)|(Game Stop)|(game stop)')
print(f'Retrieved {len(comments)} comments from Pushshift')

comments_df2 = pd.DataFrame(comments)

#part 4
before3 = int(dt.datetime(2021, 6, 1, 0, 0).timestamp())
after3 = int(dt.datetime(2021, 4, 1, 0, 0).timestamp())

subreddit="wallstreetbets"
limit=100000
comments = api.search_comments(subreddit=subreddit, limit=limit, before=before3, after=after3, q='(Gamestop)|(gamestop)|(Game stop)|(Game Stop)|(game stop)')
print(f'Retrieved {len(comments)} comments from Pushshift')

comments_df3 = pd.DataFrame(comments)

#part 5
before4 = int(dt.datetime(2021, 6, 1, 0, 0).timestamp())
after4 = int(dt.datetime(2021, 4, 1, 0, 0).timestamp())

subreddit="wallstreetbets"
limit=100000
comments = api.search_comments(subreddit=subreddit, limit=limit, before=before4, after=after4, q='(Gamestop)|(gamestop)|(Game stop)|(Game Stop)|(game stop)')
print(f'Retrieved {len(comments)} comments from Pushshift')

comments_df4 = pd.DataFrame(comments)

#part 6
before5 = int(dt.datetime(2021, 4, 1, 0, 0).timestamp())
after5 = int(dt.datetime(2021, 2, 1, 0, 0).timestamp())

subreddit="wallstreetbets"
limit=100000
comments = api.search_comments(subreddit=subreddit, limit=limit, before=before5, after=after5, q='(Gamestop)|(gamestop)|(Game stop)|(Game Stop)|(game stop)')
print(f'Retrieved {len(comments)} comments from Pushshift')

comments_df5 = pd.DataFrame(comments)


#combine 
master_stack = pd.concat([comments_df, comments_df1, comments_df2, comments_df3, comments_df4, comments_df5], axis=0)

master_stack.to_csv(r'D:\Program Files\Python\Capstone\master_dataset.csv')
