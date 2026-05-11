import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Data dari soal bu Yeni
data = {
    'Interval': ['41-50', '51-60', '61-70', '71-80', '81-90', '91-100'],
    'fi': [8, 15, 31, 53, 35, 18]
}
df = pd.DataFrame(data)

# Ekstraksi batas bawah (bb), batas atas (ba), dan nilai tengah (xi)
df[['bb', 'ba']] = df['Interval'].str.split('-', expand=True).astype(int)
df['xi'] = (df['bb'] + df['ba']) / 2
df['fk'] = df['fi'].cumsum()  # Frekuensi kumulatif
n = df['fi'].sum()

# --- BAGIAN A: RATA-RATA, MEDIAN, MODUS ---

# Mean (Rata-rata)
mean_val = (df['xi'] * df['fi']).sum() / n

# Median
# Letak median di n/2 = 160/2 = 80. Berada di kelas 71-80.
L = 70.5  # Tepi bawah kelas median
fk_sebelum = 54
f_med = 53
p = 10    # Panjang kelas
median_val = L + ((n/2 - fk_sebelum) / f_med) * p

# Modus
# Frekuensi tertinggi adalah 53 (kelas 71-80)
d1 = 53 - 31
d2 = 53 - 35
modus_val = L + (d1 / (d1 + d2)) * p

print(f"a. Rata-rata: {mean_val:.2f}")
print(f"   Median:    {median_val:.2f}")
print(f"   Modus:     {modus_val:.2f}")

# --- BAGIAN B: VISUALISASI ---
plt.figure(figsize=(10, 6))

# Histogram
bars = plt.bar(df['xi'], df['fi'], width=10, color='skyblue', edgecolor='black', alpha=0.7, label='Histogram')

# Poligon Frekuensi
plt.plot(df['xi'], df['fi'], marker='o', color='red', linestyle='-', linewidth=2, label='Poligon')

# Plot Mean
plt.axvline(mean_val, color='green', linestyle='--', linewidth=2, label=f'Mean ({mean_val:.2f})')

# Label dan Estetika
plt.title('Histogram dan Poligon Nilai Ujian Masuk', fontsize=14)
plt.xlabel('Nilai Tengah (xi)', fontsize=12)
plt.ylabel('Frekuensi (fi)', fontsize=12)
plt.xticks(df['xi'])
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.show()

# --- BAGIAN C: ANALISIS KELULUSAN ---
# Batas lulus = 71.
# Yang tidak lulus adalah kelompok 41-50, 51-60, 61-70.
mhs_tidak_lulus = df.iloc[0:3]['fi'].sum()
mhs_lulus = n - mhs_tidak_lulus
persen_lulus = (mhs_lulus / n) * 100

print(f"\nc. Persentase Lulus: {persen_lulus:.2f}%")
print(f"   Jumlah Mahasiswa Tidak Lulus: {mhs_tidak_lulus}")
