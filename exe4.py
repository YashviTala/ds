import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"Documents\sales_data.csv")
plt.plot(df["month"],df["sales"],marker='o')
plt.title("monthly sales")
plt.xlabel("month")
plt.ylabel("sales")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"Documents\sales_data.csv")
plt.bar(df["month"],df["sales"])
plt.title("monthly sales")
plt.xlabel("month")
plt.ylabel("sales")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"Documents\sales_data.csv")
plt.pie(df["sales"],labels=df["month"],autopct='%1.1f%%')
plt.title("monthly sales distribution")
plt.xlabel("month")
plt.ylabel("sales")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"Documents\sales_data.csv")
plt.plot(df["month"],df["sales"])
plt.title("monthly sales scatter plot")
plt.xlabel("month")
plt.ylabel("sales")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"Documents\sales_data.csv")
plt.hist(df["sales"],bins=5)
plt.title("sales histogram")
plt.xlabel("sales")
plt.ylabel("frequency")
plt.show()