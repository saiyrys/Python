import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

one_hot_data = pd.get_dummies(data['whoAmI'], prefix='whoAmI')
data = pd.concat([data, one_hot_data], axis=1)
data = data.drop('whoAmI', axis=1)

data.head()