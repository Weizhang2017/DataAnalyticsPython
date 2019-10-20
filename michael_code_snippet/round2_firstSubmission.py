import numpy as np
import pandas as pd 

bank = pd.read_csv('bank_accounts.csv') 
credit = pd.read_csv('credit_cards.csv') 
devices = pd.read_csv('devices.csv') 
orders = pd.read_csv('orders.csv') 

df_output = orders.copy()
df_output.drop(columns=['buyer_userid', 'seller_userid'], inplace=True)
df_output['is_fraud'] = 'not fraud'

df_output.set_index('orderid').rename(columns={'name': 'is_fraud'}).to_csv('solution_round2_firstSubmission.csv')
