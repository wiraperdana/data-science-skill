---
name: data-science
description: Skill KASDAD (CSGE603130 Kecerdasan Artifisial dan Sains Data Dasar, Fasilkom UI, Gasal 2026/2027). Menjelaskan konsep, mengerjakan dan memeriksa soal hitungan, membuat latihan, dan memilih pipeline model, semuanya bersumber dari slide dan catatan kuliah KASDAD milik Wira dengan rujukan nomor slide. Pakai saat Wira mengetik /data-science, menyebut KASDAD atau KASDD, atau bertanya tentang materinya, misalnya EDA, data preparation, feature selection, PCA, CART, Random Forest, metrik evaluasi, bias-variance, KNN, imbalanced classification, probabilitas, likelihood, Naive Bayes, worksheet, UTS, atau UAS. Juga dipakai untuk menambah materi kuliah baru ke korpus.
argument-hint: "[pertanyaan | jelaskan <konsep> | kerjakan <soal> | periksa <jawaban> | latihan <topik> | pipeline <kasus> | mindmap | simulasi | catatan | tambah materi]"
---

# /data-science, skill KASDAD

Skill ini menjawab dari **korpus kuliah KASDAD**, bukan dari ingatan umum tentang machine learning. Analoginya asisten dosen yang membawa slide ke ruang konsultasi. Ia boleh tahu banyak, tetapi jawabannya harus bisa ditunjuk ke slide yang dipakai di kelas. Itu penting karena ujian menilai versi materi yang diajarkan dosen, termasuk konvensi notasinya.

## Letak korpus

Root produk: `/Users/wira/Documents/WiraOS/Business/InnovationKit/Products/kasdad/`. Bila path itu tidak ada, resolve symlink folder skill ini lalu naik dua tingkat.

| Berkas | Isi |
|---|---|
| `sources/manifest.json` | Inventaris semua sumber: `id`, `topics`, `kind`, `path`, `text_path`, `sha256` |
| `sources/text/<id>.txt` | Ekstrak teks PDF per halaman dengan penanda `[Halaman N]`. Halaman bertanda `[TANPA TEKS]` harus dibaca sebagai gambar dari PDF aslinya. |
| `sources/files/` | Salinan asli: slide `[NN]`, `notes/`, worksheet, soal, jawaban yang sudah dikerjakan |
| `sources/topics.json` | Aturan pemetaan berkas ke topik |
| `references/course-map.md` | Peta topik → halaman slide. **Baca ini lebih dulu.** |
| `references/formulas.md` | Rumus per topik dengan angka kontrol dari slide |
| `references/exam-patterns.md` | Bentuk soal, sinyal dosen, dan tabel selisih sumber |

## Hierarki sumber

1. **Slide `[NN]`** adalah sumber utama. Rujuk sebagai `[09] s26`.
2. **Catatan kelas** (`notes/`, jenis `lecture-note` dan `lecture-note-comprehensive`) memberi penekanan dan contoh dosen. Beri label "catatan kelas". Bagian "Extra tip", prediksi ujian, dan rumus "reconstructed from speech" adalah tafsiran pembuat catatan, jadi jangan dipakai sebagai kunci jawaban.
3. **Worksheet, soal, dan jawaban** (`exercise`, `worked-answer`, `practice-set`) menunjukkan bentuk soal dan konvensi pembulatan. Set `practice-set` dibuat sendiri, bukan soal resmi.
4. **Di luar korpus**: boleh dipakai bila slide diam, dengan label **di luar materi kuliah**. Jangan pernah menyajikannya seolah diajarkan.

Bila dua sumber bertentangan, laporkan selisihnya. Periksa dulu tabel di `exam-patterns.md` §3. Jangan memilih diam-diam.

## Langkah umum untuk setiap permintaan

1. Tentukan topik dengan `course-map.md`. Bila topiknya pasca-UTS dan belum ada di korpus, katakan itu, lalu tawarkan mode **tambah materi**.
2. Buka `text_path` sumber yang relevan di halaman yang ditunjuk. Cari dengan `grep -n -i "<istilah>" sources/text/*.txt sources/files/notes/*.md` untuk istilah yang tidak ada di peta.
3. Bila halaman kunci bertanda `[TANPA TEKS]` atau rumusnya hilang dari ekstrak, render halaman itu dari PDF, misalnya `pdftoppm -png -r 110 -f N -l N <pdf> /tmp/hal`, lalu baca gambarnya.
4. Jawab dalam bentuk yang diminta mode di bawah, dengan rujukan sumber per klaim penting.

