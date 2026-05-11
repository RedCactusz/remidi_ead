import scipy.stats as stats

# --- 1. Definisi Data ---
sigma_0 = 3.00      # Standar deviasi spesifikasi (mm)
s = 3.15            # Standar deviasi sampel (mm)
n = 25              # Jumlah data
confidence = 0.95   # Selang kepercayaan 95%
alpha = 1 - confidence
df = n - 1          # Derajat kebebasan

# --- 2. Perhitungan Statistik Uji (Chi-Square Hitung) ---
# Rumus: chi_hitung = (df * s^2) / sigma_0^2
chi_hitung = (df * (s**2)) / (sigma_0**2)

# --- 3. Menentukan Nilai Kritis (Chi-Square Tabel) ---
# Karena kita menguji apakah kondisi "masih sama", ini adalah uji dua arah (two-tailed)
chi_kritis_bawah = stats.chi2.ppf(alpha/2, df)
chi_kritis_atas = stats.chi2.ppf(1 - alpha/2, df)

# --- 4. Pengambilan Keputusan ---
masih_sama = chi_kritis_bawah <= chi_hitung <= chi_kritis_atas

print(f"Statistik Uji (Chi-Square Hitung): {chi_hitung:.4f}")
print(f"Rentang Kritis: {chi_kritis_bawah:.4f} s/d {chi_kritis_atas:.4f}")

if masih_sama:
    print("\nKESIMPULAN: Kondisi alat MASIH SAMAA dengan spesifikasi.")
    print("Gagal tolak H0: Perbedaan tidak signifikan secara statistik.")
else:
    print("\nKESIMPULAN: Kondisi alat SUDAH BERBEDA dengan spesifikasi.")
    print("Tolak H0: Perbedaan signifikan secara statistik.")
