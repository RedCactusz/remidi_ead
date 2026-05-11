import numpy as np
from scipy import stats

# --- 1. Definisi Data ---
mu = 260.125      # rata-rata pengukuran (m)
sigma = 0.015     # ketelitian/standar deviasi (m)
confidence = 0.95 # selang kepercayaan 95%

# --- 2. Menghitung Nilai Kritis Z ---
# Untuk selang kepercayaan 95%, alpha = 1 - 0.95 = 0.05
# Karena ini interval dua sisi (batas bawah & atas), area di tiap ujung adalah alpha/2 = 0.025
# Nilai Z dicari pada probabilitas kumulatif 1 - 0.025 = 0.975
z_critical = stats.norm.ppf(1 - (1 - confidence) / 2)

# --- 3. Menghitung Batas (Margin of Error) ---
margin_of_error = z_critical * sigma

batas_bawah = mu - margin_of_error
batas_atas = mu + margin_of_error

# --- 4. Output ---
print(f"Nilai Kritis Z (95%): {z_critical:.3f}")
print(f"Margin of Error    : {margin_of_error:.5f} m")
print(f"Batas Bawah        : {batas_bawah:.5f} m")
print(f"Batas Atas         : {batas_atas:.5f} m")
print(f"\nRentang Ukuran: {batas_bawah:.5f} m s/d {batas_atas:.5f} m")
