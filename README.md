# Antivirus_gui

Antivirus_gui adalah sebuah aplikasi antivirus sederhana berbasis Python yang menyediakan antarmuka grafis (GUI) untuk memindai dan menangani file berbahaya seperti virus dan malware. Alat ini menggunakan deteksi berbasis signature dan memungkinkan pengguna untuk memindai folder atau file, serta mengkarantina file yang mencurigakan.

## Fitur
- **Pemindaian Folder atau File**: Memindai file atau folder untuk mencari file berbahaya yang cocok dengan signature virus.
- **Karantina File**: File yang terdeteksi sebagai virus dapat dipindahkan ke folder karantina untuk tindakan lebih lanjut.
- **Log Aktivitas Pemindaian**: Hasil pemindaian dicatat dalam file log untuk memudahkan pemeriksaan lebih lanjut.
- **Antarmuka Pengguna (GUI)**: Pengguna dapat dengan mudah berinteraksi dengan aplikasi menggunakan antarmuka grafis berbasis Python.

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama yang digunakan untuk membangun aplikasi.
- **Tkinter / PyQt**: Untuk membangun antarmuka grafis pengguna (GUI).
- **JSON**: Untuk menyimpan dan mengelola database signature virus.
- **SHA256 / MD5**: Untuk mendeteksi file yang terinfeksi berdasarkan signature hash.

## Instalasi
### Prasyarat
Pastikan Python sudah terinstal di komputer Anda. Anda dapat mengunduh Python dari [situs resmi Python](https://www.python.org/downloads/).

### Langkah-langkah Instalasi
1. **Clone repository ini:**
   ```bash
   git clone https://github.com/Cyberblaze-id/Antivirus_gui.git
   cd Antivirus_gui
   ```

2. **Instalasi dependensi:**
   Sebelum menjalankan aplikasi, Anda perlu menginstal beberapa dependensi. Jalankan perintah berikut untuk menginstal pustaka Python yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```

   Jika tidak ada file `requirements.txt`, Anda dapat menginstal dependensi secara manual:
   ```bash
   pip install cryptography
   pip install tkinter
   ```

## Penggunaan
1. Jalankan aplikasi:
   ```bash
   python antivirus_gui.py
   ```

2. **Pilih file atau folder** yang ingin dipindai.
3. Aplikasi akan **memindai file** dan mencocokkannya dengan **signature virus** yang ada.
4. Jika ditemukan file berbahaya, Anda dapat memilih untuk **memindahkan file ke karantina** atau **menghapusnya**.
5. **Log hasil pemindaian** akan dicatat dalam file `scan_log.txt`.

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan lakukan fork dan kirim pull request. Pastikan untuk mengikuti pedoman kontribusi yang ada.

### Langkah-langkah Kontribusi:
1. Fork repository ini.
2. Buat cabang baru untuk fitur atau perbaikan yang ingin Anda tambahkan.
3. Kirim pull request dengan menjelaskan perubahan yang dilakukan.

## Lisensi
Proyek ini dilisensikan di bawah **MIT License** - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

---

## Catatan Tambahan
- Aplikasi ini masih dalam tahap pengembangan, sehingga beberapa fitur atau deteksi virus mungkin terbatas.
- Diperlukan pembaruan rutin untuk memperbarui database signature virus.

---

Terima kasih telah menggunakan dan berkontribusi pada **Antivirus_gui**!


