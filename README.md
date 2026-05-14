# Deteksi Penyakit Tomat

Proyek ini adalah implementasi sistem deteksi penyakit pada tanaman tomat menggunakan teknik pengolahan citra dan machine learning. Sistem ini dapat mengklasifikasikan citra daun tomat ke dalam empat kategori: sehat (healthy), late blight, leaf mold, dan TYLCV (Tomato Yellow Leaf Curl Virus).

## Struktur Proyek

```
Deteksi-Penyakit-Tomat/
├── dataset/                  # Folder utama dataset dari Kaggle
│   ├── raw/                  # Citra asli (200 gambar) dibagi per kelas
│   │   ├── late_blight/      # 50 gambar (Tugas Ratu)
│   │   ├── leaf_mold/        # 50 gambar (Tugas Ratu)
│   │   ├── tylcv/            # 50 gambar (Tugas Najwa)
│   │   └── healthy/          # 50 gambar (Tugas Najwa)
│   └── processed/            # Hasil setelah preprocessing Fase 2
├── notebooks/                # File .ipynb untuk eksperimen/EDA
│   └── eda_visual.ipynb      # Analisis awal (Tugas Disa)
├── src/                      # Source code utama (.py)
│   ├── __init__.py           # Membuat folder src menjadi module
│   ├── loader.py             # Script pembacaan dataset (Tugas Darent)
│   ├── preprocessing.py      # Fungsi resize, filter, segmentasi (Fase 2)
│   ├── feature_extraction.py # Fungsi uLBP dan HSV (Fase 3)
│   └── classifier.py         # Logika KNN (Fase 4)
├── main.py                   # Entry point (Skrip utama yang dijalankan)
├── requirements.txt          # Daftar library (OpenCV, Scikit-learn, dll)
├── README.md                 # Dokumentasi singkat proyek
└── .gitignore                # Mengabaikan file yang tidak perlu (seperti .pyc atau venv)
```

## Fitur Utama

- **Preprocessing**: Resize, filter, dan segmentasi citra untuk meningkatkan kualitas data.
- **Feature Extraction**: Ekstraksi fitur menggunakan uLBP (Uniform Local Binary Patterns) dan HSV (Hue, Saturation, Value).
- **Klasifikasi**: Menggunakan algoritma K-Nearest Neighbors (KNN) untuk klasifikasi penyakit.
- **Dataset**: Dataset terdiri dari 200 gambar citra daun tomat, dibagi menjadi 4 kelas.

## Instalasi

1. Clone repositori ini:
   ```
   git clone <url-repositori>
   cd Deteksi-Penyakit-Tomat
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Cara Menjalankan

Jalankan skrip utama:
```
python main.py
```

## Kontribusi

- **Ratu**: Dataset raw untuk late_blight dan leaf_mold, serta bagian preprocessing.
- **Najwa**: Dataset raw untuk tylcv dan healthy.
- **Disa**: Analisis awal dan EDA di notebook.
- **Darent**: Script loader untuk pembacaan dataset.

## Lisensi

Proyek ini untuk tujuan edukasi dan akademik.