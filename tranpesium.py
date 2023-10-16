import tkinter as tk

def hitung_luas():
    sisi_atas = float(entry_sisi_atas.get())
    sisi_bawah = float(entry_sisi_bawah.get())
    tinggi = float(entry_tinggi.get())
    luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
    label_hasil.config(text=f"Luas: {luas}")

def hitung_keliling():
    sisi_atas = float(entry_sisi_atas.get())
    sisi_bawah = float(entry_sisi_bawah.get())
    sisi_miring1 = float(entry_sisi_miring1.get())
    sisi_miring2 = float(entry_sisi_miring2.get())
    keliling = sisi_atas + sisi_bawah + sisi_miring1 + sisi_miring2
    label_hasil.config(text=f"Keliling: {keliling}")

app = tk.Tk()
app.title("Kalkulator Trapesium")
app.geometry("400x400")

frame = tk.Frame(app, pady=10)
frame.pack()

label_sisi_atas = tk.Label(frame, text="Sisi Atas:")
label_sisi_atas.pack()

entry_sisi_atas = tk.Entry(frame)
entry_sisi_atas.pack()

label_sisi_bawah = tk.Label(frame, text="Sisi Bawah:")
label_sisi_bawah.pack()

entry_sisi_bawah = tk.Entry(frame)
entry_sisi_bawah.pack()

label_sisi_miring1 = tk.Label(frame, text="Sisi Miring 1:")
label_sisi_miring1.pack()

entry_sisi_miring1 = tk.Entry(frame)
entry_sisi_miring1.pack()

label_sisi_miring2 = tk.Label(frame, text="Sisi Miring 2:")
label_sisi_miring2.pack()

entry_sisi_miring2 = tk.Entry(frame)
entry_sisi_miring2.pack()

label_tinggi = tk.Label(frame, text="Tinggi:")
label_tinggi.pack()

entry_tinggi = tk.Entry(frame)
entry_tinggi.pack()

hitung_luas_button = tk.Button(frame, text="Hitung Luas", command=hitung_luas)
hitung_luas_button.pack()

hitung_keliling_button = tk.Button(frame, text="Hitung Keliling", command=hitung_keliling)
hitung_keliling_button.pack()

label_hasil = tk.Label(frame, text="", pady=10)
label_hasil.pack()

app.mainloop()
