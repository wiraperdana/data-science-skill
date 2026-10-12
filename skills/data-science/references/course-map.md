# Peta materi KASDAD (CSGE603130), Gasal 2026/2027

Peta ini menunjuk **di mana** sebuah konsep diajarkan. Isinya bukan pengganti sumber. Sebelum menjawab klaim yang spesifik mata kuliah, buka ekstrak teks slide di `sources/text/` (cari lewat `sources/manifest.json`) pada halaman yang disebut di sini.

Konvensi rujukan: `[05] s39` berarti slide [05] halaman PDF 39. Nomor halaman PDF sama dengan nomor slide di pojok kanan bawah. "Catatan sesi N" menunjuk berkas di `notes/` dan selalu diberi label **catatan kelas**.

Status per 11 Oktober 2026: slide [00] sampai [14] sudah masuk. Itu cakupan UTS (12 sampai 21 Oktober 2026). Materi pasca-UTS belum terbit, lihat bagian terakhir.

## [00] Course info dan silabus

- Komponen nilai: worksheet 10%, lab 4%, TP 6+6+4%, presentasi akhir 10%, UTS 30%, UAS 25%, partisipasi 5% (silabus).
- Worksheet dikerjakan individu dalam satu hari. TP berkelompok maksimal 4 orang, tetapi demo individu.
- Silabus menyatakan neural network **termasuk** cakupan, bertentangan dengan buku panduan MIK 2024. Untuk cakupan ujian, silabus yang dipakai.

## [01] What is AI

- s11-16: empat paradigma definisi AI: thinking humanly (cognitive modeling), acting humanly (Turing test), thinking rationally (laws of thought), acting rationally (agen rasional). Tiap paradigma punya kritik.
- s17-29: agen cerdas: percept, percept sequence, agent function f: P* → A, agent program, performance measure, PEAS (contoh taksi), sifat lingkungan (fully/partially observable, single/multi-agent, deterministic/stochastic, episodic/sequential, static/dynamic, discrete/continuous, known/unknown), tabel catur dan taksi.
- s30-37: sejarah singkat, taksonomi dan cabang AI, AGI.
- s38-47: konsep dasar pemelajaran mesin: supervised, unsupervised, reinforcement, klasifikasi vs regresi.
- Catatan sesi 1 (catatan kelas): dosen menekankan empat paradigma beserta kritiknya, agen cerdas, dan beda jenis learning.

## [02] What is Data Science

- s5-9: motivasi, learning agent, Big Data (volume, velocity, variety, veracity, value, variability).
- s11-18: definisi sains data; descriptive, diagnostic, predictive, prescriptive analytics; peran data engineer, data scientist, business stakeholder; siklus training dan inference; penyebab kegagalan proyek AI/DS.
- s20-24: metodologi: KDD, IBM flowchart, Microsoft lifecycle, SKKNI Kepmenaker 299/2020, CRISP-DM. Business understanding memilih pendekatan analitik dari tujuan.
- s26-41: studi kasus (pankreatitis akut dan lainnya), deployment, AI-enhanced humans.
- s43-50: Data Reimagined, studi kasus "Bodies as Data" pada dataset tabular Human Body Measurement.

## [03] Data collection, EDA, statistik deskriptif, visualisasi

- s7-15: data primer vs sekunder, open data, data media sosial, format (CSV, TSV, XML, JSON), tantangan pengumpulan data.
- s17-19: EDA (Tukey 1977), alasan EDA.
- s21: tipe data: kategorikal vs numerik; nominal, ordinal, interval, rasio.
- s22-26: mean (populasi μ, sampel x̄), sifat mean, median (posisi (n+1)/2), mode.
- s27-34: range, IQR, Q1/Q2/Q3, outlier RLB = Q1 - 1,5 IQR dan RUB = Q3 + 1,5 IQR, boxplot, variance dan standard deviation.
- s35-38: skewness Σ(x - x̄)³/(n s³), kurtosis Σ(x - x̄)⁴/(n s⁴), normal = 3, platykurtic < 3 < leptokurtic.
- s39-40: Pearson correlation r di [-1, 1].
- s41: catatan koder: underflow, overflow, presisi floating point.
- s43-81: visualisasi: line, area, histogram (jumlah bin), density, bar, pie (kritik), box, scatter, heatmap, tree map, waffle, word cloud, bubble, tiga poin membangun visual.
- Catatan sesi 3 dan 4 (catatan kelas): soal hitungan RLB/RUB disebut berpotensi keluar.