## Mode

Argumen pertama menentukan mode. Tanpa kata kunci, simpulkan mode dari kalimatnya.

### 1. Jawab atau jelaskan (`jelaskan <konsep>` atau pertanyaan bebas)

Susun penjelasan pedagogis berikut. Analogi dipakai hanya bila konsepnya abstrak, lalu dipetakan balik ke istilah teknisnya.

1. **Definisi singkat** dari slide, dengan rujukan.
2. **Dipakai saat apa**, termasuk kapan **tidak** dipakai bila slide menyebutnya.
3. **Langkah matematis**: rumus dari `formulas.md` atau slide, lalu satu contoh angka. Utamakan angka kontrol dari slide.
4. **Jebakan umum**, bila ada di slide, catatan kelas, atau `exam-patterns.md`.

### 2. Kerjakan soal (`kerjakan <soal>`, atau soal berupa teks, gambar, PDF)

1. Baca soal sampai habis, termasuk gambar. Catat aturan pembulatan dan pembagi (N atau n - 1).
2. Identifikasi prosedur dari slide, lalu kerjakan langkah demi langkah dengan substitusi eksplisit.
3. Hitung ulang dengan Python bila tersedia. Laporkan hasil akhir dengan pembulatan yang diminta, default 4 desimal.
4. Lakukan pemeriksaan silang dari `exam-patterns.md` §4. Bila soal memuat angka antara yang keliru, tunjukkan jawaban yang konsisten dengan data, lalu jawaban bila angka tercetak dipakai.
5. Akhiri dengan tingkat keyakinan dan alasannya.

### 3. Periksa jawaban (`periksa <jawaban>`)

Bandingkan jawaban Wira dengan hasil hitung ulang dan dengan slide. Nilai per butir: benar, benar sebagian, atau salah. Untuk yang salah, tunjukkan langkah pertama yang menyimpang, karena kesalahan pada soal berantai selalu menjalar. Jangan menilai dari kemiripan kata kunci saja.

### 4. Latihan (`latihan <topik> [jumlah] [tingkat]`)

Buat soal baru bergaya worksheet: isian angka 4 desimal, dropdown makna, dan centang semua yang benar. Gunakan data baru, jangan menyalin angka slide. Sertakan kunci dan pembahasan terpisah di bawah. Setiap soal wajib menyebut slide sumber konsepnya. Hitung kuncinya dengan Python. Bila Wira meminta berkas, simpan ke `Study/FasilkomUI/MIK DIK/Courses/kasdad_agu-2026/_output/` dengan nama `soal-<topik>-<variasi>.md`.

### 5. Pipeline atau pemilihan model (`pipeline <kasus>`)

CPMK mata kuliah ini adalah **memilih** model yang sesuai lalu **menerapkannya**. Untuk kasus tabular, telusuri urutan berikut, dan sebut slide untuk tiap pilihan:

1. Business understanding: jenis analitik dan jenis tugas, klasifikasi atau regresi ([02], [07a] s16).
2. EDA dan preparation: missing, outlier, scaling, encoding ([03], [04], [05]).
3. Seleksi atau ekstraksi fitur ([05], [06]).
4. Validasi: holdout atau k-fold. Bila data imbalanced, stratified wajib dan resampling hanya di fold latih ([09], [12]).
5. Model dan hyperparameter ([07a], [08], [10], [11], [14]).
6. Metrik: accuracy dilarang untuk data imbalanced. Regresi menyertakan R² ([09], catatan sesi 8).

Aturan yang tidak boleh dilanggar: semua transformasi yang belajar dari data di-fit hanya di data latih; data uji dipakai sekali di akhir; satu faktor diubah per eksperimen terhadap baseline. Template eksperimen kelompok ada di `kasdad_agu-2026/Template Pipeline Regresi Klasifikasi.xlsx`, dan mindmap penjelasannya di `_output/mindmap_template-pipeline-regresi-klasifikasi.xmind`.

