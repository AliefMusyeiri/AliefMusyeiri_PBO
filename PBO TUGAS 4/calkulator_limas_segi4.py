import tkinter as tk

def hitung_volume():
    panjang_sisi_alas = float(entry_sisi_alas.get())
    tinggi_limas = float(entry_tinggi_limas.get())

    volume = (1/3) * panjang_sisi_alas**2 * tinggi_limas
    hasil_var.set(f"Volume Limas Segi Empat: {volume:.2f} satuan kubik")

# Membuat instance dari Tkinter
root = tk.Tk()
root.title("Kalkulator Volume Limas Segi Empat")

# Variabel untuk menampung hasil perhitungan
hasil_var = tk.StringVar()

# Label dan Entry untuk panjang sisi alas
label_sisi_alas = tk.Label(root, text="Panjang Sisi Alas:")
label_sisi_alas.grid(row=0, column=0, padx=10, pady=10)
entry_sisi_alas = tk.Entry(root)
entry_sisi_alas.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk tinggi limas
label_tinggi_limas = tk.Label(root, text="Tinggi Limas:")
label_tinggi_limas.grid(row=1, column=0, padx=10, pady=10)
entry_tinggi_limas = tk.Entry(root)
entry_tinggi_limas.grid(row=1, column=1, padx=10, pady=10)

# Tombol untuk menghitung volume
tombol_hitung = tk.Button(root, text="Hitung Volume", command=hitung_volume)
tombol_hitung.grid(row=2, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, textvariable=hasil_var)
label_hasil.grid(row=3, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi Tkinter
root.mainloop()
