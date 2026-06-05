import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Name": ["A", "B", "C", "D"],
    "Score": [85, 90, 78, 92],
    "Age": [20, 21, 19, 22]
}

df = pd.DataFrame(data)
print(df.head())
print(df.describe())

scores = np.array(df["Score"])
print(np.mean(scores))
print(np.std(scores))

sns.histplot(df["Score"], kde=True)
plt.show()

sns.scatterplot(x="Age", y="Score", data=df)
plt.show()
