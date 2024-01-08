import pandas as pd

df = pd.read_csv('../data/uci_news_aggregator.csv')

def data_clean(self):
    print('Data Pre')

x = df['CATEGORY']
y = df['TITLE']
n = x.isnull().sum()
f = x.dropna(inplace=True)
dy = y.duplicated().sum()

print(y.sum())
print(dy)

