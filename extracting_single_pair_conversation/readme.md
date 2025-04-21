Since, a chatbot is not being built i.e. the LLM chain is designed to take one input and provide an output, since the output needs to be compared to determine the accuracy of the model, a code is being written to extract conversation having only a single pair of exchanges. The first one will be from the user and the second one will be from the customer service.

Approach one: use loops to manually check through the code, it is very slow. the logic is that for every tweet that is the start of a conversation. This is done by identifying if the 'in_response_to_tweet' column is empty, the system loops through the dataframe to identify if that tweet has a response tweet which is the final tweet in the conversation which is done by identifying if the 'response_to_tweet' column is empty.

The 'response_tweet_id' consists of float for nan and str for the remaining datatypes.

The 'in_response_to_tweet_id' consists of float for both nan and other numbers.