import tkinter as tk

def hitung_luas():
    sisi = int(entry_sisi.get())
    luas = sisi ** 2
    label_hasil.config(text=f"Luas: {luas}")

def hitung_keliling():
    sisi = int(entry_sisi.get())
    keliling = 4 * sisi
    label_hasil.config(text=f"Keliling: {keliling}")

app = tk.Tk()
app.title("Kalkulator Persegi")
app.geometry("300x200")

frame = tk.Frame(app, pady=10)
frame.pack()

label_sisi = tk.Label(frame, text="Sisi:")
label_sisi.pack()

entry_sisi = tk.Entry(frame)
entry_sisi.pack()

hitung_luas_button = tk.Button(frame, text="Hitung Luas", command=hitung_luas)
hitung_luas_button.pack()

hitung_keliling_button = tk.Button(frame, text="Hitung Keliling", command=hitung_keliling)
hitung_keliling_button.pack()

label_hasil = tk.Label(frame, text="", pady=10)
label_hasil.pack()

app.mainloop()
