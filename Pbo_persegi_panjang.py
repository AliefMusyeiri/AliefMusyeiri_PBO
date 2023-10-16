import tkinter as tk

def hitung_luas():
    panjang = int(entry_panjang.get())
    lebar = int(entry_lebar.get())
    luas = panjang * lebar
    label_hasil.config(text=f"Luas: {luas}")

def hitung_keliling():
    panjang = int(entry_panjang.get())
    lebar = int(entry_lebar.get())
    keliling = 2 * (panjang + lebar)
    label_hasil.config(text=f"Keliling: {keliling}")

app = tk.Tk()
app.title("Kalkulator Persegi Panjang")
app.geometry("300x200")

frame = tk.Frame(app, pady=10)
frame.pack()

label_panjang = tk.Label(frame, text="Panjang:")
label_panjang.pack()

entry_panjang = tk.Entry(frame)
entry_panjang.pack()

label_lebar = tk.Label(frame, text="lebar:")
label_lebar.pack()

entry_lebar = tk.Entry(frame)
entry_lebar.pack()

hitung_button = tk.Button(frame, text="Hitung Luas", command=hitung_luas)
hitung_button.pack()

hitung_keliling_button = tk.Button(frame, text="Hitung Keliling", command=hitung_keliling)
hitung_keliling_button.pack()

label_hasil = tk.Label(frame, text="", pady=10)
label_hasil.pack()

app.mainloop()