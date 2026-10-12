# Pola penilaian, sinyal ujian, dan selisih sumber KASDAD

Dokumen ini berisi tiga hal. Pertama, bentuk soal yang sudah terlihat. Kedua, penekanan dosen yang tercatat di catatan kelas. Ketiga, tempat sumber saling bertentangan, karena justru di sana jawaban ujian paling mudah salah.

## 1. Bentuk soal yang sudah terlihat

**Worksheet SCeLE** (worksheet 1: PCA dan CART; worksheet 2: likelihood dan Naive Bayes). Bentuknya kuis Moodle dengan tiga jenis isian:

1. **Isian angka**, dibulatkan 4 angka di belakang koma. Untuk nilai sangat kecil, worksheet 2 meminta mantisa saja, misalnya 2,4197 untuk 2,4197 × 10⁻².
2. **Dropdown makna**, misalnya memilih arti P(A|B) atau memilih "zero-frequency problem".
3. **Centang semua yang benar**, berisi pernyataan konsep yang sebagian sengaja dibuat salah halus.

Rantai soal hitungan bersifat berurutan. Contohnya PCA: mean → centering → kovarians → eigen → explained variance → transformasi → rekonstruksi. Contoh lain CART: Gini root → Gini tiap fitur → root node → split rekursif. Kesalahan di awal menjalar ke semua nomor berikutnya. Karena itu, tunjukkan pemeriksaan antara, misalnya jumlah kolom terpusat = 0, trace = Σλ, dan eigenvector ortogonal.

**Contoh soal cetak**: `soal-pca.pdf` (PCA 3 variabel). Soal tercetak memuat dua elemen kovarians yang keliru. Jawaban yang benar memakai data mentah sebagai sumber kebenaran dan menyebut selisihnya.

**Latihan di slide**: [09] s45-49 (confusion matrix transaksi ilegal), [11a] (KNN one-hot + Manhattan, K=3 dan K=5), [12] s81-84 (stratified fold, convex combination, bobot 3 kelas, tiga model logistic regression), [14] s42 (Naive Bayes dua fitur).

**UTS** (30%) dan **UAS** (25%): format resmi belum tercatat di korpus. Catatan sesi 7 mengutip dosen: "Ujiannya kan model-model begitu", yaitu prosedur model dikerjakan langsung. Catatan Naive Bayes menyebut "ODS (Open Book/Open Notes)" pada pekan berikutnya. Kepanjangan ODS dan hubungannya dengan UTS tidak jelas dari transkrip, jadi jangan dianggap aturan UTS.

## 2. Sinyal dari dosen (catatan kelas)

| Topik | Yang ditekankan | Sumber |
|---|---|---|
| AI | empat paradigma definisi beserta kritiknya; agen cerdas; jenis learning | catatan sesi 1 |
| EDA, preparation | hitungan outlier RLB/RUB; pilihan normalisasi | catatan sesi 4 |
| PCA | kovarians, eigenvalue, eigenvector; latihan wajib; tugas reconstruction error | catatan sesi 6, 7 |
| CART | hyperparameter ditekankan berkali-kali; mencoba kombinasi hyperparameter | catatan sesi 8 |
| Evaluasi | K-fold sebagai prosedur standar; R² selalu disertakan untuk regresi; jangan uji di data latih, jangan tuning di data uji | catatan sesi 8 |
| KNN | beda hasil K=3 vs K=5; Manhattan dan Euclidean dengan angka; jarak kecil = dekat, similarity besar = dekat | catatan KNN |
| Imbalanced | stratified CV **wajib**; accuracy **dilarang**; resampling hanya di data latih; cost-sensitive dan sampling sebagai dua jalur utama | catatan Imbalance 1-3 |
| Probabilitas, NB | conditional probability sebagai fondasi; log-likelihood untuk mencegah underflow; prior dan class conditional density untuk fitur kategorikal | catatan NB dan Pembahasan Kuis |

Bagian "Extra tip", "prediksi ujian", dan rumus bertanda "reconstructed from speech" di catatan adalah tafsiran pembuat catatan. Jangan menjadikannya kunci jawaban tanpa dukungan slide.

## 3. Selisih sumber yang sudah diketahui

| Hal | Sumber A | Sumber B | Sikap |
|---|---|---|---|
| Pembagi kovarians | [06] s7: dibagi N | worksheet dan jawaban soal PCA: dibagi n - 1 | Ikuti instruksi soal. Bila tidak ada, sebutkan pilihan dan konsekuensinya. Eigenvector tidak berubah, eigenvalue berskala. |
| Langkah 1 PCA | [06] s24 menyebut standarisasi | [06] s26 hanya mengurangi mean | Jelaskan bahwa contoh slide hanya centering. Z-score penuh dipakai bila skala fitur berbeda. |
| Range | [03] s28: (max - min) + 1 unit | [03] s31: hasil 6 untuk 2..8 | Sebutkan keduanya. |
| Label contoh target encoding | [05] s16 menulis "Classification (Height)" | isinya rata-rata tinggi, yaitu kasus regresi | Labelnya tertukar. |
| Kovarians soal-pca.pdf | angka tercetak | data mentah | Data mentah yang benar. |
| Template pipeline menandai "luar slide" | template | ada di slide: mutual_info_regression [05] s54; R² [09] s19-21; G-mean [09] s27; Brier [09] s32; PR-AUC [09] s36; Multinomial/Categorical NB [14] s39-41 | Perlakukan sebagai materi slide. |
| Cakupan neural network | buku panduan MIK 2024: tidak mencakup | silabus Gasal 2026/2027: termasuk | Untuk ujian semester ini, silabus. |
| Kaiser criterion, scree plot, EFA | tidak ada di slide | catatan KNN (catatan kelas) | Beri label catatan kelas. |

Tambahkan baris baru setiap kali menemukan selisih. Jangan memilih diam-diam.

## 4. Kebiasaan menjawab yang aman untuk soal hitungan

1. Tulis rumus dari slide, lengkap dengan rujukan.
2. Substitusi angka secara eksplisit, lalu hitung dengan presisi penuh. Bulatkan hanya di akhir sesuai instruksi soal (default worksheet: 4 desimal).
3. Lakukan satu pemeriksaan silang. Contohnya: jumlah probabilitas posterior ternormalisasi = 1; Σλ = trace; |r| ≤ 1; Gini anak tertimbang ≤ Gini induk pada split terbaik.
4. Untuk pilihan "centang semua yang benar", nilai tiap butir satu per satu dengan alasan satu kalimat.
5. Hitung ulang angka dengan Python bila tersedia, lalu laporkan bahwa angka sudah diverifikasi.
