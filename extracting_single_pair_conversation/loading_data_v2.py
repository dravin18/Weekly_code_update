import pandas as pd
import math

df = pd.read_csv('twcs.csv')
df_single_pair_conversations = df
df_single_pair_conversations = df_single_pair_conversations.iloc[0:0]
single_pair_conversations_list = []
single_pair_conversations_reply_store = None
single_pair_conversation_2nd_tweet_finder_toggle = False
single_pair_conversation_reply_tweet_id = 0
for index,row in df.iterrows():
    if single_pair_conversation_2nd_tweet_finder_toggle and single_pair_conversation_reply_tweet_id == row['tweet_id']:
        if math.isnan(row['in_response_to_tweet_id']) == True:
            if isinstance(row['response_tweet_id'],str):
                search_index = row['response_tweet_id'].strip().split(',')
                if len(search_index) == 1:
                    single_pair_conversations_list.append(single_pair_conversations_reply_store)
                    single_pair_conversations_list.append(row)
                    df_extracted_single_pair_conversations = pd.DataFrame(single_pair_conversations_list,columns=df.columns)
                    df_single_pair_conversations = pd.concat([df_single_pair_conversations,df_extracted_single_pair_conversations])
                    df_single_pair_conversations.to_csv('extracted_conversations_from_v2_script.csv',mode = 'w+')
                    single_pair_conversation_2nd_tweet_finder_toggle = False
                    single_pair_conversations_list = []
                    continue
                else:
                    single_pair_conversation_2nd_tweet_finder_toggle = False
                    continue
            else:
                single_pair_conversation_2nd_tweet_finder_toggle = False
                continue
        else:
            single_pair_conversation_2nd_tweet_finder_toggle = False
            continue
    if isinstance(row['response_tweet_id'],str) == False & math.isnan(row['in_response_to_tweet_id']) == False:
        single_pair_conversation_reply_tweet_id = int(row['in_response_to_tweet_id'])
        single_pair_conversations_reply_store = row
        row['in_response_to_tweet_id']
        single_pair_conversation_2nd_tweet_finder_toggle = True
        continue
    else:
        continue