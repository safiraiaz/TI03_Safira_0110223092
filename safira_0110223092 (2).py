# -*- coding: utf-8 -*-
"""Safira-0110223092

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pp9PnYXpVFcHRwwk9YNDogxa87mUFwuv
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca file CSV
data = pd.read_csv('/content/500_Person_Gender_Height_Weight_Index.csv')

# Menampilkan seluruh data
print(data)

# Menghitung statistik untuk tinggi dan berat badan berdasarkan Gender
statistik = data.groupby('Gender').agg(
    count_height=('Height', 'count'),
    avg_height=('Height', 'mean'),
    max_height=('Height', 'max'),
    min_height=('Height', 'min'),
    count_weight=('Weight', 'count'),
    avg_weight=('Weight', 'mean'),
    max_weight=('Weight', 'max'),
    min_weight=('Weight', 'min')
)

# Menampilkan hasil
print(statistik)

# Mengubah kolom Gender menjadi biner: Female = 0, Male = 1
data['Gender'] = data['Gender'].map({'Female': 0, 'Male': 1})

# Menampilkan 5 baris pertama untuk memverifikasi perubahan
print(data.head())

# Menggunakan seaborn untuk membuat grafik distribusi Index BMI berdasarkan Gender
plt.figure(figsize=(8, 6))
sns.countplot(x='Index', hue='Gender', data=data)

# Menambahkan judul dan label
plt.title('Distribusi Index BMI Berdasarkan Gender')
plt.xlabel('Index BMI')
plt.ylabel('Jumlah')
plt.legend(title='Gender', loc='upper right', labels=['Female', 'Male'])

# Menampilkan grafik
plt.show()