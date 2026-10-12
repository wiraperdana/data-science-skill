# Lembar rumus KASDAD, dengan angka kontrol dari slide

Setiap rumus di sini tertulis di slide yang dirujuk. Kolom "Angka kontrol" berisi contoh hitungan dari slide itu. Pakai angka kontrol untuk menguji bahwa rumus dipahami dengan benar sebelum menerapkannya ke soal baru.

Bila sebuah rumus perlu tetapi tidak ada di sini, cari dulu di `sources/text/`. Rumus dari pengetahuan umum boleh dipakai hanya dengan label **di luar materi kuliah**.

## Statistik deskriptif dan outlier [03]

| Konsep | Rumus | Angka kontrol |
|---|---|---|
| Mean | x̄ = Σxᵢ / n (populasi μ = Σxᵢ / N), s23 | |
| Median | urutkan; n ganjil posisi (n+1)/2; n genap rata-rata posisi n/2 dan n/2+1, s25 | {3,6,12,18,19,21,23} → 18 |
| Range | (max - min) + 1 unit, s28 | 2,4,4,5,6,7,8 → 6 di s31, yaitu tanpa +1. Slide tidak konsisten; sebutkan keduanya bila ditanya. |
| Quartile, IQR | Q1 median separuh bawah, Q3 median separuh atas, IQR = Q3 - Q1, s29-31 | 2,4,4,5,6,7,8 → Q1 4, Q2 5, Q3 7, IQR 3 |
| Batas outlier | RLB = Q1 - 1,5·IQR; RUB = Q3 + 1,5·IQR, s32-33 | |
| Variance, std | rata-rata kuadrat deviasi; s = √variance, s34 | |
| Skewness | Σ(xᵢ - x̄)³ / (n s³), s36 | 0 untuk normal, negatif skew kiri |
| Kurtosis | Σ(xᵢ - x̄)⁴ / (n s⁴), s38 | normal 3, platykurtic < 3, leptokurtic > 3 |
| Pearson r | Σ(x - x̄)(y - ȳ) / √(Σ(x - x̄)² Σ(y - ȳ)²), [04] s29 | rentang -1 sampai 1 |

## Data preparation dan feature engineering [04] [05]

| Konsep | Rumus | Angka kontrol |
|---|---|---|
| Simple feature scaling | x' = x / x_max, [04] s35, [05] s26 | 1 juta / 4 juta = 0,25 |
| Min-max | x' = (x - min) / (max - min), [04] s35, [05] s25 | 2 juta → 0,33 |
| Z-score | x' = (x - μ) / σ, [04] s35 | |
| Chi-square | χ² = Σ (O - E)² / E, E = total baris × total kolom / N, [04] s29, [05] s44 | Sex vs Survived: E female-survived = 463·449/1313 = 158,33; χ² total 327,70 |
| Entropy | H = -Σ p log₂ p, [05] s47 | 9 ya, 5 tidak → 0,94 |
| Information gain | Gain(A) = H(S) - Σ (|Sv|/|S|) H(Sv), [05] s47-49 | age: 0,94 - 0,6935 = 0,2465; student 0,1516; credit 0,0479; income 0,0292 |
| Target encoding | mean target per kategori (regresi) atau P(y=1 \| kategori) (klasifikasi), [05] s14-16 | |
| Target encoding berbobot | (n × option mean + m × overall mean) / (n + m), [05] s17 | |
| Lasso (bentuk model) | y* = w1x1 + ... + wnxn + d; w = 0 berarti fitur tereliminasi, [05] s64 | Rumus penalti L1 **tidak** ada di slide |

Catatan: label kolom contoh target encoding di [05] s16 tertukar. Rata-rata tinggi badan adalah kasus regresi, sedangkan P(y=1 | warna) adalah kasus klasifikasi.

## PCA [06]