## [04] Data preparation

- s5-10: dirty data, GIGO, masalah data survei (respons parsial, tidak memenuhi kriteria, ngebut, straight-line, tidak realistis, kontradiktif).
- s12-14: data munging/wrangling, contoh resep jadi tabel.
- s15-21: missing data: tanya pengumpul data, drop, replace (mean, mode, konstanta, nearest neighbor, fungsi lain), biarkan.
- s22-25: noisy data dan penanganannya (regresi, clustering, inspeksi manusia+komputer), inconsistent data dan data formatting.
- s27-31: data integration: schema integration, entity identification, konflik nilai, redundansi lewat Pearson r dan Chi-square.
- s33-35: data transformation: smoothing, aggregation, generalization, normalization (simple feature scaling, min-max, z-score), feature construction.
- s37-41: data reduction, data selection (kolom/baris), data cube aggregation, kompresi.
- s43-44: discretization lewat binning equal-frequency dan smoothing by bin means/median/boundaries.
- s46-58: contoh wine consumption: imputasi mean 185, koreksi -0,8, integrasi data India (rata-rata 2,95), outlier digit berlebih, reduksi pembulatan, diskretisasi 4 kategori.

## [05] Feature engineering dan feature selection

- s2-7: fitur; feature engineering; tiga proses: feature creation (domain, data-driven, synthetic), transformation (normalization, scaling, encoding, log/akar), extraction (PCA, t-SNE, feature combination, aggregation).
- s8-29: aggregation, differences and ratios, age encoding, indicator encoding, one-hot, target encoding (termasuk weighted mean dengan n dan m, s17), label/ordinal, frequency encoding, binarization, binning numerik dan kategorikal, min-max dan simple feature scaling dengan contoh Expenses, Bag of Words.
- s31-35: curse of dimensionality (Hughes phenomenon), tujuan feature selection.
- s36-54: filter: missing value ratio, variance threshold, korelasi (fitur-target, antar fitur), Chi-square (Titanic, χ² Sex = 327,7, s42-45), information gain (H = 0,94, Gain age = 0,2465, s46-53), fungsi sklearn (chi2, f_classif, f_regression, r_regression, mutual_info_classif, mutual_info_regression, s54).
- s55-61: wrapper: SFS, SBS, contoh 4 fitur, SequentialFeatureSelector sklearn, SFFS (plus-l take-away-r), exhaustive. RFE hanya disebut namanya di s55.
- s62-64: embedded: decision tree, Lasso (bobot 0 berarti fitur tereliminasi).
- Catatan sesi 5 (catatan kelas): contoh Lasso Y = 0,5X1 + 7X2 + 0·X4 + 5.

## [06] Dimensionality reduction dan PCA

- s2-4: curse of dimensionality, tujuan reduksi dimensi.
- s7-18: review: covariance matrix, basis dan dimensi, koordinat relatif, transformasi linear, eigenvalue/eigenvector (Av = λv), diagonalisasi P⁻¹AP = D.
- s24: lima langkah PCA: standarisasi, matriks kovarian, eigen, urutkan, vektor fitur baru.
- s25-38: contoh 2 variabel (mean 1,81 dan 1,91; λ1 = 1,284, λ2 = 0,049; data pertama (0,69, 0,49) jadi (-0,828, -0,175)); kembali ke data awal; reduksi dengan membuang eigenvector λ terkecil.
- s40: explained variance EV_k = λk / Σλ.
- s41-45: intuisi: kovarian jadi diagonal, fitur jadi tidak berkorelasi, translasi lalu rotasi.
- s46-50: eigenfaces, 1850 dimensi jadi 150, EV 0,955.
- s51-53: metode lain: SVD, t-SNE, UMAP.
- Catatan sesi 6 dan 7 (catatan kelas): latihan PCA, tugas reconstruction error. Catatan KNN menyebut Kaiser criterion, scree plot, dan EFA. Ketiganya **tidak ada di slide**, jadi beri label catatan kelas.

## [07a] CART

