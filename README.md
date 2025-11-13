# 🕹️ Auto Clicker Python — Versi GUI Update V.1

Auto Clicker canggih berbasis **Python + Tkinter + PyAutoGUI** yang mampu melakukan klik otomatis **pada jendela aplikasi tertentu (misal: Roblox)** bahkan **sambil kamu membuka aplikasi lain**.
Dapat dijalankan langsung dari Python atau dikompilasi menjadi **aplikasi `.exe` Windows** tanpa perlu membuka VS Code.

---

## ✨ Fitur Utama

✅ Klik otomatis dengan interval waktu yang dapat diatur
✅ Bisa mengarahkan klik ke **jendela target tertentu** (misal: “Roblox”)
✅ Menyimpan posisi klik relatif terhadap jendela target
✅ Tetap bisa **berpindah ke aplikasi lain** saat auto-click berjalan
✅ Klik **akan berhenti otomatis saat kursor digerakkan**, dan **aktif kembali setelah kursor diam selama 1 detik** ⚡
✅ GUI sederhana dan responsif (Tkinter)
✅ Tombol **Mulai / Berhenti / Keluar** dengan indikator status real-time
✅ Dapat dibuild menjadi file `.exe` agar mudah digunakan

---

## 📁 Struktur Proyek

```
coba-autoklik/
│
├── autoclicker.py        # Script utama aplikasi
├── requirements.txt      # Daftar library Python yang dibutuhkan
├── build.bat             # Script otomatis untuk install + build .exe
├── dist/
│   └── autoclicker.exe   # Hasil build aplikasi (setelah dikompilasi)
├── venv/                 # (Opsional) Virtual environment
└── README.md             # Dokumentasi proyek
```

---

## ⚙️ Instalasi & Menjalankan dari Source Code

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Farrassubahan/auto-clicker-python.git
cd auto-clicker-python
```

---

### 2️⃣ Buat Virtual Environment (opsional tapi disarankan)

```bash
python -m venv venv
```

Aktifkan:

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Semua Dependensi

```bash
pip install -r requirements.txt
```

📦 File `requirements.txt` sekarang berisi:

```
pyautogui
pillow
pygetwindow
pymsgbox
mouseinfo
pynput
```

---

### 4️⃣ Jalankan Aplikasi

```bash
python autoclicker.py
```

Jika berhasil, akan muncul tampilan GUI seperti berikut:

```
+------------------------------------------------+
|  Auto Clicker: Targeted Background Click 🖱️    |
|------------------------------------------------|
| Interval (detik): [ 0.1 ]                     |
| Nama Jendela Target: [ Roblox ]               |
| [Set Target Aktif] [Set Pos Relatif Mouse]    |
| Pos relatif: (default = tengah jendela)       |
| [Mulai] [Berhenti] [Keluar]                   |
| Status: Berhenti 🔴                           |
+------------------------------------------------+
```

---

## 🧱 Build Menjadi Aplikasi Windows (.exe)

### 🔹 Opsi 1 — Manual (via Terminal)

1️⃣ Install PyInstaller

```bash
pip install pyinstaller
```

2️⃣ Jalankan Build

```bash
pyinstaller --onefile --noconsole autoclicker.py
```

3️⃣ Hasilnya akan muncul di:

```
dist\autoclicker.exe
```

---

### 🔹 Opsi 2 — Otomatis (klik dua kali `build.bat`)

Isi `build.bat` sudah diatur agar otomatis menginstal semua library & build versi terbaru:

```bat
@echo off
title 🔧 Build Auto Clicker

echo Mengecek dan menginstal dependensi...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Membangun file .exe...
pyinstaller --onefile --noconsole autoclicker.py

echo.
echo ✅ Selesai! Cek folder dist\autoclicker.exe
pause
```

💡 Kamu cukup klik dua kali file `build.bat`, dan `.exe` akan langsung dibuat ulang otomatis.

---

## 💻 Cara Menggunakan

1️⃣ Jalankan `autoclicker.exe` atau `python autoclicker.py`
2️⃣ Masukkan nama jendela target (misal: **Roblox**)
3️⃣ Tentukan interval klik (misal: `0.1` detik = 10 klik per detik)
4️⃣ (Opsional) Gunakan **Set Target dari Jendela Aktif** untuk memilih window saat ini
5️⃣ (Opsional) Gunakan **Set Pos Relatif dari Pos Mouse** agar klik diarahkan ke titik tertentu dalam jendela
6️⃣ Tekan **Mulai** → klik otomatis berjalan di jendela target
7️⃣ Jika **kursor bergerak**, auto-click akan **pause otomatis**. Setelah kursor **diam 1 detik**, auto-click akan **aktif kembali** 🔄
8️⃣ Kamu bebas berpindah ke aplikasi lain tanpa mengganggu auto-click
9️⃣ Tekan **Berhenti** untuk menghentikan, atau **Keluar** untuk menutup aplikasi

---

## ⚠️ Catatan Penting

⚠️ Jangan minimize jendela target — biarkan tetap terbuka di background.
⚠️ Hindari penggunaan auto-clicker untuk tindakan ilegal atau curang di game online.
⚠️ Program ini dibuat untuk **tujuan belajar, eksperimen, dan efisiensi pekerjaan**.

---

## 🧰 Masalah Umum

| Masalah                          | Penyebab                                     | Solusi                                           |
| -------------------------------- | -------------------------------------------- | ------------------------------------------------ |
| `ModuleNotFoundError: pyautogui` | Library belum diinstal                       | Jalankan `pip install -r requirements.txt`       |
| `.exe` tidak bisa dibuka         | Antivirus memblokir                          | Tambahkan ke “Allowed apps” di Windows Defender  |
| Klik tidak jalan di game         | Game menolak input non-fokus                 | Jalankan mode windowed dan pastikan target benar |
| Aplikasi menutup setelah build   | Hilangkan `--noconsole` jika ingin lihat log | Gunakan `pyinstaller --onefile autoclicker.py`   |

---

## 📜 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
Kamu bebas memodifikasi dan menyebarkan dengan tetap mencantumkan kredit kepada pengembang asli.

---

## 👨‍💻 Dibuat oleh

**Farras**
💼 [GitHub](https://github.com/Farrassubahan)
💬 *"Klik kecil untuk pekerjaan besar — otomasi itu seni."*