| Langkah | Rumus | Angka kontrol |
|---|---|---|
| Kovarians | cov(A,B) = Σ(a - ā)(b - b̄) / N di slide s7 | Worksheet memakai pembagi n - 1. Ikuti instruksi soal. |
| Eigen | Av = λv; diagonalisasi P⁻¹CP = D, s15-18, s43 | |
| Lima langkah | standarisasi (DataAdjust = Data - mean), kovarian, eigen, urutkan λ menurun, proyeksi, s24-31 | mean (1,81; 1,91); λ1 = 1,284, λ2 = 0,049; (0,69; 0,49) → (-0,828; -0,175) |
| Proyeksi | [T] = eigenvector baris; x' = T · x_adjust; reduksi: buang baris λ terkecil, s29-38 | |
| Kembali ke awal | x_adjust = Tᵀ x'; Data = DataAdjust + mean, s34-36 | 0,69 + 1,81 = 2,50 |
| Explained variance | EV_k = λk / (λ1 + ... + λn), s40 | eigenfaces: 150 dari 1850 komponen, EV 0,955 |
| Error rekonstruksi | SSE = Σ (x - x̂)²; dengan pembagi n - 1, SSE = (n - 1) × Σ λ yang dibuang | jawaban-soal-pca: SSE 0,0306 |

## CART [07a] dan Random Forest [08]

| Konsep | Rumus | Angka kontrol |
|---|---|---|
| Gini | G = 1 - Σ p², s24 | node {1 ya, 3 tidak}: 1 - (1/4)² - (3/4)² = 0,375 |
| Entropy | H = -Σ p log p, s24 | node pure = 0 |
| Cost split | (|D1|/|D|) cost(D1) + (|D2|/|D|) cost(D2), pilih argmin, s23 | popcorn 0,405; soda 4/7·0,375 + 3/7·0 = 0,214; umur terbaik 0,343 (t=15 atau 44); root = soda, s39 |
| Split numerik | midpoint nilai terurut, s25 | 7,12,18,35,38,50,83 → 9,5; 15; 26,5; 36,5; 44; 66,5 |
| Cost regresi | (1/|D|) Σ (y - ȳ)², s24 | Nonton Video tertimbang 174,636; Lab Lengkap (Iya ȳ 65,88 cost 71,61; Tidak ȳ 22,43 cost 113,1) tertimbang 90,97, jadi root, s50-52 |
| Daun regresi | rata-rata y di daun, s48 | |
| Bootstrap | N sampel dengan pengembalian; rata-rata 63% unik, 37% out-of-bag, [08] s17-18 | |
| Random Forest | tiap node memilih d ≪ D fitur acak, [08] s21 | |
| Agregasi | klasifikasi vote mayoritas, regresi rata-rata, [08] s16, s26 | 5 Yes, 1 No → Yes |

## Evaluasi model [09]

| Konsep | Rumus | Angka kontrol (latihan transaksi ilegal, positif = ilegal, s48) |
|---|---|---|
| Accuracy | (TP + TN) / (TP + FP + TN + FN) | 1400/1500 = 0,933 |
| Precision | TP / (TP + FP) | 50/75 = 0,667 |
| Recall, sensitivity, TPR | TP / (TP + FN) | 50/125 = 0,400 |
| Specificity | TN / (TN + FP) | 1350/1375 = 0,982 |
| FPR | FP / (TN + FP) = 1 - specificity, s34 | |
| F1 | 2 · precision · recall / (precision + recall) | 0,500 |
| F-beta | (1 + β²) · precision · recall / (β² · precision + recall), s29 | β > 1 utamakan recall |
| G-mean | √(sensitivity × specificity), s27 | |
| Brier score | (1/N) Σ (f_t - o_t)², s32 | |
| Macro | rata-rata metrik per kelas tanpa bobot, s40-41 | Macro-F1 = (42,1 + 30,8 + 66,7)/3 = 46,5% |
| Micro | hitung dari total TP, FP, FN, s42 | TP 12, FP 13 → 48% |
| MAE, MSE, RMSE | (1/n)Σ\|y - y*\|; (1/n)Σ(y - y*)²; √MSE, s19 | 4 titik: 1,625; 2,9375; 1,7139 |
| R² | 1 - Σ(y - y*)² / Σ(y - ȳ)², s20 | 1 - 11,75/26 = 0,55 |
| Uji t | TS = (X̄1 - X̄2) / √(Sp² (1/n + 1/m)); Sp² = ((n-1)S1² + (m-1)S2²) / (n + m - 2); df = n + m - 2, s58-59 | Sp² 22336,31; TS -0,0471; batas -1,356; terima H0 |
| Ukuran fold | uji = N/K, latih = N(K-1)/K | 10.000 dengan 5-fold: 8.000 latih, 2.000 uji |

