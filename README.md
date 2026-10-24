# TA-03: Data-Driven Monte Carlo Simulation

## Judul Proyek
Simulasi Monte Carlo untuk Estimasi Risiko Keterlambatan Pengiriman

## Deskripsi
Proyek ini menerapkan metode Monte Carlo menggunakan data historis durasi pengiriman untuk memperkirakan probabilitas keterlambatan.

Aplikasi dikembangkan menggunakan Python dan Flask serta menyediakan dashboard interaktif untuk menjalankan simulasi dan menampilkan visualisasi hasil.

## Tujuan
1. Mengidentifikasi karakteristik statistik durasi pengiriman.
2. Menjalankan simulasi Monte Carlo berdasarkan data historis.
3. Mengestimasi probabilitas keterlambatan pengiriman.
4. Menyajikan hasil simulasi dalam bentuk statistik dan histogram.

## Metode
- Data cleaning menggunakan Pandas.
- Analisis statistik deskriptif.
- Simulasi Monte Carlo menggunakan NumPy.
- Visualisasi menggunakan Matplotlib.
- Implementasi aplikasi web menggunakan Flask.

## Parameter Simulasi
- Variabel acak: durasi pengiriman.
- Batas keterlambatan awal: 60 menit.
- Jumlah simulasi awal: 10.000 iterasi.
- Metode sampling: pengambilan sampel acak dengan pengembalian dari data historis.

## Teknologi
- Python
- Flask
- Pandas
- NumPy
- Matplotlib
- HTML
- CSS
- JavaScript

## Cara Menjalankan
1. Instal dependensi dengan `pip install -r requirements.txt`.
2. Pastikan dataset tersedia pada folder `data`.
3. Jalankan `python app.py`.
4. Buka `http://127.0.0.1:5000` di browser.

## Hasil
Hasil simulasi digunakan untuk memperkirakan probabilitas keterlambatan berdasarkan batas durasi yang ditentukan pengguna.

Nilai akhir mengikuti dataset dan konfigurasi simulasi yang dijalankan.

## Catatan
Hasil simulasi merupakan estimasi berdasarkan data historis dan bukan jaminan terhadap kondisi pengiriman pada masa mendatang.# TA-03-PDS
