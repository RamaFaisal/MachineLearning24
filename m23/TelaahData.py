#Import Library
import pandas as pd
import numpy as np

#Load dataset
path = "epl-goalScorer(20-21).csv"
df = pd.read_csv(path)

print(df.head()) #Menampilkan 5 baris awal dari dataset
print(df.tail()) #Menampilkan 5 baris akhir dari dataset
print(df.dtypes) #Mengungkap tipe tipe data dari setiap kolom

df_noid = df.iloc[:, 2:] #Ini adalah cara menggunakan metode iloc (index location) pada DataFrame df untuk memilih baris dan kolom berdasarkan posisi numerik. ':' mengindikasikan bahwa kita memilih semua baris, dan 2: mengindikasikan bahwa kita memilih kolom mulai dari posisi indeks 2 (kolom ke-3) hingga kolom terakhir
## df_noid akan berisi semua baris dari DataFrame awal (df), tetapi hanya akan berisi kolom-kolom mulai dari kolom ke-3 hingga kolom terakhir.
print(df_noid)
print(df_noid.describe()) #Menampilkan statistik dasar setiap kolom data yang bertipe numerik
print(df_noid.describe(include="all")) #Menampilkan juga statistik kolom yang bertipe non-numerik

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns #kode ini figunakan untuk memilih kolom DataFrame berdasarkan tipe data numerik yaitu integer dan float, select_dtypes digunakan untuk memfilter kolom data df
df_noid = df[numeric_cols] #kode ini digunakan untuk membuat dataFrame baru dengan memilih kolom yang sudah ditentukan di kode sebelumnya
print(df_noid.mean()) 
print(df_noid.sum())
print(df_noid.var()) #digunakan untuk mencetak varians dari setiap kolom
print(df_noid.std()) #digunakan untuk menghitung simpangan baku dari setiap kolom
print(df_noid.quantile(0.75)) #digunakan untuk menghitung kuartil tertentu dalam setiap kolom. 0,75 mengindikasikan bahwa kita ingin menghitung kuartil ke-3

q1 = df_noid.quantile(0.25) #Menghitung kuartil Q1
q3 = df_noid.quantile(0.75) #Menghitung kuartil Q3
iqr = q3 - q1 #Menghitung jangkauan antarkuartil dengan mengurangkan Q1 dan Q3
print(iqr)

import warnings
warnings.filterwarnings('ignore')

df_noid_aligndf_noid_align, iqr_new = df_noid.align(iqr, axis=1, copy=False, join='outer')
outlier_filter = (df_noid < q1 - 1.5 * iqr_new) | (df_noid > q3 + 1.5 * iqr_new) #Operasi ini menghasilkan DataFrame boolean dengan nilai 'true' sbg outlier dan 'false; sbg non-outlier
print(outlier_filter)

df_noid['player_name'] = df['player_name']
#Menyalin kolom 'player_name' ke dalam DataFrame df_noid
result = df_noid[outlier_filter['assists']] \
    .loc[:, ['player_name', 'assists']] \
    .sort_values(by=['assists'], ascending = False) #Mengurutkan dataFrame yg telah difilter berdasarkan nilai assist mulai dari tertinggi ke terendah
print(result) 

df_noid['team_title'] = df['team_title']
print(df_noid['team_title'].value_counts()) #Menghitung jumla pemain dari setiap tim yg terdapat dalam kolom 'team_title'
print(df.groupby('team_title')['goals'].std()) #Menghitung simpangan baku dari jumlah gol yang dicetak oleh pemain dari setiap tim
print(df.groupby('team_title')['goals'].mean()) #Menghitung rata-rata jumlah gol untuk setiap tim

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
df_noid = df[numeric_cols]
correlation_matrix = df_noid.loc[:, 'games':].corr()
print(correlation_matrix) #Menghitung korelasi antara semua pasangan kolom numerik yang dipilih