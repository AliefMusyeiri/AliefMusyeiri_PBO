import tkinter as tk

def hitung_volume():
    sisi = float(entry_sisi.get())
    volume = sisi**3
    hasil_var.set(f"Volume Kubus: {volume} satuan kubik")

# Membuat instance dari Tkinter
root = tk.Tk()
root.title("Kalkulator Volume Kubus")

# Variabel untuk menampung hasil perhitungan
hasil_var = tk.StringVar()

# Label dan Entry untuk sisi
label_sisi = tk.Label(root, text="Panjang Sisi:")
label_sisi.grid(row=0, column=0, padx=10, pady=10)
entry_sisi = tk.Entry(root)
entry_sisi.grid(row=0, column=1, padx=10, pady=10)

# Tombol untuk menghitung volume
tombol_hitung = tk.Button(root, text="Hitung Volume", command=hitung_volume)
tombol_hitung.grid(row=1, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, textvariable=hasil_var)
label_hasil.grid(row=2, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi Tkinter
root.mainloop()
