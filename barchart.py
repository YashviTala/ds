import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"Documents\sales_data.csv")
plt.bar(df["month"],df["sales"],color="green")
plt.title("monthly sales")
plt.xlabel("month")
plt.ylabel("sales")
plt.show()