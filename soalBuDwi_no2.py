import numpy as np
from scipy import stats

# --- 1. Definisi Data ---
n = 30
mean_x = 60.0      # derajat
s = 0.05           # standar deviasi sampel (derajat)
confidence = 0.90  # 90%
alpha = 1 - confidence
df = n - 1         # derajat kebebasan (degrees of freedom)

# --- 2. Selang Kepercayaan untuk Mean (mu) ---
# Menggunakan distribusi t karena menggunakan standar deviasi sampel s
t_crit = stats.t.ppf(1 - alpha/2, df)
margin_mean = t_crit * (s / np.sqrt(n))

mu_lower = mean_x - margin_mean
mu_upper = mean_x + margin_mean

# --- 3. Selang Kepercayaan untuk Varian (sigma^2) ---
# Rumus: [(n-1)s^2 / chi_upper, (n-1)s^2 / chi_lower]
chi_lower = stats.chi2.ppf(alpha/2, df)      # batas kiri
chi_upper = stats.chi2.ppf(1 - alpha/2, df)  # batas kanan

var_sample = s**2
var_lower = (df * var_sample) / chi_upper
var_upper = (df * var_sample) / chi_lower

# --- 4. Output ---
print(f"--- Selang Kepercayaan {confidence*100:.0f}% ---")
print(f"1. Untuk Mean (mu):")
print(f"   t-critical: {t_crit:.4f}")
print(f"   Rentang   : {mu_lower:.5f}° s/d {mu_upper:.5f}°")

print(f"\n2. Untuk Varian (sigma^2):")
print(f"   Chi-Square (L): {chi_lower:.4f}, (U): {chi_upper:.4f}")
print(f"   Rentang       : {var_lower:.7f} s/d {var_upper:.7f}")
