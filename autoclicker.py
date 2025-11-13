import threading
import time
import pyautogui
import tkinter as tk
from tkinter import messagebox

# ====== Variabel Global ======
running = False
thread = None

# ====== Fungsi Auto Click ======
def auto_click(interval):
    global running
    while running:
        pyautogui.click()
        time.sleep(interval)

# ====== Fungsi Kontrol ======
def start_clicking():
    global running, thread
    if running:
        messagebox.showinfo("Info", "Auto-clicker sudah berjalan!")
        return
    
    try:
        interval = float(interval_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk interval.")
        return

    running = True
    status_label.config(text="Status: Berjalan 🟢", fg="green")
    
    # Jalankan thread agar GUI tidak hang
    thread = threading.Thread(target=auto_click, args=(interval,), daemon=True)
    thread.start()

def stop_clicking():
    global running
    running = False
    status_label.config(text="Status: Berhenti 🔴", fg="red")

def exit_program():
    global running
    running = False
    root.destroy()

# ====== GUI ======
root = tk.Tk()
root.title("Auto Clicker Python 🖱️")
root.geometry("300x220")
root.resizable(False, False)

# Judul
tk.Label(root, text="Auto Clicker Python", font=("Segoe UI", 14, "bold")).pack(pady=10)

# Input interval
frame = tk.Frame(root)
frame.pack(pady=5)
tk.Label(frame, text="Interval (detik):").grid(row=0, column=0, padx=5)
interval_entry = tk.Entry(frame, width=10, justify="center")
interval_entry.insert(0, "0.1")  # default 0.1 detik
interval_entry.grid(row=0, column=1)

# Tombol kontrol
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
start_btn = tk.Button(btn_frame, text="Mulai", width=10, command=start_clicking, bg="#4CAF50", fg="white")
start_btn.grid(row=0, column=0, padx=5)
stop_btn = tk.Button(btn_frame, text="Berhenti", width=10, command=stop_clicking, bg="#F44336", fg="white")
stop_btn.grid(row=0, column=1, padx=5)

# Label status
status_label = tk.Label(root, text="Status: Berhenti 🔴", fg="red", font=("Segoe UI", 10, "bold"))
status_label.pack(pady=10)

# Tombol keluar
tk.Button(root, text="Keluar", command=exit_program, bg="#555", fg="white", width=10).pack()

# Jalankan GUI
root.mainloop()
