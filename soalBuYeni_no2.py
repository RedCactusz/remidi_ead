import numpy as np

# --- BAGIAN A: Matriks Varian-Kovarian ---
# Diketahui:
sigma_x = 2.1  # cm
sigma_y = 3.4  # cm
rho_xy = -0.1  # korelasi

# Menghitung Varian
var_x = sigma_x**2
var_y = sigma_y**2

# Menghitung Kovarian (sigma_xy = rho_xy * sigma_x * sigma_y)
sigma_xy = rho_xy * sigma_x * sigma_y

# Menyusun Matriks Varian-Kovarian (Sigma)
Sigma = np.array([
    [var_x, sigma_xy],
    [sigma_xy, var_y]
])

print("a. Matriks Varian-Kovarian Koordinat A (cm^2):")
print(Sigma)

# --- BAGIAN B: Matriks Bobot ---
# Diketahui:
sigma_bx = 3     # cm
sigma_by = 9     # cm
sigma_0_sq = 3   # varian aposteriori (sigma nol kuadrat) dalam cm

# Menghitung Matriks Varian B (Asumsi independen karena korelasi tidak disebutkan)
Sigma_B = np.array([
    [sigma_bx**2, 0],
    [0, sigma_by**2]
])

# Menghitung Matriks Bobot (P = sigma_0_sq * inv(Sigma_B))
# Rumus: P = sigma_0^2 * Sigma^-1
Sigma_B_inv = np.linalg.inv(Sigma_B)
P = sigma_0_sq * Sigma_B_inv

print("\nb. Matriks Bobot Pengukuran Koordinat B:")
print(P)
