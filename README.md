# 🥔 AkuKentang: Sistem Klasifikasi Penyakit Kentang Berbasis AI

AkuKentang adalah platform berbasis web yang dikembangkan untuk melakukan klasifikasi penyakit pada kentang.

---

## 📂 Dataset & Preprocessing

### 1. Dataset
Dataset yang digunakan adalah **Potato Disease Recognition Dataset** yang digabungkan dari citra asli (*Original*) dan citra yang telah diaugmentasi (*Augmented*). Dataset ini mencakup 5 kelas penyakit:
- **Blackspot Bruising Disease**: Memar hitam pada jaringan kentang.
- **Healthy Potato**: Kondisi tanaman/umbi sehat.
- **Potato Brown Rot Disease**: Pembusukan coklat akibat bakteri.
- **Potato Dry Rot Disease**: Pembusukan kering akibat jamur.
- **Potato Soft Rot Disease**: Pembusukan lunak yang membuat tekstur berair.

### 2. Preprocessing
Setiap model memiliki kebutuhan pengolahan data yang spesifik sebelum masuk ke tahap pelatihan:
- **CNN Custom**: Rescaling pixel menjadi rentang `[0, 1]` dengan input size `256x256`.
- **MobileNetV2**: Normalisasi pixel menjadi rentang `[-1, 1]` menggunakan fungsi `preprocess_input` bawaan dengan input size `224x224`.
- **ResNet50**: Konversi kanal warna dari RGB ke BGR serta melakukan *zero-centering* (pengurangan rata-rata pixel ImageNet) dengan input size `224x224`.

---

## 🤖 Penjelasan Model Deep Learning

Proyek ini menerapkan pendekatan **Transfer Learning** pada dua model pretrained dan satu model arsitektur mandiri:

| **CNN** | Arsitektur Sequential dengan 3 blok Konvolusi (Conv2D + MaxPooling) dan layer Dense di akhir. | Ringan dan efisien untuk kasus klasifikasi sederhana |
| **MobileNetV2** | Menggunakan Depthwise Separable Convolutions untuk mengurangi jumlah parameter secara drastis. | Sangat cepat, ukuran file kecil, ideal untuk deployment web. |
| **ResNet50** | Arsitektur yang menggunakan *Residual/Skip Connections* untuk mengatasi vanishing gradient. | Akurasi sangat tinggi.|

---

## 📊 Hasil Evaluasi & Analisis Perbandingan

Berdasarkan hasil pengujian pada data validasi, berikut adalah ringkasan perbandingannya:

| Parameter             | CNN           | MobileNetV2    | ResNet50                         |
| :---                  | :---          | :---           | :---                             |
| **Akurasi Validasi**  | 78%           | 81%            | 98%                              |
| **Waktu Training**    | Cepat         | Sangat Cepat   | Cepat                            |
| **tipe fileModel**    | Sedang (.h5)  | Kecil (.keras) | Besar (.keras)                   |

**Analisis:** 
Resnet menjadi yang tercepat tapi meskipun memiliki akurasi tertinggi, ketika di lakukan tes pada tiap model, yang bisa memprediksi kentang sesuai penyakitnya adalah CNN, meskipun begitu, model masih bisa memprediksi penyakit namun tidak selalu akurat saja.

**CNN**
![alt text](screenshots/Akurasi%20CNN.png)

![alt text](screenshots/Grafik%20CNN.png)

**MobileNetV2**

![alt text](screenshots/Akurasi%20MobilenetV2.png)

![alt text](screenshots/confusion%20mobilenetv2.png)

**ResNet50**

![alt text](screenshots/Confusion%20matrix%20ResNet.png)

![alt text](screenshots/Akurasi%20ResNet50.png)
---

## 💻 Panduan Menjalankan Sistem Secara Lokal

1. Download seluruh file yang ada di repository github ini
2. setelah download/pull dari github, buka app.py
3. pada app.py, buka terminal dan jalankan streamlit run app.py / python -m streamlit run app.py.
4. jika semua file ada dan library sudah terinstall, tidak akan ada error saat menjalankan webnya

## Dataset
https://www.kaggle.com/datasets/sujaykapadnis/potato-disease-recognition-dataset?resource=download
