# Evaluasi Kelayakan Beasiswa Menggunakan Logika Fuzzy

## Deskripsi Proyek
Proyek ini bertujuan untuk mengevaluasi kelayakan siswa untuk mendapatkan beasiswa berdasarkan beberapa faktor, seperti nilai rata-rata siswa, prestasi akademis, dan pendapatan orang tua. Penggunaan logika fuzzy memungkinkan penanganan data yang tidak pasti atau ambigu, yang sesuai dengan sifat relatif dan tidak biner dari penilaian kelayakan beasiswa.

## Langkah-langkah Proyek

### 1. Persiapan Data
- Data nilai rata-rata, prestasi, dan pendapatan orang tua siswa dibaca dari file Excel.
- Pastikan data telah terdefinisi dengan baik dan lengkap.

### 2. Pemrosesan Data
- Definisikan variabel input (nilai rata-rata, prestasi, pendapatan orang tua) dan output (kelayakan) beserta fungsi keanggotaannya.
- Buat aturan fuzzy berdasarkan kombinasi nilai variabel input untuk menentukan nilai output kelayakan.

### 3. Evaluasi Menggunakan Logika Fuzzy
- Gunakan kontrol sistem fuzzy untuk mengatur aturan-aturan fuzzy yang telah dibuat.
- Lakukan fuzzy inference untuk menghasilkan nilai kelayakan beasiswa berdasarkan data input siswa.

### 4. Penyimpanan Hasil
- Simpan nilai kelayakan beasiswa dan keterangan kelayakan (rendah, sedang, atau tinggi) untuk setiap siswa.
- Hasil evaluasi disimpan dalam file Excel untuk referensi dan analisis lebih lanjut.

## Cara Menjalankan Proyek
1. Pastikan Python telah terinstal di komputer Anda.
2. Unduh file Excel dengan data nilai rata-rata, prestasi, dan pendapatan orang tua siswa.
3. Jalankan kode Python untuk membaca data, menghitung kelayakan, dan menyimpan hasil evaluasi ke file Excel.
4. Instal library skfuzzy menggunakan pip dengan menjalankan perintah berikut di terminal atau command prompt:
   ## Instalasi Library yang Diperlukan
Pastikan Anda telah menginstal library yang diperlukan sebelum menjalankan proyek ini. Anda dapat menginstalnya menggunakan pip. Jalankan perintah berikut di terminal atau command prompt:
```bash
pip install pandas

pip install numpy

pip install scikit-fuzzy

