import tkinter as tk

def hitung_luas():
    alas = int(entry_alas.get())
    tinggi = int(entry_tinggi.get())
    luas = alas * tinggi
    label_hasil.config(text=f"Luas: {luas}")

def hitung_keliling():
    sisi1 = int(entry_sisi1.get())
    sisi2 = int(entry_sisi2.get())
    keliling = 2 * (sisi1 + sisi2)
    label_hasil.config(text=f"Keliling: {keliling}")

app = tk.Tk()
app.title("Kalkulator Jajar Genjang")
app.geometry("300x300")

frame = tk.Frame(app, pady=10)
frame.pack()

label_alas = tk.Label(frame, text="Alas:")
label_alas.pack()

entry_alas = tk.Entry(frame)
entry_alas.pack()

label_tinggi = tk.Label(frame, text="Tinggi:")
label_tinggi.pack()

entry_tinggi = tk.Entry(frame)
entry_tinggi.pack()

label_sisi1 = tk.Label(frame, text="Sisi 1:")
label_sisi1.pack()

entry_sisi1 = tk.Entry(frame)
entry_sisi1.pack()

label_sisi2 = tk.Label(frame, text="Sisi 2:")
label_sisi2.pack()

entry_sisi2 = tk.Entry(frame)
entry_sisi2.pack()

hitung_luas_button = tk.Button(frame, text="Hitung Luas", command=hitung_luas)
hitung_luas_button.pack()

hitung_keliling_button = tk.Button(frame, text="Hitung Keliling", command=hitung_keliling)
hitung_keliling_button.pack()

label_hasil = tk.Label(frame, text="", pady=10)
label_hasil.pack()

app.mainloop()
