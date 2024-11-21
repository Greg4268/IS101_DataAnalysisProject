import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./country_dataset.csv')

country_df = df[df['Country'] == 'USA']

country_df['Smoothed Life Expectancy'] = country_df['Life Expectancy (Years)'].rolling(window=3).mean()
country_df['Smoothed Doctor-to-Patient Ratio'] = country_df['Doctor-to-Patient Ratio'].rolling(window=3).mean()

# Normalize the data for comparison
max_life_expectancy = country_df['Smoothed Life Expectancy'].max()
min_life_expectancy = country_df['Smoothed Life Expectancy'].min()
max_ratio = country_df['Smoothed Doctor-to-Patient Ratio'].max()
min_ratio = country_df['Smoothed Doctor-to-Patient Ratio'].min()

country_df['Normalized Life Expectancy'] = (country_df['Smoothed Life Expectancy'] - min_life_expectancy) / (max_life_expectancy - min_life_expectancy)
country_df['Normalized Doctor-to-Patient Ratio'] = (country_df['Smoothed Doctor-to-Patient Ratio'] - min_ratio) / (max_ratio - min_ratio)

# Plotting the data
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot normalized life expectancy
ax1.plot(country_df['Year'], country_df['Normalized Life Expectancy'], color='blue', linewidth=2, label='Normalized Life Expectancy')
ax1.set_xlabel('Year')
ax1.set_ylabel('Normalized Life Expectancy', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis
ax2 = ax1.twinx()
ax2.plot(country_df['Year'], country_df['Normalized Doctor-to-Patient Ratio'], color='green', linewidth=2, label='Normalized Doctor-to-Patient Ratio')
ax2.set_ylabel('Normalized Doctor-to-Patient Ratio', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Title and legends
plt.title('Comparison of Life Expectancy and Doctor-to-Patient Ratio Over Time (Normalized)')
fig.tight_layout()
plt.show()