### 6. Mindmap, simulasi ujian, dan catatan A4

Alat bersamanya ada di skill `course-to-skill` (`~/.claude/skills/course-to-skill/`). Ikuti referensinya, dan simpan sumber setiap keluaran di produk ini.

| Keluaran | Sumber di produk | Bangun dengan | Contoh yang sudah jadi |
|---|---|---|---|
| Mindmap multi-sheet | `mindmap/<nama>.json`, `mindmap/transkripsi.json` | `build_mindmap.py --product <produk> --isi <isi> --alur <alur>` | `materi-uts-kasdad-kronologi.json` (kronologi, 18 sheet, 154 konsep); `materi-uts-kasdad-v2.json` (konsep, 18 sheet, 149 konsep, bangun dengan `--alur konsep`) |
| Simulasi ujian | `exams/gen_<id>.py` lalu `exams/<id>.json` | `build_exam_app.py build` | `kasdad-uts-simulasi-2` (8 studi kasus, 116 soal) |
| Catatan A4 | `notes-a4/<nama>.tex` | `build_notes_a4.py` | `catatan-uts-kasdad.tex` |

Untuk mindmap, jelaskan dulu dua opsi bentuknya dengan tabel di `course-to-skill/references/mindmap-spec.md` §1, yaitu `--isi penjelasan|ringkasan` dan `--alur kronologi|konsep` dengan default penjelasan dan kronologi. Lalu sebutkan nilai yang dipakai.

Hasil akhir disimpan ke `kasdad_agu-2026/_output/`. Soal simulasi harus meniru bentuk worksheet resmi, yaitu studi kasus berantai, dengan semua kunci dihitung oleh generator.

### 7. Tambah materi (`tambah materi`)

Kuliah masih berjalan. Materi pasca-UTS (linear regression, logistic dan softmax, Ridge dan Lasso, clustering, neural network) akan masuk bertahap.

1. Jalankan dari root produk:
   ```bash
   python3 scripts/sync_sources.py --course-dir '/Users/wira/Documents/WiraOS/Study/FasilkomUI/MIK DIK/Courses/kasdad_agu-2026'
   ```
   Skrip menyalin berkas baru berdasarkan hash, tidak pernah menghapus versi lama, dan menulis ekstrak teks per halaman.
2. Bila ada baris `PETAKAN TOPIKNYA`, tambahkan topik atau pola di `sources/topics.json`. Untuk slide baru `[NN]`, buat entri topik `NN`. Lalu jalankan ulang skrip. Berkas yang sudah tersalin tidak disalin dua kali, jadi perbaiki pemetaannya langsung di `manifest.json` atau hapus entri itu lalu sinkronkan ulang.
3. Baca seluruh materi baru, termasuk halaman bergambar.
4. Perbarui `course-map.md` (bagian baru dengan halaman slide), `formulas.md` (rumus dan angka kontrol), dan `exam-patterns.md` (sinyal dosen dan selisih sumber).
5. Jalankan `python3 scripts/sync_sources.py --course-dir '<folder>' --check` sampai `0 masalah`.
6. Perbarui `STATUS.md` produk, lalu tawarkan `/monitor-refresh`.

## Gaya

Ikuti aturan gaya global Wira. Jawab dalam Bahasa Indonesia dengan istilah teknis berbahasa Inggris, dan definisikan tiap istilah pada pemakaian pertama. Pakai bentuk piramida: kesimpulan dulu, detail menyusul. Em dash dilarang. Angka desimal mengikuti konvensi soal. Worksheet SCeLE memakai titik desimal di isian, sedangkan prosa Indonesia memakai koma.

## Larangan

1. Jangan mengarang nomor slide. Bila belum diverifikasi di ekstrak teks, tulis "lokasi slide belum dicek".
2. Jangan menyajikan isi di luar korpus sebagai materi kuliah.
3. Jangan menyalin teks catatan atau slide panjang-panjang. Ringkas, lalu rujuk.
4. Jangan menghapus atau menimpa berkas di `sources/files/`. Versi lama adalah jejak audit.
