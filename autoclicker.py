# autoclicker.py
import threading
import time
import pyautogui
import pygetwindow as gw
import tkinter as tk
from tkinter import messagebox
from pynput import keyboard  # pip install pynput

# ---------------- PyAutoGUI Config ----------------
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False  # hati-hati: gerak ke pojok kiri atas tidak menghentikan otomatis

# ---------------- Globals ----------------
running = False
click_thread = None
monitor_thread = None
target_window = None
rel_click_x = None
rel_click_y = None

# Mouse idle detection
_last_mouse_pos = pyautogui.position()
_last_move_time = time.time()
_idle_lock = threading.Lock()

# ---------------- Helper Functions ----------------
def _update_mouse_activity_loop(poll=0.05):
    """Thread: pantau posisi mouse untuk mendeteksi kapan terakhir kali bergerak."""
    global _last_mouse_pos, _last_move_time
    while True:
        try:
            pos = pyautogui.position()
            with _idle_lock:
                if pos != _last_mouse_pos:
                    _last_mouse_pos = pos
                    _last_move_time = time.time()
        except Exception:
            pass
        time.sleep(poll)

def last_move_seconds_ago():
    with _idle_lock:
        return time.time() - _last_move_time

def find_window_by_name(name):
    wins = gw.getWindowsWithTitle(name)
    return wins[0] if wins else None

def get_abs_click_pos(win):
    if not win:
        return None
    if rel_click_x is None or rel_click_y is None:
        x = win.left + win.width // 2
        y = win.top + win.height // 2
    else:
        x = win.left + rel_click_x
        y = win.top + rel_click_y
    return (x, y)

# ---------------- Auto-click Loop ----------------
def auto_click_loop(interval, move_back, idle_threshold, require_idle):
    global running, target_window
    while running:
        try:
            # cek target
            if not target_window or not gw.getWindowsWithTitle(target_window.title):
                # target hilang -> hentikan
                running = False
                root.after(0, lambda: status_label.config(text="Status: Target hilang ❌", fg="orange"))
                break

            # refresh object (posisi/ukuran mungkin berubah)
            wins = gw.getWindowsWithTitle(target_window.title)
            if not wins:
                running = False
                root.after(0, lambda: status_label.config(text="Status: Target hilang ❌", fg="orange"))
                break
            tgt = wins[0]

            if tgt.isMinimized:
                # jendela diminimize -> skip klik
                # tetap running, hanya menunggu
                # Update status non-blocking
                root.after(0, lambda: status_label.config(text="Status: Target diminimalkan (menunggu)...", fg="orange"))
            else:
                # cek idle
                idle_ok = (not require_idle) or (last_move_seconds_ago() >= idle_threshold)
                if not idle_ok:
                    # jika user baru saja memindahkan mouse, tunda klik
                    root.after(0, lambda: status_label.config(
                        text=f"Status: Menunggu idle ({last_move_seconds_ago():.1f}s) ...", fg="orange"))
                else:
                    abs_pos = get_abs_click_pos(tgt)
                    if abs_pos:
                        x, y = abs_pos
                        # simpan posisi current
                        try:
                            cur = pyautogui.position()
                        except Exception:
                            cur = None

                        # lakukan klik
                        try:
                            pyautogui.click(x, y)
                        except Exception as e:
                            print("Klik gagal:", e)

                        # kembalikan kursor jika diinginkan
                        if move_back and cur:
                            try:
                                pyautogui.moveTo(cur)
                            except Exception:
                                pass

                        # update status
                        root.after(0, lambda: status_label.config(text=f"Status: Menjalankan (target: {tgt.title}) 🟢", fg="green"))
        except Exception as e:
            print("Error di auto loop:", e)
        # delay
        time.sleep(max(0.001, interval))

# ---------------- Control Functions ----------------
def start_clicking_gui():
    """Dipanggil dari GUI (thread-safe via main thread)."""
    global running, click_thread, target_window

    if running:
        messagebox.showinfo("Info", "Auto-clicker sudah berjalan!")
        return

    # parse interval
    try:
        interval = float(interval_entry.get())
        if interval <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka valid (>0) untuk interval.")
        return

    target_name = window_entry.get().strip()
    if not target_name:
        messagebox.showerror("Error", "Masukkan nama jendela target (misal: Roblox).")
        return

    win = find_window_by_name(target_name)
    if not win:
        messagebox.showerror("Error", f"Tidak ditemukan jendela dengan nama: {target_name}")
        return

    target_window = win
    running = True
    move_back = moveback_var.get()
    idle_threshold = float(idle_entry.get())
    require_idle = idle_var.get()

    status_label.config(text=f"Status: Menjalankan (target: {target_window.title}) 🟢", fg="green")
    click_thread = threading.Thread(target=auto_click_loop, args=(interval, move_back, idle_threshold, require_idle), daemon=True)
    click_thread.start()

def stop_clicking_gui():
    global running
    running = False
    status_label.config(text="Status: Berhenti 🔴", fg="red")

def exit_program():
    global running
    running = False
    root.destroy()
    # stop monitor thread by exiting program

# ---------------- Hotkey integration (F6 start, F7 stop) ----------------
def _on_hotkey_start():
    # schedule start on main thread
    root.after(0, start_clicking_gui)

def _on_hotkey_stop():
    root.after(0, stop_clicking_gui)

def hotkey_listener_thread():
    # menggunakan pynput GlobalHotKeys
    with keyboard.GlobalHotKeys({
        '<f6>': _on_hotkey_start,
        '<f7>': _on_hotkey_stop
    }) as h:
        h.join()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Auto Clicker — Safe Background Mode")