- s5-17: learning problem (T, P, E), supervised, unsupervised, semi-supervised, reinforcement, hipotesis h ≈ f.
- s19-27: struktur tree, algoritma CART (binary split, cost tertimbang, argmin), cost klasifikasi Gini = 1 - Σp² atau entropy, cost regresi MSE, cara memilih split point (midpoint), greedy.
- s29-45: contoh Ice Age. Root dipilih dari popcorn 0,405, minuman soda 0,214, dan umur 0,343 (terbaik umur di t=15 atau 44), jadi root = Suka Minuman Soda (s39). Cabang soda=Iya lalu di-split dengan umur ≤ 12,5, kedua anak pure (s43).
- s48-54: regression tree (contoh nilai ujian: Nonton Video 174,636 vs Lab Lengkap 90,97, jadi root = Lab Lengkap, s50-52; daun = rata-rata).
- s55-59: tree besar dan dalam, parameter vs hyperparameter, hyperparameter CART (max_depth, min_samples_split, min_samples_leaf, max_features, max_leaf_nodes).
- s61-64: isu missing value (surrogate split), data fragmentation, model nonlinear, DT vs logistic regression, pros/cons (tidak perlu standardisasi, robust outlier, high variance).

## [08] Random Forest

- s14-18: ensemble, rata-rata atau committee (vote), stacking, bagging (bootstrap, 63% vs 37% out-of-bag).
- s20-27: Random Forest: bootstrap + subset fitur d ≪ D per node, contoh 6 tree dengan vote mayoritas, hyperparameter (n_estimators, max_samples, plus hyperparameter tree).
- s28-33: performa (DT 0,86 vs bag/RF 0,90-0,91), alasan RF lebih baik, pros/cons.

## [09] Supervised model evaluation

- s6-15: training, validation, testing; larangan memakai test untuk tuning; holdout; random subsampling; k-fold; LOOCV; pilihan K (umumnya 10).
- s18-21: metrik regresi MAE, MSE, RMSE, R² (contoh 4 titik: MAE 1,625, MSE 2,9375, RMSE 1,7139, R² 0,55).
- s22-31: confusion matrix, accuracy, precision, recall/sensitivity, specificity, G-mean, F1, F-beta, contoh F1 (precision 0,048, recall 0,833, F1 0,09).
- s32-36: Brier score, threshold (0,8 vs 0,4), ROC (TPR vs FPR), AUC, PR-AUC.
- s37-43: multiclass, class confusion matrix, OvR, macro dan micro averaging.
- s45-49: latihan transaksi ilegal (kelas positif adalah kelas yang penting: recall 0,400, specificity 0,982, accuracy 0,933, precision 0,667, F1 0,500).
- s51-60: ablation study, benchmark dataset, uji t (pooled variance, contoh TS = -0,0471, df 12, α 0,1).

## [10] Bias-variance tradeoff

- s4-12: curve fitting, consistency vs simplicity, Occam's razor, contoh tikus (linear regression vs squiggly line), training error vs generalization error.
- s13-19: bias, variance, underfitting, overfitting, model ideal, tabel gejala.
- s20-25: dekomposisi MSE = Bias² + Var + σ² (irreducible error).
- s26-28: regularisasi pada tree: pre-pruning (kriteria heuristik) dan post-pruning.
- s29-34: ensemble: bagging (variance σ²/k), boosting (AdaBoost, Gradient Boosting, XGBoost), diagram AdaBoost dan Gradient Boosting.
- s35-37: learning curve, tabel dampak teknik terhadap bias dan variance.

## [11] dan [11a] KNN

- [11] s5-17: motivasi, jarak Manhattan, Euclidean, cosine, Jaccard; memilih K (K=1 rentan noise, cross-validation).
- [11] s19-30: prediksi klasifikasi (vote), contoh pelanggan 13 (Manhattan 36, K=3 jadi kelas A), normalisasi (contoh salah klasifikasi tanpa normalisasi), fitur non-numerik, one-hot vs label encoding mengubah jarak.
- [11] s32-37: KNN regresi ŷ = (1/k)Σy, contoh harga rumah 1.670.
- [11] s39-42: pertimbangan praktis, kompleksitas O(knd), pros/cons.
- [11a]: latihan one-hot + Manhattan, K=3 dan K=5, beserta kunci jawaban.
- Catatan KNN (catatan kelas): beda K=3 dan K=5 berpotensi keluar; metrik jarak kecil berarti dekat, similarity besar berarti dekat.

## [12] Imbalanced classification

