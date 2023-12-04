import tkinter as tk
import math

def hitung_volume():
    jari_jari = float(entry_jari_jari.get())
    tinggi = float(entry_tinggi.get())

    volume = math.pi * jari_jari**2 * tinggi
    hasil_var.set(f"Volume Tabung: {volume:.2f} satuan kubik")

# Membuat instance dari Tkinter
root = tk.Tk()
root.title("Kalkulator Volume Tabung")

# Variabel untuk menampung hasil perhitungan
hasil_var = tk.StringVar()

# Label dan Entry untuk jari-jari
label_jari_jari = tk.Label(root, text="Jari-Jari:")
label_jari_jari.grid(row=0, column=0, padx=10, pady=10)
entry_jari_jari = tk.Entry(root)
entry_jari_jari.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk tinggi
label_tinggi = tk.Label(root, text="Tinggi:")
label_tinggi.grid(row=1, column=0, padx=10, pady=10)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=1, column=1, padx=10, pady=10)

# Tombol untuk menghitung volume
tombol_hitung = tk.Button(root, text="Hitung Volume", command=hitung_volume)
tombol_hitung.grid(row=2, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, textvariable=hasil_var)
label_hasil.grid(row=3, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi Tkinter
root.mainloop()
