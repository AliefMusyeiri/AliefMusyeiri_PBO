import tkinter as tk

def hitung_luas():
    diagonal1 = float(entry_diagonal1.get())
    diagonal2 = float(entry_diagonal2.get())
    luas = 0.5 * diagonal1 * diagonal2
    label_hasil.config(text=f"Luas: {luas}")

def hitung_keliling():
    sisi = float(entry_sisi.get())
    keliling = 4 * sisi
    label_hasil.config(text=f"Keliling: {keliling}")

app = tk.Tk()
app.title("Kalkulator Belah Ketupat")
app.geometry("300x300")

frame = tk.Frame(app, pady=10)
frame.pack()

label_diagonal1 = tk.Label(frame, text="Diagonal 1:")
label_diagonal1.pack()

entry_diagonal1 = tk.Entry(frame)
entry_diagonal1.pack()

label_diagonal2 = tk.Label(frame, text="Diagonal 2:")
label_diagonal2.pack()

entry_diagonal2 = tk.Entry(frame)
entry_diagonal2.pack()

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
