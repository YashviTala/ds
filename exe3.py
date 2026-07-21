import pandas as pd
df=pd.read_csv("stud.csv")
print(df)

print(df.head())

print(df.tail())

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.info())

print(df.describe())

print(df[df['marks']>20])

print(df[df['city']=="surat"])

print(df.sort_values(by='marks',ascending=false))

