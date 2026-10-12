#!/usr/bin/env python3
"""Outline mindmap materi UTS KASDAD, alur kronologi dan isi penjelasan.

Dibangun dari outline v2 (materi-uts-kasdad-v2.json, alur konsep). Isi setiap
konsep dipakai ulang apa adanya, lalu:
1. Konsep disusun ulang per dek slide [01] sampai [14], mengikuti bagian di
   slide "Outline" dosen atau course-map.md; dek tebal dipecah dua sheet.
2. Langkah tanpa hitungan dipindah ke elemen "urutan"; "langkah" tinggal untuk
   langkah matematis.
3. Elemen "hubungan" ditambahkan pada konsep yang menyambung ke bagian atau
   dek lain.
4. Lima konsep baru mengisi bagian slide yang belum punya konsep di v2.
5. Rujukan pertama di "sumber" = tempat konsep dibahas pada posisinya.

Pemakaian:
    python3 gen_materi-uts-kasdad-kronologi.py materi-uts-kasdad-kronologi.json
    python3 <course-to-skill>/scripts/build_mindmap.py materi-uts-kasdad-kronologi.json \
        --product .. --transkripsi transkripsi.json --alur kronologi --isi penjelasan -o <out>.xmind
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
V2 = json.loads((HERE / "materi-uts-kasdad-v2.json").read_text(encoding="utf-8"))
KONSEP = {k["concept"]: dict(k) for s in V2["sheets"] for g in s["children"] for k in g["children"]}

# 2. Langkah tanpa hitungan menjadi urutan.
for nama in ["Acting humanly", "KDD process", "CRISP-DM", "Business understanding", "Missing value",
             "Data integration", "SFS dan SBS", "Greedy dan kondisi berhenti", "Bootstrap dan bagging",
             "Random Forest", "K-fold cross-validation", "Confusion matrix", "Model ideal", "Memilih K",
             "Resampling hanya di training", "Condensed Nearest Neighbor", "Edited Nearest Neighbors"]:
    KONSEP[nama]["urutan"] = KONSEP[nama].pop("langkah")
# Penanganan, bukan langkah: pindah ke catatan.
KONSEP["Underfitting"]["catatan"] = "atasi: " + KONSEP["Underfitting"].pop("langkah")
KONSEP["Overfitting"]["catatan"] = "atasi: " + KONSEP["Overfitting"].pop("langkah")
KONSEP["Train, validation, test"]["urutan"] = "latih di training, tuning di validation, uji di test"

# Contoh Ice Age dipindah ke konsepnya sendiri di bagian contoh.
KONSEP["CART classification"].pop("contoh")

# 5. Rujukan pertama = posisi pembahasan pada alur slide.
SUMBER = {
    "CART classification": "[07a] s19-27",
    "Regression tree": "[07a] s48-53, s24",
    "KNN classifier": "[11] s19-23, s15, s42",
    "Underfitting": "[10] s15, s11, s19",
    "Overfitting": "[10] s15, s10, s19, s25",
    "Model ideal": "[10] s16-18, s24, s5",
}
for nama, s in SUMBER.items():
    KONSEP[nama]["sumber"] = s

# 3. Hubungan dengan bagian atau dek lain. Tidak dipasang bila konsep sudah punya
# 5 elemen (Normalisasi, SMOTE, Asumsi naive) atau bila kaitannya sudah tertulis
# di elemen lain.
HUBUNGAN = {
    "Acting rationally": "pendekatan agen rasional menjadi dasar bagian agen cerdas",
    "PEAS": "performance measure menentukan arti rasional bagi agen",
    "Supervised learning": "diulang di awal CART sebagai learning problem",
    "Klasifikasi vs regresi": "CART, KNN, dan metrik evaluasi dibedakan per jenis ini",
    "CRISP-DM": "kerangka kuliah data understanding dan data preparation berikutnya",
    "Business understanding": "hasilnya menentukan data yang dikumpulkan",
    "Central tendency": "mean dipakai lagi untuk imputasi missing value",
    "Pearson correlation": "dipakai lagi untuk cek redundansi di data integration",
    "Dirty data dan GIGO": "tiap jenis masalah ditangani di bagian data cleaning",
    "Data reduction dan selection": "dimensionality reduction diperdalam di sesi PCA",
    "Data discretization": "memakai binning yang sama dengan smoothing",
    "Feature creation": "feature extraction (PCA, t-SNE) dibahas di sesi PCA",
    "One-hot encoding": "memengaruhi perhitungan jarak pada KNN",
    "Curse of dimensionality": "motivasi feature selection di sini dan PCA",
    "Chi-square": "juga dipakai untuk cek redundansi di data integration",
    "Information gain": "entropy yang sama dipakai sebagai cost CART",
    "Tree importance": "muncul lagi di pros-cons CART",
    "Matriks kovarians": "bahan langkah kedua prosedur PCA",
    "Eigenvalue dan eigenvector": "eigenvector menjadi arah principal component",
    "Explained variance": "dasar memilih jumlah komponen pada eigenfaces",
    "t-SNE": "sudah disebut di feature extraction sesi feature engineering",
    "CART classification": "diterapkan langkah demi langkah pada contoh Ice Age",
    "Entropy": "sama dengan entropy information gain di feature selection",
    "Regression tree": "struktur sama dengan classification tree, cost diganti MSE",
    "Hyperparameter tree": "menjadi alat pre-pruning di sesi bias-variance",
    "Ensemble learning": "menjawab kelemahan high variance CART yang di-recall",
    "Bootstrap dan bagging": "dibahas ulang sebagai penurun variance di bias-variance",
    "K-fold cross-validation": "versi stratified wajib untuk data imbalanced",
    "MAE, MSE, RMSE": "MSE didekomposisi menjadi bias dan variance",
    "Accuracy": "alasan utama metrik khusus pada imbalanced classification",
    "Training vs generalization error": "diestimasi dengan holdout atau cross-validation",
    "Dekomposisi MSE": "memformalkan bias dan variance yang dibahas sebelumnya",
    "Pre-pruning": "memakai hyperparameter tree dari sesi CART",
    "Bagging untuk variance": "menjelaskan bagging dan Random Forest dari sesi sebelumnya",
    "Dampak teknik": "merangkum semua teknik di sesi ini",
    "Manhattan distance": "dipakai ulang di contoh pelanggan 13",
    "Normalisasi fitur": "memakai normalisasi dari data preparation",
    "Encoding fitur non-numerik": "memakai encoding dari feature engineering",
    "KNN regression": "sama seperti classifier, vote diganti rata-rata",
    "Metrik untuk imbalanced": "memilih ulang metrik dari sesi evaluasi model",
    "Stratified k-fold": "versi stratified dari k-fold cross-validation",
    "Class weight": "bobot kebalikan frekuensi kelas, sejalan dengan cost matrix",
    "Condensed Nearest Neighbor": "memakai 1-NN dari sesi KNN",
    "Likelihood": "dimaksimalkan oleh MLE saat training Naive Bayes",
    "Law of total probability": "menghitung penyebut pada Bayes theorem",
    "Bayes theorem": "dasar posterior Naive Bayes di sesi berikutnya",
}
for nama, h in HUBUNGAN.items():
    KONSEP[nama]["hubungan"] = h

# 4. Konsep baru, isinya diverifikasi dari teks atau transkripsi slide.
BARU = {
    "Exploratory Data Analysis": {
        "sumber": "[03] s17-18",
        "definisi": "analisis dan visualisasi awal sebelum model formal",
        "tujuan": "kenali atribut, missing, distribusi, imbalance, outlier, korelasi",
        "hubungan": "statistik deskriptif dan visualisasi adalah teknik EDA",
        "catatan": "istilah EDA dicetuskan John W. Tukey"},
    "Tipe data": {
        "sumber": "[03] s21",
        "definisi": "kenali data: kategorikal atau numerik",
        "jenis": "nominal, ordinal, interval, rasio",
        "hubungan": "nominal dan ordinal menentukan pilihan encoding di feature engineering"},
    "Reduksi dimensi": {
        "sumber": "[06] s2-4",
        "definisi": "kurangi jumlah fitur, informasi penting tetap terjaga",
        "tujuan": "representasi data matrix berdimensi lebih rendah",
        "hubungan": "lanjutan curse of dimensionality dari sesi feature selection",
        "catatan": "Hughes phenomenon: dimensi tinggi tidak menjamin akurasi naik"},
    "Contoh Ice Age": {
        "sumber": "[07a] s29-39, s41, s43",
        "tujuan": "classification tree prediksi suka film Ice Age",
        "langkah": ["Hitung cost Gini tiap kandidat split root",
                    "Popcorn 0,405; soda 0,214; umur 0,343",
                    "Root: Suka Minuman Soda, cost terkecil",
                    "Soda=Iya di-split umur ≤ 12,5; anak pure"],
        "hubungan": "kasus yang sama dipakai ulang di sesi Random Forest"},
    "Studi kasus student exchange": {
        "sumber": "[14] s17-34",
        "tujuan": "prediksi mahasiswa ikut student exchange atau tidak",
        "langkah": ["Prior: P(ya) = 9/14, P(tidak) = 5/14",
                    "P(X|ya) = 1,55e-05; P(X|tidak) = 2,88e-06",
                    "Kali prior: 1e-05 > 1,03e-06, prediksi ya"],
        "hubungan": "menerapkan NB kategorikal dan Gaussian sekaligus"},
}
for nama, isi in BARU.items():
    assert nama not in KONSEP, nama
    KONSEP[nama] = {"concept": nama, **isi}


def K(nama):
    return KONSEP[nama]


def B(judul, sumber, *nama):
    return {"title": judul, "sumber": sumber, "children": [K(n) for n in nama]}


def S(judul, *bagian):
    return {"title": judul, "children": list(bagian)}


SHEETS = [
    S("01. What is AI",
      B("Paradigma humanly", "[01] s11-14", "Thinking humanly", "Acting humanly"),
      B("Paradigma rationally", "[01] s15-16", "Thinking rationally", "Acting rationally"),
      B("Agen dan PEAS", "[01] s17-21", "Agent function", "PEAS"),
      B("Lingkungan dan tipe agen", "[01] s22-29", "Sifat lingkungan", "Tipe agen"),
      B("Supervised learning", "[01] s38-43", "Supervised learning", "Klasifikasi vs regresi"),
      B("Unsupervised dan elemen ML", "[01] s44-47", "Unsupervised learning", "Elemen machine learning")),
    S("02. What is Data Science",
      B("Motivasi sains data", "[02] s5-9", "Big Data"),
      B("Pengertian dan lingkup", "[02] s11-18", "Sains data dan analytics"),
      B("Metodologi sains data", "[02] s20-24", "KDD process", "CRISP-DM"),
      B("Studi kasus", "[02] s26-41", "Business understanding")),
    S("03. Data Collection, EDA, Statistics",
      B("Data collection", "[03] s7-15", "Data primer dan sekunder", "Open data"),
      B("EDA dan tipe data", "[03] s17-21", "Exploratory Data Analysis", "Tipe data"),
      B("Ukuran pusat dan sebaran", "[03] s22-34", "Central tendency", "Variance dan standard deviation",
        "IQR dan outlier"),
      B("Bentuk dan korelasi", "[03] s35-40", "Skewness dan kurtosis", "Pearson correlation"),
      B("Visualisasi data", "[03] s43-81", "Visualisasi EDA")),
    S("04. Data Preparation",
      B("Dirty data", "[04] s5-10", "Dirty data dan GIGO"),
      B("Data cleaning", "[04] s11-25", "Missing value", "Smoothing noisy data", "Data formatting"),
      B("Data integration", "[04] s26-31", "Data integration"),
      B("Data transformation", "[04] s32-35", "Normalisasi"),
      B("Selection dan reduction", "[04] s36-41", "Data reduction dan selection"),
      B("Data discretization", "[04] s42-44", "Data discretization")),
    S("05.1 Feature Engineering",
      B("Proses feature engineering", "[05] s2-11", "Feature creation"),
      B("Encoding kategorikal", "[05] s12-21", "One-hot encoding", "Target encoding", "Label / ordinal encoding",
        "Frequency encoding"),
      B("Binning dan scaling", "[05] s22-26", "Binning dan binarization"),
      B("Bag of Words", "[05] s27-29", "Bag of Words")),
    S("05.2 Feature Selection",
      B("Motivasi feature selection", "[05] s31-35", "Curse of dimensionality"),
      B("Filter", "[05] s36-54", "Missing ratio dan variance threshold", "Filter korelasi", "Chi-square",
        "Information gain"),
      B("Wrapper", "[05] s55-61", "SFS dan SBS", "SFFS, exhaustive, RFE"),
      B("Embedded", "[05] s62-64", "Tree importance", "Lasso")),
    S("06. Dimensionality Reduction dan PCA",
      B("Motivasi reduksi dimensi", "[06] s2-5", "Reduksi dimensi"),
      B("Review aljabar linear", "[06] s7-18", "Matriks kovarians", "Eigenvalue dan eigenvector"),
      B("Prosedur PCA", "[06] s24-38", "PCA", "Skor dan rekonstruksi"),
      B("Explained variance dan intuisi", "[06] s40-45", "Explained variance"),
      B("Eigenfaces", "[06] s46-50", "Eigenfaces"),
      B("Metode lain", "[06] s51-53", "t-SNE")),
    S("07a. CART",
      B("Algoritma CART", "[07a] s19-23", "CART classification", "Split kategorikal"),
      B("Cost dan split point", "[07a] s24-27", "Gini index", "Entropy", "Split numerik",
        "Greedy dan kondisi berhenti"),
      B("Classification tree Ice Age", "[07a] s29-46", "Contoh Ice Age"),
      B("Regression tree", "[07a] s47-54", "Regression tree"),
      B("Hyperparameter tree", "[07a] s55-59", "Hyperparameter tree"),
      B("Isu dan pros-cons", "[07a] s60-64", "Surrogate split")),
    S("08. Random Forest",
      B("Ensemble learning", "[08] s13-16", "Ensemble learning", "Majority vote"),
      B("Bagging dan out-of-bag", "[08] s17-18", "Bootstrap dan bagging", "Out-of-bag"),
      B("Random Forest", "[08] s19-27", "Random Forest", "Hyperparameter Random Forest"),
      B("Performa Random Forest", "[08] s28-33", "Random Forest vs single tree")),
    S("09.1 Evaluasi: validasi dan metrik dasar",
      B("Pembagian data", "[09] s6-10", "Train, validation, test", "Holdout"),
      B("Cross-validation", "[09] s11-15", "K-fold cross-validation", "LOOCV dan random subsampling"),
      B("Metrik regresi", "[09] s18-21", "MAE, MSE, RMSE", "R-squared"),
      B("Confusion matrix", "[09] s22-25", "Confusion matrix", "Accuracy")),
    S("09.2 Evaluasi: metrik lanjut dan perbandingan",
      B("Precision, recall, F", "[09] s26-31", "Precision", "Recall dan specificity", "G-mean", "F1 dan F-beta"),
      B("Probabilitas dan threshold", "[09] s32-36", "Brier score", "ROC dan AUC"),
      B("Multiclass", "[09] s37-43", "Macro dan micro averaging"),
      B("Perbandingan model", "[09] s51-60", "Benchmark dan ablation", "Uji t (t-test)")),
    S("10.1 Bias dan variance",
      B("Generalisasi", "[10] s4-12", "Training vs generalization error"),
      B("Bias dan variance", "[10] s13-14", "Bias", "Variance"),
      B("Underfitting dan overfitting", "[10] s15-19", "Underfitting", "Overfitting", "Model ideal"),
      B("Dekomposisi MSE", "[10] s20-25", "Dekomposisi MSE")),
    S("10.2 Mengendalikan bias dan variance",
      B("Regularisasi tree", "[10] s26-28", "Pre-pruning", "Post-pruning"),
      B("Bagging", "[10] s29-31", "Bagging untuk variance"),
      B("Boosting", "[10] s32-34", "Boosting", "XGBoost", "AdaBoost", "Gradient Boosting"),
      B("Learning curve dan dampak", "[10] s35-37", "Learning curve", "Dampak teknik")),
    S("11. KNN Classification dan Regression",
      B("Jarak dan memilih K", "[11] s5-17", "Manhattan distance", "Euclidean distance", "Cosine similarity",
        "Jaccard similarity", "Memilih K"),
      B("KNN classification", "[11] s18-30", "KNN classifier", "Normalisasi fitur", "Encoding fitur non-numerik"),
      B("KNN regression", "[11] s31-37", "KNN regression"),
      B("Analisis KNN", "[11] s38-42", "Kompleksitas")),
    S("12.1 Imbalanced: evaluasi dan cost-sensitive",
      B("Imbalanced classification", "[12] s8-15", "Imbalanced classification", "Penyebab dan tantangan"),
      B("Evaluation level", "[12] s16-22", "Metrik untuk imbalanced", "Stratified k-fold"),
      B("Cost matrix dan class weight", "[12] s23-29", "Cost matrix", "Class weight"),
      B("Cost-sensitive LR dan DT", "[12] s30-35", "Cost-sensitive LR dan DT")),
    S("12.2 Imbalanced: data level",
      B("Prinsip data level", "[12] s36-47", "Resampling hanya di training", "Random over/undersampling"),
      B("Oversampling sintetis", "[12] s48-62", "SMOTE", "Borderline-SMOTE", "ADASYN"),
      B("Undersampling simpan", "[12] s64-68", "NearMiss", "Condensed Nearest Neighbor"),
      B("Undersampling hapus", "[12] s69-74", "Tomek Links", "Edited Nearest Neighbors", "OSS dan NCR"),
      B("Kombinasi over dan under", "[12] s75-79", "SMOTE + Tomek atau ENN")),
    S("13. Probability dan Likelihood",
      B("Review probability", "[13] s5-13", "Aksioma dan aturan dasar", "Conditional probability"),
      B("Independensi", "[13] s14-16", "Independence", "Conditional independence"),
      B("Random variable", "[13] s18-29", "Bernoulli dan Binomial", "Normal (Gaussian)"),
      B("Likelihood", "[13] s31-37", "Likelihood", "Log-likelihood"),
      B("Bayes theorem", "[13] s39-46", "Law of total probability", "Bayes theorem")),
    S("14. Naive Bayes",
      B("Model probabilistik", "[14] s5-10", "Asumsi naive dan posterior"),
      B("Training dengan MLE", "[14] s11-15", "Maximum likelihood estimation", "Naive Bayes kategorikal",
        "Gaussian Naive Bayes"),
      B("Studi kasus student exchange", "[14] s17-34", "Studi kasus student exchange"),
      B("Masalah Naive Bayes", "[14] s36-41", "Zero-frequency dan Laplace", "Missing dan mixed-type")),
]

terpakai = [k["concept"] for s in SHEETS for b in s["children"] for k in b["children"]]
ganda = {n for n in terpakai if terpakai.count(n) > 1}
sisa = set(KONSEP) - set(terpakai)
assert not ganda and not sisa, (ganda, sisa)

json.dump({"sheets": SHEETS}, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(SHEETS)} sheet, {len(terpakai)} konsep ({len(BARU)} baru), "
      f"{sum('urutan' in k for k in KONSEP.values())} urutan, {len(HUBUNGAN) + len(BARU)} hubungan")
