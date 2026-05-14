# Laporan Teknis: Deteksi Penyakit Tomat

## Pendahuluan

Proyek ini bertujuan untuk mengembangkan sistem deteksi penyakit pada tanaman tomat menggunakan teknik pengolahan citra dan machine learning. Sistem ini mengklasifikasikan citra daun tomat ke dalam empat kategori: sehat (healthy), late blight, leaf mold, dan TYLCV (Tomato Yellow Leaf Curl Virus). Dataset yang digunakan berasal dari Kaggle, terdiri dari 200 gambar citra daun tomat yang dibagi rata per kelas (50 gambar per kelas).

Proyek ini dibagi menjadi empat fase utama:
- **Fase 1**: Pengumpulan dan persiapan dataset.
- **Fase 2**: Preprocessing citra (resize, filter, segmentasi).
- **Fase 3**: Ekstraksi fitur menggunakan uLBP dan HSV.
- **Fase 4**: Klasifikasi menggunakan algoritma K-Nearest Neighbors (KNN).

## Metodologi

### Fase 1: Persiapan Dataset
Dataset awal terdiri dari citra asli yang disimpan di folder `dataset/raw/`, dibagi per kelas. Citra ini kemudian diproses untuk mempersiapkan data pelatihan dan pengujian.

### Fase 2: Preprocessing
Preprocessing dilakukan untuk meningkatkan kualitas citra sebelum ekstraksi fitur. Langkah-langkah meliputi:
- **Resize**: Menyamakan ukuran citra ke dimensi standar (misalnya 256x256 piksel).
- **Filter**: Aplikasi filter seperti Gaussian blur untuk mengurangi noise.
- **Segmentasi**: Pemisahan daun dari latar belakang menggunakan teknik thresholding atau edge detection.

Hasil preprocessing disimpan di `dataset/processed/`.

### Fase 3: Ekstraksi Fitur
Fitur diekstrak dari citra yang telah diproses menggunakan dua metode:
- **uLBP (Uniform Local Binary Patterns)**: Untuk mendeteksi pola tekstur lokal pada citra grayscale.
- **HSV (Hue, Saturation, Value)**: Untuk mengekstrak informasi warna dari citra.

Fitur-fitur ini digabungkan menjadi vektor fitur yang mewakili setiap citra.

### Fase 4: Klasifikasi
Algoritma KNN digunakan untuk klasifikasi berdasarkan vektor fitur. KNN membandingkan jarak Euclidean antara fitur citra baru dengan fitur citra pelatihan untuk menentukan kelas terdekat.

## Implementasi

### Struktur Kode
Kode utama berada di folder `src/`:
- `loader.py`: Membaca dan memuat dataset dari folder.
- `preprocessing.py`: Mengimplementasikan fungsi resize, filter, dan segmentasi.
- `feature_extraction.py`: Mengimplementasikan ekstraksi fitur uLBP dan HSV.
- `classifier.py`: Mengimplementasikan logika KNN.
- `__init__.py`: Membuat `src` sebagai modul Python.

Skrip utama `main.py` mengintegrasikan semua modul untuk menjalankan pipeline lengkap.

### Library yang Digunakan
- **OpenCV**: Untuk pengolahan citra (resize, filter, segmentasi).
- **Scikit-learn**: Untuk algoritma KNN dan evaluasi model.
- **NumPy**: Untuk manipulasi array dan perhitungan matematis.
- **Matplotlib/Seaborn**: Untuk visualisasi hasil (jika diperlukan).
- **Pandas**: Untuk manipulasi data tabular.

Daftar lengkap library tercantum di `requirements.txt`.

### Cara Menjalankan
1. Install dependencies: `pip install -r requirements.txt`
2. Jalankan skrip utama: `python main.py`

## Evaluasi

Evaluasi model dilakukan menggunakan metrik standar klasifikasi:
- **Akurasi**: Persentase prediksi yang benar.
- **Precision**: Proporsi prediksi positif yang benar.
- **Recall**: Proporsi kasus positif yang terdeteksi.
- **F1-Score**: Rata-rata harmonik precision dan recall.

Dataset dibagi menjadi data pelatihan (80%) dan pengujian (20%) menggunakan stratified split untuk memastikan distribusi kelas seimbang. Cross-validation dapat digunakan untuk validasi lebih lanjut.

## Kesimpulan

Sistem deteksi penyakit tomat ini menyediakan solusi otomatis untuk identifikasi penyakit berdasarkan citra daun. Dengan kombinasi preprocessing, ekstraksi fitur, dan KNN, sistem ini dapat membantu petani dalam diagnosis dini. Pengembangan selanjutnya dapat melibatkan penggunaan model deep learning seperti CNN untuk akurasi yang lebih tinggi, atau penambahan lebih banyak data untuk generalisasi yang lebih baik.

Untuk pertanyaan atau modifikasi, silakan hubungi tim pengembang.