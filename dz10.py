import pandas as pd



# Исходный код

import random

lst = ['robot'] * 10

lst += ['human'] * 10

random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

print("Исходный DataFrame:")

print(data.head())



# One hot

one_hot_data = pd.get_dummies(data['whoAmI'])

data_one_hot = pd.concat([data, one_hot_data], axis=1)

data_one_hot = data_one_hot.drop('whoAmI', axis=1)



print("\nDataFrame после one hot encoding:")

print(data_one_hot.head())