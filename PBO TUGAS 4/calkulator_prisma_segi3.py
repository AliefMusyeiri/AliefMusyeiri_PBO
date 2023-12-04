import tkinter as tk
import math

def hitung_volume():
    alas = float(entry_alas.get())
    tinggi_segitiga = float(entry_tinggi_segitiga.get())
    tinggi_prisma = float(entry_tinggi_prisma.get())

    luas_segitiga = 0.5 * alas * tinggi_segitiga
    volume = luas_segitiga * tinggi_prisma
    hasil_var.set(f"Volume Prisma Segitiga: {volume:.2f} satuan kubik")

# Membuat instance dari Tkinter
root = tk.Tk()
root.title("Kalkulator Volume Prisma Segitiga")

# Variabel untuk menampung hasil perhitungan
hasil_var = tk.StringVar()

# Label dan Entry untuk alas segitiga
label_alas = tk.Label(root, text="Alas Segitiga:")
label_alas.grid(row=0, column=0, padx=10, pady=10)
entry_alas = tk.Entry(root)
entry_alas.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk tinggi segitiga
label_tinggi_segitiga = tk.Label(root, text="Tinggi Segitiga:")
label_tinggi_segitiga.grid(row=1, column=0, padx=10, pady=10)
entry_tinggi_segitiga = tk.Entry(root)
entry_tinggi_segitiga.grid(row=1, column=1, padx=10, pady=10)

# Label dan Entry untuk tinggi prisma
label_tinggi_prisma = tk.Label(root, text="Tinggi Prisma:")
label_tinggi_prisma.grid(row=2, column=0, padx=10, pady=10)
entry_tinggi_prisma = tk.Entry(root)
entry_tinggi_prisma.grid(row=2, column=1, padx=10, pady=10)

# Tombol untuk menghitung volume
tombol_hitung = tk.Button(root, text="Hitung Volume", command=hitung_volume)
tombol_hitung.grid(row=3, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, textvariable=hasil_var)
label_hasil.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi Tkinter
root.mainloop()
