import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
data_path = '../data/bank/bank.csv'
df = pd.read_csv(data_path)

# Explorar datos
print(df.head())
print(df.describe())

# Visualizar datos
sns.histplot(df['job'])
plt.show()