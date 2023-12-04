import tkinter as tk
import math

def hitung_volume():
    alas = float(entry_alas.get())
    tinggi_alas = float(entry_tinggi_alas.get())
    tinggi_limas = float(entry_tinggi_limas.get())

    volume = (1/3) * alas * tinggi_alas * tinggi_limas
    hasil_var.set(f"Volume Limas Segitiga: {volume:.2f} satuan kubik")

# Membuat instance dari Tkinter
root = tk.Tk()
root.title("Kalkulator Volume Limas Segitiga")

# Variabel untuk menampung hasil perhitungan
hasil_var = tk.StringVar()

# Label dan Entry untuk alas
label_alas = tk.Label(root, text="Alas Segitiga:")
label_alas.grid(row=0, column=0, padx=10, pady=10)
entry_alas = tk.Entry(root)
entry_alas.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk tinggi alas
label_tinggi_alas = tk.Label(root, text="Tinggi Alas:")
label_tinggi_alas.grid(row=1, column=0, padx=10, pady=10)
entry_tinggi_alas = tk.Entry(root)
entry_tinggi_alas.grid(row=1, column=1, padx=10, pady=10)

# Label dan Entry untuk tinggi limas
label_tinggi_limas = tk.Label(root, text="Tinggi Limas:")
label_tinggi_limas.grid(row=2, column=0, padx=10, pady=10)
entry_tinggi_limas = tk.Entry(root)
entry_tinggi_limas.grid(row=2, column=1, padx=10, pady=10)

# Tombol untuk menghitung volume
tombol_hitung = tk.Button(root, text="Hitung Volume", command=hitung_volume)
tombol_hitung.grid(row=3, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, textvariable=hasil_var)
label_hasil.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi Tkinter
root.mainloop()
