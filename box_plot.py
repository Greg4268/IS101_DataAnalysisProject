import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./country_dataset.csv")

plt.figure(figsize=(14,8))
sns.boxplot(x='Country', y='Life Expectancy (Years)', data=df)

mean = df['Life Expectancy (Years)'].mean()
plt.axhline(y=mean, color='r', linestyle='--', label=f'Overall Mean: {mean:.2f}')

plt.title('Life Expectancy Distribution by Country (20 year period)')
plt.xlabel('Country')
plt.ylabel('Life Expectancy (Years)')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()