root.geometry("700x460")
root.minsize(520, 380)
root.resizable(True, True)

main = tk.Frame(root, padx=16, pady=16)
main.pack(fill="both", expand=True)

tk.Label(main, text="Auto Clicker — Klik di Jendela Target (aman untuk multitasking)", font=("Segoe UI", 14, "bold")).pack(pady=(0,10))

# interval
f1 = tk.Frame(main)
f1.pack(fill="x", pady=6)
tk.Label(f1, text="Interval (detik):", width=18, anchor="w").pack(side="left")
interval_entry = tk.Entry(f1, width=12, justify="center")
interval_entry.insert(0, "0.5")
interval_entry.pack(side="left")

# idle threshold
f_idle = tk.Frame(main)
f_idle.pack(fill="x", pady=6)
tk.Label(f_idle, text="Require Idle (s):", width=18, anchor="w").pack(side="left")
idle_entry = tk.Entry(f_idle, width=8, justify="center")
idle_entry.insert(0, "1.0")
idle_entry.pack(side="left", padx=(0,8))
idle_var = tk.BooleanVar(value=True)
tk.Checkbutton(f_idle, text="Tunda klik saat mouse baru bergerak (disarankan)", variable=idle_var).pack(side="left")

# window name
f2 = tk.Frame(main)
f2.pack(fill="x", pady=6)
tk.Label(f2, text="Nama Jendela Target (atau gunakan tombol Set Target Aktif):", anchor="w").pack(fill="x")
window_entry = tk.Entry(f2, width=60, font=("Segoe UI", 10))
window_entry.insert(0, "Roblox")
window_entry.pack(pady=4, anchor="w")

# actions
f_actions = tk.Frame(main)
f_actions.pack(fill="x", pady=6)
tk.Button(f_actions, text="Set Target dari Jendela Aktif", command=lambda: set_target_active()).pack(side="left", padx=6)
tk.Button(f_actions, text="Set Pos Relatif dari Pos Mouse Saat Ini", command=lambda: set_rel_pos()).pack(side="left", padx=6)
tk.Button(f_actions, text="Clear Pos Relatif (pakai tengah jendela)", command=lambda: clear_rel_pos()).pack(side="left", padx=6)

# pos label
pos_label = tk.Label(main, text="Pos relatif: (default = tengah jendela)")
pos_label.pack(pady=6)

# move back option
moveback_var = tk.BooleanVar(value=True)
tk.Checkbutton(main, text="Kembalikan posisi mouse setelah klik (disarankan)", variable=moveback_var).pack(pady=4)

# start/stop buttons
f_btn = tk.Frame(main)
f_btn.pack(pady=10)
tk.Button(f_btn, text="Mulai (F6)", width=14, height=2, bg="#4CAF50", fg="white", command=start_clicking_gui).grid(row=0, column=0, padx=8)
tk.Button(f_btn, text="Berhenti (F7)", width=14, height=2, bg="#F44336", fg="white", command=stop_clicking_gui).grid(row=0, column=1, padx=8)
tk.Button(f_btn, text="Keluar", width=14, height=2, bg="#555", fg="white", command=exit_program).grid(row=0, column=2, padx=8)

status_label = tk.Label(main, text="Status: Berhenti 🔴", fg="red", font=("Segoe UI", 11, "bold"))
status_label.pack(pady=12)

tk.Label(main, text="Catatan: jendela target harus tetap terbuka (tidak diminimize). Gunakan F6 untuk mulai / F7 untuk berhenti.", fg="gray").pack(pady=(6,0))

# ---------------- Utility GUI functions (needed above) ----------------
def set_target_active():
    active = gw.getActiveWindow()
    if not active:
        messagebox.showerror("Error", "Tidak ada jendela aktif terdeteksi.")
        return
    window_entry.delete(0, tk.END)
    window_entry.insert(0, active.title)
    messagebox.showinfo("Sukses", f"Target diset ke: {active.title}")

def set_rel_pos():
    global rel_click_x, rel_click_y, target_window
    if not target_window:
        # try to set from the name if possible
        name = window_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Set target window terlebih dahulu (atau gunakan 'Set Target Aktif').")
            return
        w = find_window_by_name(name)
        if not w:
            messagebox.showerror("Error", "Target window tidak ditemukan saat mencoba set posisi.")
            return
        target_window = w
    mx, my = pyautogui.position()
    wins = gw.getWindowsWithTitle(target_window.title)
    if not wins:
        messagebox.showerror("Error", "Target window tidak ditemukan saat mencoba set posisi.")
        return
    target_window = wins[0]
    rel_click_x = mx - target_window.left
    rel_click_y = my - target_window.top
    pos_label.config(text=f"Pos relatif: ({rel_click_x}, {rel_click_y})")
    messagebox.showinfo("Sukses", f"Posisi klik diset relatif ke jendela: ({rel_click_x}, {rel_click_y})")

def clear_rel_pos():
    global rel_click_x, rel_click_y
    rel_click_x = None
    rel_click_y = None
    pos_label.config(text="Pos relatif: (default = tengah jendela)")

# ---------------- Start background monitor & hotkey listener ----------------
# Start mouse activity monitor (daemon)
monitor_thread = threading.Thread(target=_update_mouse_activity_loop, daemon=True)
monitor_thread.start()

# Start hotkey listener (daemon)
hotkey_thread = threading.Thread(target=hotkey_listener_thread, daemon=True)
hotkey_thread.start()

# ---------------- Start GUI loop ----------------
root.mainloop()
