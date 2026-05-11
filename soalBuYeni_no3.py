import numpy as np

# --- 1. Definisi Data (Input) ---
h_arcmin = 3.0          # sudut heling dalam menit busur (')
sigma_h_arcsec = 2.0    # simpangan baku heling dalam detik busur (")
dm = 200.0              # jarak datar dalam meter (m)
sigma_dm = 0.02         # simpangan baku jarak datar (2 cm = 0.02 m)

# Konversi satuan ke Standar (Radian dan Meter)
h_rad = np.radians(h_arcmin / 60.0)
sigma_h_rad = np.radians(sigma_h_arcsec / 3600.0)

# --- 2. Perhitungan Beda Tinggi (Dh) ---
# Rumus: Dh = dm * tan(h)
dh = dm * np.tan(h_rad)

# --- 3. Perambatan Kesalahan (Error Propagation) ---
# Turunan parsial terhadap dm: d(Dh)/d(dm) = tan(h)
f_dm = np.tan(h_rad)

# Turunan parsial terhadap h: d(Dh)/d(h) = dm * sec^2(h)
# sec(h) = 1/cos(h)
f_h = dm / (np.cos(h_rad)**2)

# Rumus Perambatan Kesalahan (Matriks Varian-Kovarian Independen)
# sigma_Dh^2 = (f_dm * sigma_dm)^2 + (f_h * sigma_h_rad)^2
sigma_dh = np.sqrt((f_dm * sigma_dm)**2 + (f_h * sigma_h_rad)**2)

# --- 4. Output Hasil ---
print(f"Hasil Perhitungan:")
print(f"Beda Tinggi (Dh)     : {dh:.5f} meter")
print(f"Simpangan Baku (sigma_Dh): {sigma_dh:.5f} meter ({sigma_dh*1000:.2f} mm)")
