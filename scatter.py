import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np 


df = pd.read_csv("./country_dataset.csv")
print(df.info())

plt.figure(figsize=(14, 6))

# Scatter Plot Comparing LF to HE (overall)
y = df["Life Expectancy (Years)"].values
x = df["Healthcare Expenditure per Capita (USD)"].values
plt.scatter(x , y, c="pink", linewidths=2, edgecolors="red", s = 50)

# log scale
plt.xscale('log')

# linear model in log space 
log_x = np.log10(x)
slope, intercept = np.polyfit(log_x, y, 1)
trendline = slope * log_x + intercept 

# plot trendline 
plt.plot(df['Healthcare Expenditure per Capita (USD)'], trendline, color='r', label=f'Trendline: y = {slope:.2f}x + {intercept:.2f}')

# Add ellipse around clusters 
ellipse_1 = Ellipse((73, 69), width=10, height=10, fill=False, edgecolor='b', linestyle='--', linewidth=2, alpha=0.5)
plt.gca().add_patch(ellipse_1)

ellipse_2 = Ellipse((451,76), width=75, height=10, fill=False, edgecolor='r', linestyle='-.',linewidth=2, alpha=0.5)
plt.gca().add_patch(ellipse_2)

ellipse_3 = Ellipse((530,73), width=80, height=10, fill=False, edgecolor='g', linestyle='-',linewidth=2, alpha=0.5)
plt.gca().add_patch(ellipse_3)

# overlapping country data 
ellipse_4 = Ellipse((5251,83), width=900, height=10, fill=False, edgecolor='#3d7dd5', linestyle='--',linewidth=2, alpha=0.5)
plt.gca().add_patch(ellipse_4)
ellipse_5 = Ellipse((5251,82.75), width=900, height=10, fill=False, edgecolor='#f35837', linestyle='-',linewidth=2, alpha=0.5)
plt.gca().add_patch(ellipse_5)

ellipse_6 = Ellipse((11028,79), width=1600, height=10, fill=False, edgecolor='b', linestyle='--',linewidth=2, alpha=0.5)
plt.gca().add_patch(ellipse_6)

# TO DO: Label Clusters by Country 


# title and axis 
plt.title("Healthcare Expenditure per Capita (USD) vs Life Expectancy (Years)")
plt.xlabel("Healthcare Expenditure per Capita (USD)")
plt.ylabel("Life Expectancy (Years)")
plt.legend()
plt.show()








