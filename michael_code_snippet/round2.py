import numpy as np
import pandas as pd 

# read files
bank = pd.read_csv('bank_accounts.csv') 
credit = pd.read_csv('credit_cards.csv') 
devices = pd.read_csv('devices.csv') 
orders = pd.read_csv('orders.csv') 

#order_join = pd.DataFrame.merge(orders, bank, left_on='buyer_userid', right_on='userid', how='outer', suffixes=('', '_buyer'))
#orders = orders.iloc[:1000]

# left join with devices
df_device_joint_buyer = pd.merge(left=orders, right=devices, how='left', left_on='buyer_userid', right_on='userid')
df_device_joint_buyer.rename(columns={'device': 'buyer_device'}, inplace=True)
df_device_joint = pd.merge(left=df_device_joint_buyer, right=devices, how='left', left_on='seller_userid', right_on='userid')
df_device_joint.rename(columns={'device': 'seller_device'}, inplace=True)

# detect fraud over direct link with devices
def same_device(row): 
    if row['is_fraud'] == 'not fraud': 
        if row['buyer_device'] == row['seller_device']: 
            return str(row['buyer_userid']) + "-device:" + row['buyer_device'] + "->" + str(row['seller_userid'])
        else:
            return row['is_fraud']  
    else:
        return row['is_fraud']  

df_device_joint['is_fraud'] = 'not fraud'
df_device_joint['is_fraud']  = df_device_joint.apply(same_device, axis=1)

# merge different orderid's back into one
def get_single_order(group): 
    b = group.is_fraud.unique() 
    if len(b) == 1 :
        return b[0]
    else: 
        return b[b != 'not fraud'][0]

result = df_device_joint.groupby('orderid').apply(get_single_order)
result.name = 'is_fraud'
pd.DataFrame(result).to_csv('solution_round2_secondSubmission.csv') 
