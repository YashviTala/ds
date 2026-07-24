import pandas as pd
df=pd.read_csv("D:\stud.csv")
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

print(df.sort_values(by='marks'))

print(df.sort_values(by='marks', ascending=False))

print(df['marks'].max())

print(df['name'].count())

df['result']="pass"
print(df)

df.to_csv("stud.csv",index=False)
print("csv file saved successfully.")
