import pandas as pd


data = pd.read_csv('programm.csv')
print(data)
print(data.sort_values(by='name', ascending=True))
# print(data)
