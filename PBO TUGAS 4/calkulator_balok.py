import tkinter as tk

def hitung_volume():
    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())
    tinggi = float(entry_tinggi.get())

    volume = panjang * lebar * tinggi

    hasil_var.set(f"Volume Balok: {volume} satuan kubik")

# Membuat instance dari Tkinter
root = tk.Tk()
root.title("Kalkulator Volume Balok")

# Variabel untuk menampung hasil perhitungan
hasil_var = tk.StringVar()

# Label dan Entry untuk panjang
label_panjang = tk.Label(root, text="Panjang:")
label_panjang.grid(row=0, column=0, padx=10, pady=10)
entry_panjang = tk.Entry(root)
entry_panjang.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk lebar
label_lebar = tk.Label(root, text="Lebar:")
label_lebar.grid(row=1, column=0, padx=10, pady=10)
entry_lebar = tk.Entry(root)
entry_lebar.grid(row=1, column=1, padx=10, pady=10)

# Label dan Entry untuk tinggi
label_tinggi = tk.Label(root, text="Tinggi:")
label_tinggi.grid(row=2, column=0, padx=10, pady=10)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=2, column=1, padx=10, pady=10)

# Tombol untuk menghitung volume
tombol_hitung = tk.Button(root, text="Hitung Volume", command=hitung_volume)
tombol_hitung.grid(row=3, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, textvariable=hasil_var)
label_hasil.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi Tkinter
root.mainloop()