## Bias-variance [10]

- MSE = Bias(g(x̂))² + Var(g(x̂)) + σ², dengan σ² irreducible error, s23.
- Rata-rata k prediksi i.i.d. yang masing-masing bervariansi σ² punya variansi σ²/k, s30. Inilah alasan bagging menurunkan variance.

## KNN [11]

| Konsep | Rumus | Angka kontrol |
|---|---|---|
| Manhattan | Σ \|pᵢ - qᵢ\|, s9 | (1,2,3) vs (4,5,6) → 9 |
| Euclidean | √Σ (pᵢ - qᵢ)², s9 | → √27 = 5,196 |
| Cosine | p·q / (‖p‖ ‖q‖), s10 | |
| Jaccard | \|p ∩ q\| / \|p ∪ q\|, s10-11 | |
| Regresi | ŷ = (1/k) Σ yᵢ, s33 | (1.500 + 1.700 + 1.800)/3 = 1.670 |
| Kompleksitas | O(knd), s41 | |

## Imbalanced [12]

| Konsep | Rumus | Angka kontrol |
|---|---|---|
| Bobot kelas | n_samples / (n_classes × n_samples_with_class), s28-29 | 10.000 data, 9.900 vs 100 → 0,505 dan 50 |
| SMOTE | s = λ·a + (1 - λ)·b, 0 ≤ λ ≤ 1 (convex combination), s49-50; ditulis juga r1 = X1 + gap·diff, s58, s62 | Latihan s82: titik harus terletak di segmen a-b |
| Borderline-SMOTE | dari k tetangga X1: #mayoritas = k noise; k/2 ≤ #mayoritas < k borderline (di-SMOTE); < k/2 safe, s58 | contoh k = 8 |
| ADASYN | bobot w1 ∝ #(mayoritas)/#(minoritas) di sekitar X1 ∝ jumlah sintetis, s62 | 9.900:100 menjadi 9.900:9.899 |
| Cost awal | cost FN = kebalikan rasio kelas, s27 | 1:100 → FN 100, FP 1 |
| Rasio imbalanced (catatan kelas) | jumlah semua sampel / jumlah sampel kelas terbanyak | catatan Imbalance 2, bukan slide |

## Probabilitas dan Naive Bayes [13] [14]

| Konsep | Rumus | Angka kontrol |
|---|---|---|
| Union | P(A∪B) = P(A) + P(B) - P(A∩B), [13] s8 | |
| Product rule | P(A,B) = P(A\|B)P(B) = P(B\|A)P(A), s10 | |
| Independence | P(A,B) = P(A)P(B); mutually exclusive berarti P(A∩B) = 0, s15 | |
| Conditional independence | P(A,B\|C) = P(A\|C)P(B\|C), s16 | |
| Bernoulli, Binomial | p^x(1-p)^(1-x); C(n,x) p^x (1-p)^(n-x), s23-25 | |
| Normal | f(x) = e^(-(x-μ)²/(2σ²)) / (σ√(2π)), s28 | |
| Likelihood i.i.d. | L(θ\|D) = Π p(xᵢ\|θ); log-likelihood = Σ log p(xᵢ\|θ), s36-37 | (0,8)¹(0,2)⁵ = 0,000256 |
| Total probability | P(A) = Σ P(A\|Cᵢ)P(Cᵢ), s39-40 | 0,4·0,3 + 0,2·0,7 = 0,26 |
| Bayes | P(C\|A) = P(A\|C)P(C) / P(A), s41-42 | |
| Prior NB | θ_c = N_c / N, [14] s12 | P(ya) = 9/14 |
| Kategorikal NB | θ_dck = N_dck / N_c, [14] s13 | P(olahraga \| ya) = 3/9 |
| Gaussian NB | μ dan σ² per kelas per fitur, [14] s14 | μ tulis,ya = 73; f60(73, 38) ≈ 0,007 |
| Posterior | P(c\|x) ∝ P(c) Π P(x_d\|c), pilih argmax, [14] s9, s15 | ya 1e-05 > tidak 1,03e-06 |
| Laplace | (N_dck + 1) / (N_c + K), K = jumlah kategori fitur, [14] s37 | keilmuan \| tidak = (1+0)/(3+5) |
| Missing pada NB | abaikan suku fitur yang hilang, [14] s38 | |