- s8-15: definisi, slight vs severe imbalance, penyebab, tantangan (cost FN vs FP, ukuran data, label noise, overlap distribusi).
- s16-22: solusi per level; stratified k-fold dan stratified train/test split.
- s24-35: cost-sensitive learning: cost matrix (contoh 88 dan 5; kebalikan rasio 1:100), compute_class_weight (n_samples / (n_classes × n_samples_with_class), contoh 0,505 dan 50), metode cost-sensitive (resampling, algoritma, ensemble), cost-sensitive logistic regression (NLL berbobot, ROC AUC 0,985 jadi 0,989), cost-sensitive decision tree.
- s37-47: sampling hanya pada data training; random oversampling dan undersampling; imblearn Pipeline.
- s49-62: SMOTE (convex combination), Borderline-SMOTE (aturan noise, borderline, safe dari jumlah mayoritas di k tetangga, s58), Borderline-SMOTE SVM, ADASYN (r1 = X1 + gap·diff, bobot ∝ #mayoritas/#minoritas, s62).
- s64-74: undersampling simpan (NearMiss-1/2/3, CNN), hapus (Tomek Links, ENN), kombinasi (OSS, NCR).
- s76-79: kombinasi over dan under, SMOTE + Tomek, SMOTE + ENN.
- s81-84: latihan (stratified 5-fold, titik convex combination, bobot 3 kelas, tiga model logistic regression).
- Catatan Imbalance 1 sampai 3 (catatan kelas): stratified CV dan metrik selain accuracy disebut **wajib**; accuracy dilarang pada data imbalanced.

## [13] Probability, likelihood, Bayes theorem

- s5-16: sample space, event, frekuensi relatif, aksioma, union, komplemen, conditional probability, product rule, chain rule, marginal (sum rule), independence vs mutually exclusive, conditional independence.
- s18-29: random variable, diskret vs kontinu, Bernoulli, Binomial, ringkasan RV diskret, Normal N(μ, σ²).
- s31-37: likelihood L(θ|X), i.i.d., log-likelihood, contoh cuaca (0,8)¹(0,2)⁵ = 0,000256.
- s39-46: law of total probability (contoh kacamata 0,26), Bayes theorem, kasus cuaca.

## [14] Naive Bayes

- s5-10: model probabilistik, discriminative vs generative, posterior ∝ likelihood × prior, asumsi naive (independen bersyarat kelas), argmax, log-likelihood.
- s11-15: training MLE: prior Nc/N, class conditional density kategorikal N_dck/N_c, numerik Gaussian (μ, σ²); testing.
- s17-34: studi kasus student exchange (prior 9/14 dan 5/14; posterior ya 1e-05 vs tidak 1,03e-06).
- s36-41: zero-frequency dan Laplace estimator, missing value (abaikan suku fitur), mixed-type attributes, varian NB (Gaussian, Multinomial, Bernoulli, Categorical).
- s42: latihan dua fitur.

## Latihan dan worksheet

| Berkas | Topik | Isi |
|---|---|---|
| `soal-pca.pdf` + `jawaban-soal-pca.md/html` | 06 | PCA 3 variabel, jumlah komponen, transformasi, rekonstruksi. Soal tercetak memuat kovarians yang keliru, lihat jawabannya. |
| `worksheet.png` + `jawaban-worksheet-pca-cart.html` | 06, 07a, 08, 10 | Worksheet 1 SCeLE: PCA 4 variabel (eigen 9,2720; 5; 3; 0,7280) dan CART deposito, bias-variance, ensemble, RF. |
| `ws2/0-6.png` + `jawaban-ws2-likelihood-naive-bayes.md` | 13, 14 | Worksheet 2: probabilitas UKM, uji penyakit, likelihood koin, independensi bersyarat, Naive Bayes spam dengan Laplace. |
| `soal-09` sampai `soal-12` dan PDF `soal-dan-pembahasan-kasdad-topik-09-12` | 09 sampai 12 | Set latihan buatan sendiri beserta pembahasan, **bukan** soal resmi. |
| `TP 1 KASDAD Ganjil 2026_2027.pdf` | tugas | Tugas pemrograman 1, klasifikasi dan regresi. |

## Pasca-UTS, belum ada materi (silabus)

Pekan 9-10: linear regression dan gradient descent, logistic dan softmax regression, Ridge dan Lasso. Pekan 11: clustering K-means dan hierarchical. Pekan 12-13: neural network MLP dan backpropagation. Worksheet 3, 4, 5 dan TP 2, 3 menyusul. Saat slidenya masuk, tambahkan bagian baru di peta ini mengikuti format di atas.
