from scipy import stats

# --- 1. Definisi Data ---
n_total = 1000
n_diterima = 300
mu = 62
sigma = 8

# --- 2. Menghitung Proporsi (Area di bawah kurva) ---
# Kita mencari skor minimal untuk 300 orang terbaik (Top 30%)
# Artinya, area di sebelah kanan kurva adalah 0.3
# Maka, area di sebelah kiri (kumulatif) adalah 1 - 0.3 = 0.7
proporsi_lulus = n_diterima / n_total
proporsi_kumulatif = 1 - proporsi_lulus

# --- 3. Mencari Nilai Z dan Skor Minimal (x) ---
# Menggunakan Percent Point Function (ppf) yang merupakan invers dari CDF
# Nilai x = mu + z * sigma
skor_minimal = stats.norm.ppf(proporsi_kumulatif, loc=mu, scale=sigma)

# Menghitung nilai Z secara spesifik untuk referensi
z_score = stats.norm.ppf(proporsi_kumulatif)

print(f"Proporsi yang dicari (Top %): {proporsi_lulus*100}%")
print(f"Nilai Z-score (batas 70%): {z_score:.4f}")
print(f"Hasil ujian minimal (x): {skor_minimal:.2f}")
