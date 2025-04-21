import pandas as pd
from logger_config import logger
import math

df = pd.read_csv('twcs.csv')
df_2 = df
df_2 = df_2.iloc[0:0]
for index,row in df.iterrows():
    if df_2.shape[0] > 10:
        break
    if row['inbound'] == False:
        continue
    if not math.isnan(row['in_response_to_tweet_id']):
        logger.info(f"this cell data type has been detected as a float {row['in_response_to_tweet_id']},type:{type(row['in_response_to_tweet_id'])}")
        continue
    else:
        logger.info(f"the twitter id being considered is: {row['tweet_id']}")
        if isinstance(row['response_tweet_id'],str):
            search_index = row['response_tweet_id'].strip().split(',') 
            if len(search_index) != 1:
                continue
        logger.info(f"the response twitter to be searched is: {search_index}")
        for index_2, row_2 in df.iterrows():
            if int(row_2['tweet_id']) <= (int(row['tweet_id']) - 2):
                continue
            if row_2['inbound'] == True:
                continue
            if row_2['tweet_id'] == int(search_index[0]):
                logger.info(f"the response tweet being considered is: {row_2}")
                if row['response_tweet_id'].isnull() == True:
                    df_2 = pd.concat([df_2,row],axis=1)
                    df_2 = pd.concat([df_2,row_2],axis=1)
                    df_2.to_csv('extracted_conversations.csv',mode='w+')