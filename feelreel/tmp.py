import json
import os
import pprint
from collections import defaultdict

import praw
import requests
import pandas as pd

from reddit_download_and_analyze import *


def process_charlies_data(which_subreddit_idx):
    comments_from_charlie = pd.read_csv('data/SQL_files/combined_cleaned.csv')
    subreddit = comments_from_charlie['subreddit'].unique()

    s_dct = defaultdict(dict)
    print(subreddit)

    for s_idx, s in enumerate(subreddit):
        print(s_idx, which_subreddit_idx)
        if s_idx != which_subreddit_idx:
            continue
        os.makedirs(f'data/SQL_files/{s}', exist_ok=True)
        subreddit_subset = comments_from_charlie[comments_from_charlie['subreddit'] == s]

        c_dct = defaultdict(dict)
        urls = subreddit_subset['Images'].unique()
        for idx, c in enumerate(urls):

            post_subset = subreddit_subset[subreddit_subset['Images'] == c]

            c_dct[s]['title'] = post_subset['SubmissionTitle'].unique()[0]
            c_dct[s]['url'] = post_subset['Images'].unique()[0]

            c_dct[s]['comments'] = []
            for _, row in post_subset.iterrows():
                # Get the submission object using the URL
                try:
                    # cleaned_comment = clean_text(row['Comment'])
                    word_freq = get_cap_analysis_from_comment(row['Comment'])
                except Exception as e:
                    print(e)
                    cleaned_comment = ''
                    word_freq = {}

                c_dct[s]['comments'].append(
                    {
                        "body": row['Comment'],
                        'analysis': word_freq
                    })

            data = {
                'title': c,
                'url': c_dct[s]['url'],
                'comments': c_dct[s]['comments']
            }

            pprint.pprint(data)
            filename = f'{idx}.json'
            imgname = f'{idx}.png'
            os.makedirs(f'data/saved_subreddits/{s}/jsons', exist_ok=True)
            os.makedirs(f'data/saved_subreddits/{s}/images', exist_ok=True)
            filepath = os.path.join(f'data/saved_subreddits/{s}/jsons', filename)
            imgpath = os.path.join(f'data/saved_subreddits/{s}/images', imgname)

            if os.path.exists(filepath):
                print(f'{filepath} already exists!')
            else:
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
                    print(f'Saved {filepath}!')
            response = requests.get(c_dct[s]['url'])
            if os.path.exists(imgpath):
                print(f'{imgpath} already exists!')
            else:
                with open(imgpath, 'wb') as f:
                    f.write(response.content)
                    print(f'Saved {imgpath}!')

        s_dct[s] = c_dct
    pprint.pprint(s_dct)


def find_subredditnames():
    filepath = 'valid_image_submission_table_added_subredditnames.csv'
    submission_df = pd.read_csv('data/SQL_files/valid_image_submission_table.csv')
    # comments = pd.read_csv('data/SQL_files/valid_image_cleaned_comments_table.csv')
    submission_df = submission_df[submission_df['SubmissionID'] > 5699]

    reddit = praw.Reddit(client_id='xRyVhJbhZudd0OPXZWEjEA',
                         client_secret='oxCHHsu0YeyXuasW2gL30QUWWRy17Q',
                         username='Datacollector002',
                         password='datacollector02',
                         user_agent=user_agent)


    if os.path.exists(f'data/SQL_files/{filepath}'):
        print(f'{filepath} already exists!')
        valid_submission_df = pd.read_csv(f'data/SQL_files/{filepath}')
        subreddit_names = valid_submission_df['SubredditName'].values.tolist()
    else:
        valid_submission_df = pd.DataFrame(
            columns=['SubmissionID', 'SubmissionTitle', 'Images', 'SubmissionRetrieveTime',
                     'SubmissionCreatTime'])
        subreddit_names = []

    for idx, row in submission_df.iterrows():
        if row['Images'] in valid_submission_df['Images'].values:
            continue
        # Search for the image URL on Reddit
        search_results = reddit.subreddit('all').search(f'url:{row["Images"]}')
        # Add a delay of 2 seconds between requests
        time.sleep(2)
        # Loop through the search results and print the subreddit name(s)
        subreddits = []
        for submission in search_results:
            if submission.subreddit.display_name not in subreddits:
                subreddits.append(submission.subreddit.display_name)

        if len(subreddits) > 0:
            print(f'The image {row["Images"]} was posted in the following subreddit(s): {", ".join(subreddits)}')
            # Add a new row
            new_row = submission_df[submission_df['Images'] == row['Images']].iloc[0]
            valid_submission_df = valid_submission_df.append(pd.Series(new_row, index=submission_df.columns),
                                                             ignore_index=True)
            subreddit_names.append(", ".join(subreddits))
        else:
            print(f'The image {row["Images"]} could not be found on Reddit.')

        valid_submission_df['SubredditName'] = subreddit_names
        print(valid_submission_df)
        valid_submission_df.to_csv(f'data/SQL_files/{filepath}', index=False)
        print(f'Saved {filepath}! to data/SQL_files/')




if __name__ == '__main__':
    # process_charlies_data(which_subreddit_idx=20)
    find_subredditnames()
