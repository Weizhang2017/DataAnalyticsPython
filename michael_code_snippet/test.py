import numpy as np
import pandas as pd 

extra2 = pd.read_csv('Extra Material 2 - keyword list_with substring.csv')
extra3 = pd.read_csv('Extra Material 3 - mismatch list.csv') 
keywords = pd.read_csv('Keyword_spam_question.csv') 

extra2['aslist'] = extra2.Keywords.apply(lambda st : st.split(', ')) 

def find_group_id(st = ""): 
    result = []
    for index_id, list_of_items in extra2['aslist'].items() : 
        found = [ kk for kk in list_of_items if kk in st.lower() ]
        if len(found) > 0: 
            result.append(index_id)
    
    return result


keywords.name.apply(find_group_id)

