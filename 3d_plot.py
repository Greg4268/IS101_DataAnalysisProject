import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv("./country_dataset.csv")
print(df.info())

y = df["Life Expectancy (Years)"].values
x = df["Healthcare Expenditure per Capita (USD)"].values
z = df["Doctor-to-Patient Ratio"].values

# Plotting the data
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='b', marker='o', edgecolors='k', alpha=0.7)
ax.view_init(elev=19, azim=-44, roll=0)

# Changing the background color of the 3D plot walls (panes)
ax.xaxis.pane.fill = True
ax.yaxis.pane.fill = True
ax.zaxis.pane.fill = True

ax.xaxis.pane.set_facecolor((0.2, 0.2, 0.2, 1))  
ax.yaxis.pane.set_facecolor((0.2, 0.2, 0.2, 1))
ax.zaxis.pane.set_facecolor((0.2, 0.2, 0.2, 1))

# Labelling Clusters by Country 
countries = ["USA", "Russia", "Canada", "China", "India", "Australia"]
grouped_data = {country: {'x': [], 'y': [], 'z': []} for country in countries}

for i in range(len(df)):
    country = countries[i % len(countries)]  
    grouped_data[country]['x'].append(x[i])
    grouped_data[country]['y'].append(y[i])
    grouped_data[country]['z'].append(z[i])

# Labeling the clusters with country names
for country, data in grouped_data.items():
    centroid_x = np.mean(data['x'])
    centroid_y = np.mean(data['y'])
    centroid_z = np.mean(data['z'])
    ax.text(centroid_x, centroid_y, centroid_z, country, fontsize=10, color='white')

# Set axis labels and title
ax.set_xlabel('Healthcare Expenditure per Capita (USD)')
ax.set_ylabel('Life Expectancy (Years)')
ax.set_zlabel('Doctor-to-Patient Ratio')
plt.title("How Doctor-to-Patient Ratio May Influence Life Expectancy")

plt.show()
