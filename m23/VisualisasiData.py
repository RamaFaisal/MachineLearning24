import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
'''
# Visualisasi Pie Chart
flavors = ('Chocolate', 'Vanilla', 'Pistachio', 'Mango', 'Strawberry')
votes = (12, 11, 4, 8, 7)
colors = ('#8B4513', '#FFF8DC', '#93C572', '#E67F0D', '#D53032') ##Kostumisasi warna pie chart
explode = (0, 0, 0, 0.1, 0)

plt.title('Favorite Ice Cream Flavors')
plt.pie(
    votes,
    labels = flavors,
    autopct = '%1.1f%%', #autopct digunakan untuk melihat berapa persen kontribusi masing masing rasa eskrim
    colors=colors,
    explode=explode,
    shadow=True,
)
plt.show()
'''

'''
# visualisasi bar chart
countries = ('Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador',
             'Falkland Islands', 'French Guiana', 'Guyana', 'Paraguay', 'Peru',
             'Suriname', 'Uruguay', 'Venezuela')

populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
               3481, 287750, 785409, 7107305, 32880332, 585169, 3470475,
               28258770)

df = pd.DataFrame({
    'Country' : countries,
    'Population' : populations,
})
df.sort_values(by='Population', inplace = True)

x_coords = np.arange(len(df))
colors = ['#0000FF' for _ in range(len(df))]
colors[-2] = '#FF0000' #Pewarnaan pada bar -2
plt.figure(figsize=(15,10)) #Size dari grafik
plt.bar(x_coords, df['Population'], tick_label=df['Country'], color=colors)
## x_coords = np.arange(len(countries)) #Sebelum diurutkan
## plt.bar(x_coords, populations) 
## plt.bar(x_coords, populations, tick_label=countries)
plt.xticks(rotation=90) #Memutar labels x-axis
plt.ylabel('Population (Millions)')
plt.title('South American Populations')
plt.show()
'''

#Visualisasi line graph
temperature_c_actual = [2, 1, 0, 0, 1, 5, 8, 9, 8, 5, 3, 2, 2]
temperature_c_predicted = [2, 2, 1, 0, 1, 3, 7, 8, 8, 6, 4, 3, 3]
hour = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

'''plt.plot(
    hour,
    temperature_c,
    marker='x',
)'''
'''plt.plot(hour, temperature_c_actual)
plt.plot(hour, temperature_c_predicted, linestyle='--')
plt.title('Temperatures in Kirkland, WA, USA on 2 Feb 2020')
plt.ylabel('Temperature Celsius')
plt.xlabel('Hour')
plt.show()'''

#visualisasi scatter plot
'''country = ['Bangladesh', 'Brazil', 'China', 'India', 'Indonesia', 'Japan', 
           'Mexico', 'Nigeria', 'Pakistan', 'Russia', 'United States']
gdp = [2421, 13418, 9475, 4353, 7378, 35477, 14276, 5087, 4133, 20255, 49267]
population = [148692131, 194946470, 1341335152, 1224614327, 239870937,
              126535920, 113423047, 158423182, 173593383, 142958164, 310383948]
plt.scatter(population, gdp)
plt.show()'''

'''#Visualisasi scatterplot dengan 2 variabel
lemon_diameter = [6.44, 6.87, 7.7, 8.85, 8.15, 9.96, 7.21, 10.04, 10.2, 11.06]
lemon_weight = [112.05, 114.58, 116.71, 117.4, 128.93, 
                132.93, 138.92, 145.98, 148.44, 152.81]

lime_diameter = [6.15, 7.0, 7.0, 7.69, 7.95, 7.51, 10.46, 8.72, 9.53, 10.09]
lime_weight = [112.76, 125.16, 131.36, 132.41, 138.08,
               142.55, 156.86, 158.67, 163.28, 166.74]
plt.title('Lemons vs Limes')
plt.xlabel('Diameter (cm)')
plt.ylabel('Weight (g)')
plt.scatter(lemon_diameter, lemon_weight, color='y')
plt.scatter(lime_diameter, lime_weight, color='g')
plt.legend(['lemons', 'limes'])
plt.show()'''

'''
# Visualisasi heatmap
import seaborn as sns
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City',
          'Beijing', 'Osaka', 'Cairo', 'New York', 'Dhaka', 'Karachi']
months = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
temperatures = [
  [10, 10, 14, 19, 23, 26, 30, 31, 27, 22, 17, 12], # Tokyo
  [20, 24, 30, 37, 40, 39, 35, 34, 34, 33, 28, 22], # Delhi
  [ 8, 10, 14, 20, 24, 28, 32, 32, 27, 23, 17, 11], # Shanghai
  [29, 29, 28, 27, 23, 23, 23, 25, 25, 26, 27, 28], # Sao Paulo
  [31, 32, 33, 33, 34, 32, 30, 30, 31, 34, 34, 32], # Mumbai
  [22, 24, 26, 27, 27, 26, 24, 25, 24, 24, 23, 23], # Mexico City
  [ 2,  5, 12, 21, 27, 30, 31, 30, 26, 19, 10,  4], # Beijing
  [ 9, 10, 14, 20, 25, 28, 32, 33, 29, 23, 18, 12], # Osaka
  [19, 21, 24, 29, 33, 35, 35, 35, 34, 30, 25, 21], # Cairo
  [ 4,  6, 11, 18, 22, 27, 29, 29, 25, 18, 13,  7], # New York
  [25, 29, 32, 33, 33, 32, 32, 32, 32, 31, 29, 26], # Dhaka
  [26, 28, 32, 35, 36, 35, 33, 32, 33, 35, 32, 28], # Karachi
]
sns.heatmap(temperatures, yticklabels=cities, xticklabels=months)
## plt.show()'''

