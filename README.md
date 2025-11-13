# 🕹️ Auto Clicker Python

Auto Clicker sederhana berbasis **Python + Tkinter + PyAutoGUI** yang dapat melakukan klik otomatis pada layar komputer dengan interval waktu yang bisa diatur.
Aplikasi ini dilengkapi antarmuka GUI yang ringan, mudah digunakan, dan bisa dikonversi menjadi aplikasi `.exe` agar dapat dijalankan tanpa membuka VS Code atau Python secara langsung.

---

## ✨ Fitur

* Klik otomatis dengan interval waktu yang dapat disesuaikan
* Tampilan GUI sederhana dan user-friendly
* Tombol **Mulai**, **Berhenti**, dan **Keluar**
* Indikator status (🟢 Berjalan / 🔴 Berhenti)
* Bisa dijalankan langsung sebagai **aplikasi Windows (.exe)**

---

## 📁 Struktur Project

```
coba-autoklik/
│
├── autoclicker.py        # Script utama aplikasi
├── requirements.txt      # Daftar library yang dibutuhkan
├── venv/                 # (Opsional) Virtual environment Python
├── dist/
│   └── autoclicker.exe   # Hasil build aplikasi (setelah dikompilasi)
└── README.md             # Dokumentasi proyek
```

---

## Instalasi (Menjalankan dari Kode Python)

### 1️⃣ Clone Repository

```bash
git clone https:/Farrassubahan/github.com/auto-clicker-python.git
cd auto-clicker-python
```

### 2️⃣ Buat Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Aktifkan Virtual Environment

**Terminal:**

```bash
venv\Scripts\activate
```

Jika berhasil, akan muncul tulisan `(venv)` di awal baris terminal.

---

### 4️⃣ Install Dependensi

Sekarang kamu tidak perlu mengetik semua library satu per satu.
Cukup jalankan:

```bash
pip install -r requirements.txt
```

📦 File `requirements.txt` berisi:

```
pyautogui
pillow
pygetwindow
pymsgbox
mouseinfo
```

---

### 5️⃣ Jalankan Program

```bash
python autoclicker.py
```

Akan muncul tampilan GUI seperti berikut:

```
+---------------------------+
|  Auto Clicker Python 🕹️  |
|---------------------------|
| Interval (detik): [0.1]  |
| [Mulai] [Berhenti]       |
| Status: Berhenti 🔴       |
| [Keluar]                 |
+---------------------------+
```

---

## 🧱 Build Menjadi Aplikasi (.exe)

> Langkah ini opsional — hanya jika ingin menjalankan tanpa membuka Python.

### 1️⃣ Install PyInstaller

```bash
pip install pyinstaller
```

### 2️⃣ Build Program

```bash
pyinstaller --onefile --noconsole autoclicker.py
```

### 3️⃣ Temukan Hasilnya

Setelah proses selesai, hasil build dapat ditemukan di:

```
dist/autoclicker.exe
```

Klik dua kali file tersebut untuk menjalankan aplikasinya seperti program Windows biasa ✅

---

## 🕹️ Cara Menggunakan

1. Jalankan program (`python autoclicker.py` atau `autoclicker.exe`)
2. Masukkan interval klik dalam **detik** (contoh: `0.1` untuk 10 klik per detik)
3. Tekan tombol **Mulai** → Auto-clicker akan mulai bekerja
4. Tekan tombol **Berhenti** untuk menghentikan klik otomatis
5. Tekan **Keluar** untuk menutup aplikasi

---

## ⚠️ Peringatan

* Gunakan dengan hati-hati! Auto-clicker dapat melakukan klik sangat cepat.
* Hindari menggunakannya pada area sensitif (seperti tombol hapus, pembelian online, dll).
* Program ini dibuat untuk tujuan **belajar dan eksperimen**.

---

## 📜 Lisensi

Project ini dilisensikan di bawah [MIT License](LICENSE).
Kamu bebas memodifikasi, menggunakan, dan membagikan ulang dengan tetap mencantumkan kredit ke pengembang asli.

---

## 💡 Kontribusi

Pull request sangat diterima!
Kalau kamu ingin menambahkan fitur baru (misalnya hotkey start/stop, custom target area, atau pengatur klik kanan/kiri), silakan fork repository ini dan kirim PR 🚀

---

## 👨‍💻 Dibuat oleh

**Farras**
💼 [GitHub](https://github.com/Farrassubahan)
💬 "Sederhana tapi berguna — karena klik berulang pun bisa diotomatisasi."
