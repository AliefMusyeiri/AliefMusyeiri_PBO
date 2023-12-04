import tkinter as tk
from tkinter import ttk

def submit_schedule():
    day = day_var.get()
    time = time_var.get()
    course = course_entry.get()

    schedule_text.insert(tk.END, f"Day: {day}, Time: {time}, Course: {course}\n")
    clear_entries()

def clear_entries():
    day_var.set("")
    time_var.set("")
    course_entry.delete(0, tk.END)

# Membuat window utama
root = tk.Tk()
root.title("Jadwal Kuliah")

# Variabel StringVar untuk menyimpan nilai dropdown dan entry
day_var = tk.StringVar(root)
time_var = tk.StringVar(root)

# Label dan Entry untuk hari
day_label = tk.Label(root, text="Hari:")
day_label.grid(row=0, column=0, padx=10, pady=10)
day_entry = ttk.Combobox(root, textvariable=day_var, values=["Senin", "Selasa", "Rabu", "Kamis", "Jumat"])
day_entry.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk waktu
time_label = tk.Label(root, text="Waktu:")
time_label.grid(row=1, column=0, padx=10, pady=10)
time_entry = ttk.Combobox(root, textvariable=time_var, values=["08:00", "10:00", "13:00", "15:00"])
time_entry.grid(row=1, column=1, padx=10, pady=10)

# Label dan Entry untuk mata kuliah
course_label = tk.Label(root, text="Mata Kuliah:")
course_label.grid(row=2, column=0, padx=10, pady=10)
course_entry = tk.Entry(root)
course_entry.grid(row=2, column=1, padx=10, pady=10)

# Tombol Submit
submit_button = tk.Button(root, text="Submit", command=submit_schedule)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Text widget untuk menampilkan jadwal
schedule_text = tk.Text(root, height=10, width=40)
schedule_text.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan main loop
root.mainloop()