'''cities = ['New York', 'Beijing', 'Tokyo', 'Osaka', 'Shanghai', 'Cairo', 'Delhi',
          'Karachi', 'Dhaka', 'Mexico City', 'Mumbai', 'Sao Paulo']

temperatures = [
  [ 4,  6, 11, 18, 22, 27, 29, 29, 25, 18, 13,  7], # New York
  [ 2,  5, 12, 21, 27, 30, 31, 30, 26, 19, 10,  4], # Beijing
  [10, 10, 14, 19, 23, 26, 30, 31, 27, 22, 17, 12], # Tokyo
  [ 9, 10, 14, 20, 25, 28, 32, 33, 29, 23, 18, 12], # Osaka
  [ 8, 10, 14, 20, 24, 28, 32, 32, 27, 23, 17, 11], # Shanghai
  [19, 21, 24, 29, 33, 35, 35, 35, 34, 30, 25, 21], # Cairo
  [20, 24, 30, 37, 40, 39, 35, 34, 34, 33, 28, 22], # Delhi
  [26, 28, 32, 35, 36, 35, 33, 32, 33, 35, 32, 28], # Karachi
  [25, 29, 32, 33, 33, 32, 32, 32, 32, 31, 29, 26], # Dhaka
  [22, 24, 26, 27, 27, 26, 24, 25, 24, 24, 23, 23], # Mexico City
  [31, 32, 33, 33, 34, 32, 30, 30, 31, 34, 34, 32], # Mumbai
  [29, 29, 28, 27, 23, 23, 23, 25, 25, 26, 27, 28], # Sao Paulo
]

##sns.heatmap(temperatures, yticklabels=cities, xticklabels=months)
sns.heatmap(
    temperatures,
    yticklabels=cities,
    xticklabels=months,
    cmap='coolwarm'
)
## plt.show()
'''

# Histogram
path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
print(df.head())

'''df.hist(column='price', bins=30)
plt.show()'''

# Melakukan plot beberapa grup
'''df.hist(column='price', by='drive-wheels', bins=20)
plt.show()'''

# Melakukan plot pada beberapa seri
'''df[['bore', 'stroke']].plot(kind='hist',
            alpha=0.7,
            bins=30,
            title='Histogram of Bore and Stroke in Engine',
            rot=45,
            grid=True,
            figsize=(12,8),
            fontsize=15,
            color=['#FF5733', '#5C33FF'])
plt.xlabel('Size')
plt.ylabel("Number of Cars")
plt.show()'''

'''from scipy import stats
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

print(df.dtypes)'''

# visualisasi scatter plot menggunakan regplot untuk mengetahui hubungan korelasi variabel 'engine-size' & 'price'
'''sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
plt.show()'''

#Korelasi 'engine-size' & 'price'
'''df[["engine-size", "price"]].corr()

# visualisasi scatter plot menggunakan regplot untuk mengetahui hubungan korelasi variabel 'engine-size' & 'price'
sns.regplot(x="highway-mpg", y="price", data=df)
plt.show()

# mengetahui korelasi 'highway-mpg' & 'price'
df[['highway-mpg', 'price']].corr()
'''
# visualisasi scatter plot menggunakan regplot untuk mengetahui hubungan korelasi variabel 'peak-rpm' & 'price'
'''sns.regplot(x="peak-rpm", y="price", data=df)
plt.show()'''

## df[['peak-rpm', 'price']].corr()

## Variabel Kategori Statistik
# visualisasi variabel kategori statistik variabel 'body-style' & 'price'
'''sns.boxplot(x="body-style", y="price", data=df)
plt.show()'''

'''sns.boxplot(x="engine-location", y="price", data=df)
plt.show()'''

'''df.describe(include=['object'])
df['drive-wheels'].value_counts() #menghitung nilai pada 'drive-wheels'
df['drive-wheels'].value_counts().to_frame()

# membuat dataframe baru dengan nama "drive_wheels_counts"
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
# mengganti nama "drive-wheels" menjadi "value_counts"
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts

# mengganti nama indeks menjadi 'drive-wheels'
drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts

# mengulang proses di atas dengan dataframe baru 'engine-location'
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(10)'''

## Grouping
df['drive-wheels'].unique()
df_group_one = df[['drive-wheels', 'body-style', 'price']]
df_group_one = df_group_one.groupby(['drive-wheels'], as_index=False).mean()
'''print(df_group_one)'''

df_gptest = df[['drive-wheels', 'body-style', 'price']]
grouped_test1 = df_gptest.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
##print(grouped_test1)

grouped_pivot = grouped_test1.pivot(index='drive-wheels', columns='body-style')
grouped_pivot = grouped_pivot.fillna(0)
print(grouped_pivot)

df_gptest2 = df[['body-style','price']]
grouped_test_bodystyle = df_gptest2.groupby(['body-style'],as_index= False).mean()
print(grouped_test_bodystyle)

plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()

fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

# nama label
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

# pindahkan ticks and labels ke tenah
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

# masukan  labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

# rotasi label
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()