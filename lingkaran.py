import tkinter as tk
import math

def hitung_luas():
    jari_jari = int(entry_jari_jari.get())
    luas = math.pi * jari_jari ** 2
    label_hasil.config(text=f"Luas: {luas:.2f}")

def hitung_keliling():
    jari_jari = int(entry_jari_jari.get())
    keliling = 2 * math.pi * jari_jari
    label_hasil.config(text=f"Keliling: {keliling:.2f}")

app = tk.Tk()
app.title("Kalkulator Lingkaran")
app.geometry("300x200")

frame = tk.Frame(app, pady=10)
frame.pack()

label_jari_jari = tk.Label(frame, text="Jari-jari:")
label_jari_jari.pack()

entry_jari_jari = tk.Entry(frame)
entry_jari_jari.pack()

hitung_luas_button = tk.Button(frame, text="Hitung Luas", command=hitung_luas)
hitung_luas_button.pack()

hitung_keliling_button = tk.Button(frame, text="Hitung Keliling", command=hitung_keliling)
hitung_keliling_button.pack()

label_hasil = tk.Label(frame, text="", pady=10)
label_hasil.pack()

app.mainloop()
