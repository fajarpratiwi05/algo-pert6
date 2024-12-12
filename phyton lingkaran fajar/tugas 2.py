import math

# Fungsi untuk menghitung hipotenusa
def hitung_hipotenusa(a, b):
    c = math.sqrt(a**2 + b**2)  # Rumus Pythagoras
    return c

# Nilai a dan b
a = 7
b = 5

# Menghitung hipotenusa
c = hitung_hipotenusa(a, b)

# Menampilkan hasil
print(f"Panjang hipotenusa adalah: {c}")