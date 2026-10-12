#!/usr/bin/env python3
"""Set simulasi UTS KASDAD bergaya worksheet SCeLE: studi kasus berantai. Semua kunci dihitung di sini."""
import json, math, sys
from pathlib import Path

G, Q = [], []
def group(id, title, stem): G.append({"id": id, "title": title, "stem": stem})
def q(id, grp, kind, prompt, solution, source, answer=None, options=None, decimals=4, rubric=None, model=None, sec="A"):
    topic = next(g["title"] for g in G if g["id"] == grp) if grp else "Essay"
    Q.append({k: v for k, v in dict(id=id, section=sec, group=grp, topic=topic, kind=kind, prompt=prompt, options=options,
              answer=answer, decimals=decimals if kind == "num" else None, solution=solution, source=source,
              rubric=rubric, model_answer=model).items() if v is not None})
def r4(x): return round(x + 0.0, 4)
def f4(x): return f"{x:.4f}"
def H(*p): t = sum(p); return -sum((a / t) * math.log2(a / t) for a in p if a)
def gini_l(l): n = len(l); return 0 if n == 0 else 1 - sum((l.count(c) / n) ** 2 for c in set(l))
def table(head, rows): return "<table class='t'><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"
def npdf(x, m, v): return math.exp(-(x - m) ** 2 / (2 * v)) / math.sqrt(2 * math.pi * v)

# ===================== K1. PCA =====================
X = {"X1": [7, 2, 6, 5, 5], "X2": [16, 11, 9, 12, 12], "X3": [9, 9, 9, 5, 8], "X4": [21, 21, 21, 21, 16]}
names = list(X); n = 5; mean = {k: sum(v) / n for k, v in X.items()}
C = {k: [x - mean[k] for x in v] for k, v in X.items()}
def cov(a, b): return sum(x * y for x, y in zip(C[a], C[b])) / (n - 1)
S = [[cov(a, b) for b in names] for a in names]
lam = sorted([7.5, 5.0, 3.0, 2.5], reverse=True)
s5 = math.sqrt(5); v1 = (1 / s5, 2 / s5, 0, 0); vX4 = (0, 0, 0, 1); vX3 = (0, 0, 1, 0); v4 = (2 / s5, -1 / s5, 0, 0)
for vec, l in [(v1, 7.5), (vX4, 5), (vX3, 3), (v4, 2.5)]:  # cek Sv = λv
    Sv = [sum(S[i][j] * vec[j] for j in range(4)) for i in range(4)]
    assert all(abs(Sv[i] - l * vec[i]) < 1e-9 for i in range(4))
obs1 = [C[k][0] for k in names]
z1 = sum(a * b for a, b in zip(obs1, v1)); z2 = sum(a * b for a, b in zip(obs1, vX4))
sse = sum(sum(C[k][i] * v4[j] for j, k in enumerate(names)) ** 2 for i in range(n))
assert abs(sse - (n - 1) * 2.5) < 1e-9
tot = sum(lam)
group("K1", "Studi kasus 1. PCA",
      "Lima observasi dengan empat variabel:" + table(["Observasi"] + names, [[i + 1] + [X[k][i] for k in names] for i in range(n)]) +
      "Lakukan PCA. Gunakan kovarians sampel dengan pembagi n − 1. Eigenvector dinormalkan panjang 1 dan komponen tak-nol pertamanya positif. Isian dibulatkan 4 desimal.")
q("P1", "K1", "num", "Mean variabel X2 adalah …", f"X̄2 = ({' + '.join(map(str, X['X2']))})/5 = <b>{f4(mean['X2'])}</b>. Vektor mean μ = ({', '.join(f'{mean[k]:g}' for k in names)}).", "[06] s26", answer=r4(mean["X2"]))
q("P2", "K1", "mc", "Mengapa data perlu di-centering sebelum menghitung matriks kovarians?",
  "Rumus kovarians mengukur variasi di sekitar mean. Centering (DataAdjust = Data − mean) meletakkan mean di 0 sehingga sumbu PCA menggambarkan variasi antarobservasi, bukan besar nilai rata-rata.", "[06] s26", answer=2,
  options=["Agar semua nilai menjadi positif", "Agar eigenvalue menjadi bilangan bulat", "Agar sumbu PCA menggambarkan variasi di sekitar mean, bukan besar mean", "Agar jumlah variabel berkurang"])
q("P3", "K1", "num", "Nilai X1 observasi pertama setelah centering (X1′) adalah …", f"X1′ = {X['X1'][0]} − {mean['X1']:g} = <b>{f4(C['X1'][0])}</b>. Seluruh observasi 1 terpusat: ({', '.join(f'{x:g}' for x in obs1)}).", "[06] s26", answer=r4(C["X1"][0]))
q("P4", "K1", "num", "Variansi sampel X1 adalah …", f"Var(X1) = Σ(X1′)²/(n−1) = ({' + '.join(f'({x:g})²' for x in C['X1'])})/4 = <b>{f4(S[0][0])}</b>.", "[06] s7; worksheet 1", answer=r4(S[0][0]))
q("P5", "K1", "num", "Kovarians X1 dengan X2 adalah …", f"Cov(X1,X2) = Σ(X1′·X2′)/4 = ({' + '.join(f'({a:g})({b:g})' for a, b in zip(C['X1'], C['X2']))})/4 = <b>{f4(S[0][1])}</b>.", "[06] s7", answer=r4(S[0][1]))
q("P6", "K1", "num", "Kovarians X1 dengan X3 adalah …", f"Cov(X1,X3) = ({' + '.join(f'({a:g})({b:g})' for a, b in zip(C['X1'], C['X3']))})/4 = <b>{f4(S[0][2])}</b>. Hal yang sama berlaku untuk pasangan lain di luar blok X1–X2, sehingga matriks kovarians berbentuk blok diagonal:<br>S = " +
  "[" + "; ".join("[" + ", ".join(f"{x:g}" for x in r) + "]" for r in S) + "].", "[06] s7", answer=r4(S[0][2]))
q("P7", "K1", "mc", "Elemen diagonal dan elemen di luar diagonal matriks kovarians berturut-turut menyatakan …",
  "Diagonal = variansi tiap variabel; luar diagonal = kovarians pasangan variabel, tandanya menunjukkan arah perubahan bersama.", "[06] s7-8", answer=0,
  options=["Variansi tiap variabel; kovarians antarpasangan variabel", "Mean tiap variabel; korelasi antarvariabel", "Eigenvalue; eigenvector", "Kovarians antarpasangan; variansi tiap variabel"])
sol_eig = ("det(S − λI) = 0 dapat dipisah per blok karena entri nol. Blok X1–X2: (3,5 − λ)(6,5 − λ) − 2² = 0 → λ² − 10λ + 18,75 = 0 → λ = (10 ± √(100 − 75))/2 = (10 ± 5)/2 → 7,5 dan 2,5. "
           "Blok X3: λ = 3. Blok X4: λ = 5. Urutkan menurun: λ1 = 7,5; λ2 = 5; λ3 = 3; λ4 = 2,5.")
for i, l in enumerate(lam, 1):
    q(f"P{7 + i}", "K1", "num", f"Eigenvalue terbesar ke-{i} (λ{i}) adalah …", sol_eig + f" Jawaban: <b>{f4(l)}</b>.", "[06] s15-18, s27; worksheet 1", answer=r4(l))
q("P12", "K1", "mc", "Apa makna eigenvector pada PCA?",
  "Eigenvector adalah arah principal component (basis baru); elemennya menunjukkan bobot tiap variabel asli pada arah itu. Eigenvalue adalah besar variansi data sepanjang arah tersebut.", "[06] s27-29, s41-45", answer=1,
  options=["Besar variansi data pada sebuah arah", "Arah principal component, berisi bobot tiap variabel asli", "Rata-rata tiap variabel", "Error rekonstruksi tiap observasi"])
sol_v1 = "Untuk λ1 = 7,5 pada blok X1–X2: (3,5 − 7,5)a + 2b = 0 → b = 2a; komponen X3 dan X4 harus 0 karena (3 − 7,5)c = 0 dan (5 − 7,5)d = 0. Normalisasi: v1 = (1, 2, 0, 0)/√5 = (0,4472; 0,8944; 0; 0)."
q("P13", "K1", "num", "Komponen X1 pada eigenvector PC1 (v1) adalah …", sol_v1 + f" Jawaban: <b>{f4(v1[0])}</b>.", "[06] s28; worksheet 1", answer=r4(v1[0]))
q("P14", "K1", "num", "Komponen X2 pada eigenvector PC1 (v1) adalah …", sol_v1 + f" Jawaban: <b>{f4(v1[1])}</b>.", "[06] s28", answer=r4(v1[1]))
q("P15", "K1", "num", "Total variansi data (jumlah seluruh eigenvalue) adalah …", f"Σλ = 7,5 + 5 + 3 + 2,5 = <b>{f4(tot)}</b> = trace S = 3,5 + 6,5 + 3 + 5.", "[06] s40", answer=r4(tot))
q("P16", "K1", "num", "Explained variance ratio PC1 (proporsi) adalah …", f"EV1 = λ1/Σλ = 7,5/18 = <b>{f4(7.5 / 18)}</b>.", "[06] s40", answer=r4(7.5 / 18))
q("P17", "K1", "num", "Cumulative explained variance PC1 dan PC2 (proporsi) adalah …", f"(7,5 + 5)/18 = <b>{f4(12.5 / 18)}</b>.", "[06] s40", answer=r4(12.5 / 18))
q("P18", "K1", "num", "Banyak principal component minimum agar cumulative explained variance ≥ 85% adalah …",
  f"Kumulatif: PC1 {f4(7.5 / 18)}, PC1–2 {f4(12.5 / 18)}, PC1–3 {f4(15.5 / 18)}, PC1–4 1,0000. Yang pertama ≥ 0,85 adalah tiga komponen → <b>3</b>.", "[06] s40", answer=3, decimals=0)
q("P19", "K1", "mc", "Bila dipertahankan k = 3 komponen, ukuran matriks transformasi T (baris = komponen) dan matriks skor Z (komponen × observasi) adalah …",
  "T disusun dari 3 eigenvector sebagai baris: 3 × 4. Z = T·Xcᵀ: (3 × 4)(4 × 5) = 3 × 5.", "[06] s29-31; worksheet 1", answer=1, options=["4 × 3 dan 5 × 3", "3 × 4 dan 3 × 5", "3 × 5 dan 4 × 5", "4 × 4 dan 4 × 5"])
q("P20", "K1", "num", "Skor PC1 observasi pertama adalah …", f"z = v1 · x′ = (0,4472)({obs1[0]:g}) + (0,8944)({obs1[1]:g}) + 0 + 0 = <b>{f4(z1)}</b>.", "[06] s30-31", answer=r4(z1))
q("P21", "K1", "num", "Skor PC2 observasi pertama adalah …", f"PC2 berpadanan λ2 = 5, yaitu arah X4: v2 = (0, 0, 0, 1). Skor = X4′ observasi 1 = <b>{f4(z2)}</b>.", "[06] s30-31", answer=r4(z2))
q("P22", "K1", "num", "Dengan k = 3 komponen, berapa total reconstruction SSE (seluruh elemen data)?",
  f"Yang hilang hanya komponen PC4 (λ4 = 2,5, arah (2, −1, 0, 0)/√5). SSE = Σ(skor PC4)² = (n − 1)·λ4 = 4 × 2,5 = <b>{f4(sse)}</b>. Cek per observasi: skor PC4 = (2x1′ − x2′)/√5 → 0, −5/√5, 5/√5, 0, 0 → kuadrat 0 + 5 + 5 + 0 + 0 = 10.", "[06] s33-38; soal-pca", answer=r4(sse))
q("P23", "K1", "num", "Reconstruction MSE per elemen data (SSE dibagi n × p) adalah …", f"MSE = 10/(5 × 4) = <b>{f4(sse / 20)}</b>.", "soal-pca; worksheet 1", answer=r4(sse / 20))

# ===================== K2. CART dan Random Forest =====================
usia = [24, 29, 33, 38, 44, 49, 55, 61]
sal = ["Ya", "Tidak", "Ya", "Tidak", "Tidak", "Ya", "Ya", "Ya"]
kan = ["RM", "Cabang", "RM", "RM", "Cabang", "Cabang", "Mobile", "RM"]
dep = ["Tidak", "Tidak", "Tidak", "Ya", "Ya", "Ya", "Tidak", "Ya"]
def split(mask, idx=range(8)):
    idx = list(idx); L = [dep[i] for i in idx if mask[i]]; R = [dep[i] for i in idx if not mask[i]]
    return len(L) / len(idx) * gini_l(L) + len(R) / len(idx) * gini_l(R), L, R
def cnt(l): return f"{l.count('Ya')} Ya, {l.count('Tidak')} Tidak"
groot = gini_l(dep)
cS, LS, RS = split([s == "Ya" for s in sal])
ck = {k: split([x == k for x in kan]) for k in ["Mobile", "Cabang", "RM"]}
mids = [(usia[i] + usia[i + 1]) / 2 for i in range(7)]
cu = {t: split([u <= t for u in usia]) for t in mids}
tb = min(cu, key=lambda t: cu[t][0])
R_idx = [i for i in range(8) if usia[i] > tb]; L_idx = [i for i in range(8) if usia[i] <= tb]
gR = gini_l([dep[i] for i in R_idx])
cRk = {k: split([x == k for x in kan], R_idx) for k in sorted(set(kan[i] for i in R_idx))}
cRs = split([s == "Ya" for s in sal], R_idx)
group("K2", "Studi kasus 2. CART dan Random Forest",
      "Bank ingin memprediksi apakah nasabah membuka <b>Deposito</b> (Ya/Tidak). Bangun classification tree CART dengan kriteria Gini dan binary split:" +
      table(["ID", "Usia", "Saldo Tinggi", "Kanal", "Deposito"], [[i + 1, usia[i], sal[i], kan[i], dep[i]] for i in range(8)]) +
      "Cost split = rata-rata Gini anak yang dibobot jumlah data. Isian 4 desimal.")
q("C1", "K2", "num", "Banyak nasabah dengan Deposito = Ya adalah …", f"Hitung kolom Deposito: <b>{dep.count('Ya')}</b>.", "[07a] s29-30", answer=dep.count("Ya"), decimals=0)
q("C2", "K2", "num", "Gini index root adalah …", f"Root: {cnt(dep)}. Gini = 1 − (4/8)² − (4/8)² = <b>{f4(groot)}</b>.", "[07a] s24", answer=r4(groot))
q("C3", "K2", "num", "Gini kelompok Saldo Tinggi = Ya adalah …", f"Saldo Tinggi = Ya: {cnt(LS)} → Gini = <b>{f4(gini_l(LS))}</b>.", "[07a] s24, s31", answer=r4(gini_l(LS)))
q("C4", "K2", "num", "Cost split berdasarkan Saldo Tinggi adalah …", f"Ya: {len(LS)} data, Gini {f4(gini_l(LS))}; Tidak: {len(RS)} data ({cnt(RS)}), Gini {f4(gini_l(RS))}. Cost = {len(LS)}/8·{f4(gini_l(LS))} + {len(RS)}/8·{f4(gini_l(RS))} = <b>{f4(cS)}</b>.", "[07a] s23, s31", answer=r4(cS))
q("C5", "K2", "num", "Fitur Kanal memiliki tiga kategori. Berapa banyak partisi biner unik (satu kategori vs dua lainnya) yang perlu dievaluasi?", "CART kategorikal: x_j = t vs x_j ≠ t untuk tiap t. Tiga kategori → <b>3</b> partisi: Mobile | Cabang+RM, Cabang | Mobile+RM, RM | Mobile+Cabang.", "[07a] s23, s25", answer=3, decimals=0)
solk = "<br>".join(f"{k} | lainnya: {k} → {cnt(v[1])} (Gini {f4(gini_l(v[1]))}); lainnya → {cnt(v[2])} (Gini {f4(gini_l(v[2]))}); cost = {f4(v[0])}" for k, v in ck.items())
for nm, k in [("C6", "Mobile"), ("C7", "Cabang"), ("C8", "RM")]:
    q(nm, "K2", "num", f"Cost split partisi Kanal: <b>{k} | lainnya</b> adalah …", solk + f"<br>Jawaban: <b>{f4(ck[k][0])}</b>.", "[07a] s23-25", answer=r4(ck[k][0]))
q("C9", "K2", "num", "Untuk fitur Usia, berapa banyak kandidat threshold (midpoint antar nilai terurut)?", f"8 nilai berbeda → 8 − 1 = <b>7</b> midpoint: {', '.join(f'{t:g}' for t in mids)}.", "[07a] s25, s33", answer=7, decimals=0)
for nm, t in [("C10", 35.5), ("C11", 41.0)]:
    v = cu[t]
    q(nm, "K2", "num", f"Cost split Usia ≤ {t:g} adalah …", f"Kiri (≤ {t:g}): {cnt(v[1])}, Gini {f4(gini_l(v[1]))}. Kanan: {cnt(v[2])}, Gini {f4(gini_l(v[2]))}. Cost = {len(v[1])}/8·{f4(gini_l(v[1]))} + {len(v[2])}/8·{f4(gini_l(v[2]))} = <b>{f4(v[0])}</b>.<br>Semua kandidat: " +
      ", ".join(f"t={x:g}: {f4(cu[x][0])}" for x in mids) + ".", "[07a] s33-38", answer=r4(v[0]))
q("C12", "K2", "mc", "Fitur dan threshold yang dipilih sebagai root adalah …",
  f"Bandingkan cost minimum tiap fitur: Saldo {f4(cS)}, Kanal terbaik {f4(min(v[0] for v in ck.values()))}, Usia ≤ {tb:g} {f4(cu[tb][0])}. Terkecil: <b>Usia ≤ {tb:g}</b>.", "[07a] s39", answer=2,
  options=["Saldo Tinggi", "Kanal = Mobile | lainnya", f"Usia ≤ {tb:g}", "Usia ≤ 41"])
q("C13", "K2", "num", "Gini node kanan (Usia > root threshold) adalah …", f"Node kanan berisi ID {', '.join(str(i + 1) for i in R_idx)}: {cnt([dep[i] for i in R_idx])} → Gini = <b>{f4(gR)}</b>. Node kiri ({cnt([dep[i] for i in L_idx])}) sudah pure sehingga menjadi leaf.", "[07a] s40", answer=r4(gR))
q("C14", "K2", "num", "Pada node kanan, berapa cost split terbaik dari fitur Kanal?",
  "<br>".join(f"{k} | lainnya: cost = {f4(v[0])}" for k, v in cRk.items()) + f"<br>Saldo Tinggi: {f4(cRs[0])}. Terbaik Kanal = Mobile | lainnya dengan cost <b>{f4(min(v[0] for v in cRk.values()))}</b>, kedua anak pure.",
  "[07a] s40-44", answer=r4(min(v[0] for v in cRk.values())))
q("C15", "K2", "mc", f"Tree akhir dipakai untuk nasabah baru: Usia 50, Saldo Tinggi = Tidak, Kanal = Cabang. Prediksinya adalah …",
  f"Usia 50 > {tb:g} → node kanan. Kanal = Cabang ≠ Mobile → cabang 'lainnya' yang berisi seluruhnya Ya → prediksi <b>Ya</b>.", "[07a] s45", answer=0, options=["Ya", "Tidak"])
q("C16", "K2", "mc", "Model A dibatasi max_depth = 1, Model B tumbuh penuh dengan error training 0% dan error testing 30%. Pernyataan yang tepat adalah …",
  "Tree dangkal: bias lebih tinggi, variance rendah. Tree penuh dengan error training 0% dan testing tinggi: overfitting (high variance). Pengendaliannya: batasi kedalaman, naikkan min_samples_leaf, atau pruning.", "[10] s13-19, s27-28; worksheet 1", answer=1,
  options=["A overfitting, B underfitting", "A cenderung high bias, B overfitting (high variance)", "Keduanya high bias", "B ideal karena error training 0%"])
q("C17", "K2", "num", "Ensemble tiga tree memprediksi seorang nasabah: Ya, Tidak, Ya. Proporsi suara Ya adalah …", "Majority vote: 2 dari 3 suara → prediksi Ya. Proporsi = 2/3 = <b>0.6667</b>.", "[08] s16, s25-26", answer=r4(2 / 3))
q("C18", "K2", "mc", "Bootstrap sampling dalam bagging berarti …", "Ambil N sampel dari data latih <b>dengan pengembalian</b>; satu observasi bisa terambil berkali-kali, sekitar 37% tidak terambil (out-of-bag).", "[08] s17-18", answer=0,
  options=["Mengambil sampel dengan pengembalian sebanyak N", "Membagi data menjadi K fold tanpa tumpang tindih", "Mengambil subset fitur acak", "Mengurutkan data lalu mengambil setengah"])
q("C19", "K2", "num", "Random Forest dengan 100 tree pada data 3 fitur memakai d = 2 kandidat fitur per split. Bila d dinaikkan menjadi 3 (semua fitur), model menjadi setara dengan …? Ketik banyak kandidat fitur per split untuk Random Forest semula.",
  "RF memilih d ≪ D fitur acak di setiap node; d = <b>2</b>. Bila d = D, RF menjadi bagging biasa dan korelasi antartree naik.", "[08] s21-23", answer=2, decimals=0)
q("C20", "K2", "mc", "Observasi yang tidak terambil pada bootstrap sample suatu tree digunakan untuk …", "Data out-of-bag dapat dipakai sebagai testing set untuk estimasi kinerja model.", "[08] s18", answer=2,
  options=["Menambah fitur baru", "Dibuang", "Estimasi kinerja (out-of-bag)", "Menentukan nilai d"])

# ===================== K3. Evaluasi dan imbalanced =====================
N3, fraud, flagged, tp = 2000, 80, 100, 60
TP, FP, FN = tp, flagged - tp, fraud - tp; TN = N3 - TP - FP - FN
acc = (TP + TN) / N3; prec = TP / (TP + FP); rec = TP / (TP + FN); spec = TN / (TN + FP)
f1 = 2 * prec * rec / (prec + rec); f2 = 5 * prec * rec / (4 * prec + rec); gm = math.sqrt(rec * spec)
group("K3", "Studi kasus 3. Evaluasi model dan imbalanced classification",
      f"Sistem deteksi transaksi fraud diuji pada {N3:,} transaksi; {fraud} di antaranya fraud. Sistem menandai {flagged} transaksi sebagai fraud, dan {tp} dari tandaan itu benar fraud. Kelas positif = fraud. Isian 4 desimal.".replace(",", "."))
for nm, lab, val, how in [("E1", "FN", FN, f"FN = fraud − TP = {fraud} − {TP}"), ("E2", "TN", TN, f"TN = {N3} − TP − FP − FN = {N3} − {TP} − {FP} − {FN}")]:
    q(nm, "K3", "num", f"Nilai {lab} adalah …", f"TP = {TP}, FP = {flagged} − {TP} = {FP}. {how} = <b>{val}</b>.", "[09] s24, s45-49", answer=val, decimals=0)
for nm, lab, val, how, src in [("E3", "Accuracy", acc, f"({TP} + {TN})/{N3}", "[09] s25"), ("E4", "Precision", prec, f"{TP}/({TP} + {FP})", "[09] s26"),
                               ("E5", "Recall", rec, f"{TP}/({TP} + {FN})", "[09] s26"), ("E6", "Specificity", spec, f"{TN}/({TN} + {FP})", "[09] s26"),
                               ("E7", "F1-score", f1, f"2·{f4(prec)}·{f4(rec)}/({f4(prec)} + {f4(rec)})", "[09] s28"),
                               ("E8", "F2-score", f2, f"5·{f4(prec)}·{f4(rec)}/(4·{f4(prec)} + {f4(rec)})", "[09] s29"),
                               ("E9", "G-mean", gm, f"√({f4(rec)} × {f4(spec)})", "[09] s27")]:
    q(nm, "K3", "num", f"{lab} adalah …", f"{lab} = {how} = <b>{f4(val)}</b>.", src, answer=r4(val))
dummy = (N3 - fraud) / N3
q("E10", "K3", "num", "Accuracy model 'dummy' yang selalu memprediksi bukan-fraud adalah …", f"({N3} − {fraud})/{N3} = <b>{f4(dummy)}</b>, hampir sama dengan accuracy sistem ({f4(acc)}) padahal recall-nya 0. Inilah alasan accuracy dilarang untuk data imbalanced.", "[09] s22, s31; [12] s12", answer=r4(dummy))
q("E11", "K3", "mc", "Untuk deteksi fraud, kesalahan yang paling mahal adalah fraud yang lolos. Metrik yang paling tepat diprioritaskan adalah …", "Fraud lolos = FN. Metrik yang menghukum FN: recall, atau F-beta dengan β > 1 (misal F2).", "[09] s26, s29, s49", answer=2,
  options=["Accuracy", "Precision", "Recall / F2-score", "Specificity"])
cost = FN * 50 + FP * 1
q("E12", "K3", "num", "Cost matrix menetapkan FN = 50, FP = 1, prediksi benar = 0. Total cost sistem adalah …", f"Total = 50·FN + 1·FP = 50·{FN} + {FP} = <b>{cost}</b>.", "[12] s24-27", answer=cost, decimals=0)
w1 = N3 / (2 * fraud)
q("E13", "K3", "num", "Dengan compute_class_weight('balanced'), bobot kelas fraud adalah …", f"w = n_samples/(n_classes × n_kelas) = {N3}/(2 × {fraud}) = <b>{f4(w1)}</b>. Bobot non-fraud = {N3}/(2 × {N3 - fraud}) = {f4(N3 / (2 * (N3 - fraud)))}.", "[12] s28-29", answer=r4(w1))
q("E14", "K3", "num", "Data dievaluasi dengan stratified 5-fold cross-validation. Berapa sampel fraud pada data training tiap fold?", f"Fold uji memuat {fraud}/5 = {fraud // 5} fraud, sehingga training memuat {fraud} − {fraud // 5} = <b>{fraud - fraud // 5}</b>.", "[12] s20-21, s81", answer=fraud - fraud // 5, decimals=0)
q("E15", "K3", "multi", "SMOTE dijalankan pada dua sampel fraud bertetangga a = (2, 6) dan b = (6, 2). Centang semua titik yang dapat menjadi data sintetis.",
  "s = λa + (1 − λ)b, 0 ≤ λ ≤ 1 → titik di segmen a–b, yaitu x1 + x2 = 8 dengan 2 ≤ x1 ≤ 6. (4, 4) λ = 0,5 ✓; (3, 5) λ = 0,75 ✓; (5.5, 2.5) λ = 0,125 ✓; (5, 4) jumlah 9 ✗; (7, 1) λ = −0,25 ✗.", "[12] s49-50, s82", answer=[0, 1, 2],
  options=["(4, 4)", "(3, 5)", "(5.5, 2.5)", "(5, 4)", "(7, 1)"])
q("E16", "K3", "mc", "Di mana SMOTE seharusnya diterapkan dalam 5-fold cross-validation?", "Resampling hanya pada data training tiap fold (misalnya lewat imblearn Pipeline). Menerapkan SMOTE sebelum split membocorkan sampel sintetis ke data uji.", "[12] s37, s44, s77", answer=1,
  options=["Pada seluruh data sebelum dibagi fold", "Hanya pada data training di tiap fold", "Hanya pada data testing", "Pada training dan testing secara terpisah"])

# ===================== K4. KNN =====================
P = [("P1", (1, 2), "A", 10), ("P2", (2, 1), "A", 12), ("P3", (4, 4), "B", 20), ("P4", (5, 3), "B", 22), ("P5", (3, 5), "B", 18), ("P6", (2, 4), "A", 14), ("P7", (6, 5), "B", 24)]
qp = (4, 2)
d = sorted(((math.dist(qp, p), nm, c, yv, abs(p[0] - qp[0]) + abs(p[1] - qp[1])) for nm, p, c, yv in P))
group("K4", "Studi kasus 4. KNN classification dan regression",
      "Data training (fitur sudah satu skala):" + table(["Titik", "x1", "x2", "Kelas", "y"], [[nm, p[0], p[1], c, yv] for nm, p, c, yv in P]) + f"Titik uji q = {qp}. Gunakan jarak Euclidean kecuali disebut lain. Isian 4 desimal.")
rank = "Urutan Euclidean: " + ", ".join(f"{x[1]} = {x[0]:.4f} ({x[2]})" for x in d)
q("N1", "K4", "num", "Jarak Euclidean q ke P2 adalah …", f"√((4 − 2)² + (2 − 1)²) = √5 = <b>{f4(math.sqrt(5))}</b>.", "[11] s9", answer=r4(math.sqrt(5)))
q("N2", "K4", "num", "Jarak Manhattan q ke P6 adalah …", "|4 − 2| + |2 − 4| = <b>4</b>.", "[11] s9, s21-22", answer=4, decimals=0)
q("N3", "K4", "mc", "Titik terdekat ketiga dari q adalah …", rank, "[11] s19-23", answer=1, options=["P3", "P2", "P6", "P1"])
v3 = [x[2] for x in d[:3]]; v5 = [x[2] for x in d[:5]]
q("N4", "K4", "mc", "Prediksi kelas q dengan K = 3 adalah …", rank + f"<br>3 terdekat → {', '.join(x[2] for x in d[:3])} → <b>{max(set(v3), key=v3.count)}</b>.", "[11] s19-23", answer=["A", "B"].index(max(set(v3), key=v3.count)), options=["A", "B"])
q("N5", "K4", "mc", "Prediksi kelas q dengan K = 5 adalah …", rank + f"<br>5 terdekat → A {v5.count('A')}, B {v5.count('B')} → <b>{max(set(v5), key=v5.count)}</b>. Hasil berubah dari K = 3; K dipilih dengan cross-validation.", "[11] s16-17", answer=["A", "B"].index(max(set(v5), key=v5.count)), options=["A", "B"])
reg3 = sum(x[3] for x in d[:3]) / 3
q("N6", "K4", "num", "Prediksi KNN regression (K = 3) untuk q adalah …", f"ŷ = ({' + '.join(str(x[3]) for x in d[:3])})/3 = <b>{f4(reg3)}</b>.", "[11] s32-37", answer=r4(reg3))
q("N7", "K4", "num", "Fitur warna {merah, kuning, biru} di-one-hot (100, 010, 001). Berapa jarak Manhattan antara merah dan biru?", "|1 − 0| + |0 − 0| + |0 − 1| = <b>2</b>; semua pasangan berjarak sama, berbeda dengan label encoding 1, 2, 3.", "[11] s26-28", answer=2, decimals=0)
q("N8", "K4", "mc", "Fitur 1 bernilai 1–2, fitur 2 bernilai 100–200. Apa akibatnya pada KNN tanpa normalisasi?", "Jarak didominasi fitur 2; contoh slide salah klasifikasi dan menjadi benar setelah normalisasi.", "[11] s24-25", answer=0,
  options=["Jarak didominasi fitur 2 sehingga prediksi bisa salah", "Tidak berpengaruh", "Hanya waktu komputasi yang naik", "KNN otomatis menormalisasi"])

# ===================== K5. Probabilitas dan Bayes =====================
T5, M, D5, B5 = 200, 80, 60, 24
pM, pD, pMD = M / T5, D5 / T5, B5 / T5
group("K5", "Studi kasus 5. Probabilitas dan Bayes theorem",
      f"Bagian I. Dari {T5} mahasiswa, {M} mengambil mata kuliah ML (M), {D5} ikut klub Data Science (D), dan {B5} melakukan keduanya. Satu mahasiswa dipilih acak.<br>"
      "Bagian II. Prevalensi suatu penyakit 1%. Alat tes memiliki sensitivity 0,95 dan specificity 0,90. Isian 4 desimal.")
q("R1", "K5", "num", "P(M ∪ D) adalah …", f"P(M) + P(D) − P(M ∩ D) = {pM} + {pD} − {pMD} = <b>{f4(pM + pD - pMD)}</b>.", "[13] s8", answer=r4(pM + pD - pMD))
q("R2", "K5", "num", "Peluang mahasiswa mengambil M tetapi bukan anggota D adalah …", f"({M} − {B5})/{T5} = <b>{f4((M - B5) / T5)}</b>.", "[13] s8", answer=r4((M - B5) / T5))
q("R3", "K5", "num", "P(D | M) adalah …", f"P(D|M) = P(M ∩ D)/P(M) = {B5}/{M} = <b>{f4(B5 / M)}</b>.", "[13] s10", answer=r4(B5 / M))
q("R4", "K5", "mc", "Apakah kejadian M dan D independen?", f"P(M)P(D) = {pM} × {pD} = {f4(pM * pD)} dan P(M ∩ D) = {f4(pMD)}. Sama, jadi <b>independen</b>; setara dengan P(D|M) = P(D) = {pD}.", "[13] s15", answer=0,
  options=["Independen, karena P(M ∩ D) = P(M)P(D)", "Tidak independen, karena keduanya bisa terjadi bersamaan", "Mutually exclusive", "Tidak dapat ditentukan"])
prev, se, sp = 0.01, 0.95, 0.90
pp = se * prev + (1 - sp) * (1 - prev); ppv = se * prev / pp; pneg = 1 - pp; fnr = (1 - se) * prev / pneg
q("R5", "K5", "num", "P(tes positif) adalah …", f"P(+) = P(+|S)P(S) + P(+|¬S)P(¬S) = 0,95·0,01 + 0,10·0,99 = <b>{f4(pp)}</b>.", "[13] s39-40", answer=r4(pp))
q("R6", "K5", "num", "P(sakit | tes positif) adalah …", f"Bayes: 0,0095/{f4(pp)} = <b>{f4(ppv)}</b>.", "[13] s41-42; ws2 Q2", answer=r4(ppv))
q("R7", "K5", "num", "P(sakit | tes negatif), nyatakan dalam satuan ×10⁻⁴ (contoh: 0,00012 ditulis 1.2) …",
  f"P(−|S)P(S)/P(−) = 0,05·0,01/{f4(pneg)} = {fnr:.4e} → <b>{f4(fnr * 1e4)}</b> × 10⁻⁴.", "[13] s41-42; ws2 Q2", answer=r4(fnr * 1e4))
prev2 = 0.2; pp2 = se * prev2 + (1 - sp) * (1 - prev2); ppv2 = se * prev2 / pp2
q("R8", "K5", "num", "Bila alat yang sama dipakai di populasi dengan prevalensi 20%, P(sakit | positif) menjadi …", f"P(+) = 0,95·0,2 + 0,1·0,8 = {f4(pp2)}; P(S|+) = 0,19/{f4(pp2)} = <b>{f4(ppv2)}</b>.", "[13] s41-42; ws2 Q2", answer=r4(ppv2))
q("R9", "K5", "mc", "Mengapa P(sakit | positif) pada prevalensi 1% jauh lebih kecil daripada sensitivity 0,95?",
  "Prevalensi kecil: kelompok sehat yang besar menghasilkan false positive yang jumlahnya melampaui true positive.", "[13] s41-46", answer=1,
  options=["Karena alat tes tidak akurat", "Karena prevalensi kecil sehingga false positive dari kelompok sehat mendominasi", "Karena sensitivity dan specificity dijumlahkan", "Karena tes positif dan sakit independen"])

# ===================== K6. Likelihood dan Naive Bayes =====================
h, nflip = 9, 15
L5 = 0.5 ** nflip; L6 = 0.6 ** h * 0.4 ** (nflip - h); ll6 = h * math.log(0.6) + (nflip - h) * math.log(0.4)
pen = {"n": 5, "link": 4, "waktu": {"Pagi": 0, "Siang": 1, "Malam": 4}, "x": [30, 34, 28, 36, 32]}
nor = {"n": 7, "link": 2, "waktu": {"Pagi": 3, "Siang": 3, "Malam": 1}, "x": [20, 24, 18, 22, 26, 21, 23]}
for c in (pen, nor):
    c["mu"] = sum(c["x"]) / c["n"]; c["var"] = sum((v - c["mu"]) ** 2 for v in c["x"]) / c["n"]
Ntot = pen["n"] + nor["n"]; pPen = pen["n"] / Ntot; pNor = nor["n"] / Ntot
group("K6", "Studi kasus 6. Likelihood dan Naive Bayes",
      f"Bagian I. Sebuah koin dilempar {nflip} kali secara i.i.d. dan muncul {h} head. θ = P(head). L(θ) = θ^{h}(1 − θ)^{nflip - h}. Log adalah logaritma natural.<br>"
      "Bagian II. Naive Bayes untuk mengklasifikasikan pesan <b>Penipuan</b> atau <b>Normal</b>. Fitur: Link (Ya/Tidak), Waktu kirim (Pagi/Siang/Malam), dan Panjang pesan (kata, Gaussian dengan variance pembagi n)." +
      table(["Kelas", "n", "Link = Ya", "Pagi / Siang / Malam", "Panjang"], [["Penipuan", 5, 4, "0 / 1 / 4", ", ".join(map(str, pen["x"]))], ["Normal", 7, 2, "3 / 3 / 1", ", ".join(map(str, nor["x"]))]]) +
      "Isian 4 desimal; bila diminta dalam satuan ×10⁻ᵏ, tulis mantisanya saja.")
q("L1", "K6", "num", "L(0,5) dalam satuan ×10⁻⁵ adalah …", f"0,5^{nflip} = {L5:.4e} → <b>{f4(L5 * 1e5)}</b>.", "[13] s35-37; ws2 Q3", answer=r4(L5 * 1e5))
q("L2", "K6", "num", "L(0,6) dalam satuan ×10⁻⁵ adalah …", f"0,6⁹ × 0,4⁶ = {L6:.4e} → <b>{f4(L6 * 1e5)}</b>. L(0,6) > L(0,5), jadi θ = 0,6 lebih didukung data.", "[13] s35-37; ws2 Q3", answer=r4(L6 * 1e5))
q("L3", "K6", "num", "Nilai MLE θ̂ adalah …", f"θ̂ = #head/n = {h}/{nflip} = <b>{f4(h / nflip)}</b>.", "[14] s11-12; ws2 Q3", answer=r4(h / nflip))
q("L4", "K6", "num", "Log-likelihood pada θ = 0,6 adalah …", f"9 ln 0,6 + 6 ln 0,4 = 9({math.log(0.6):.4f}) + 6({math.log(0.4):.4f}) = <b>{f4(ll6)}</b>. Log mengubah perkalian menjadi penjumlahan dan mencegah underflow.", "[13] s36; [14] s10", answer=r4(ll6))
x1 = {"link": "Ya", "waktu": "Malam", "x": 30}
def lik(c, link, w, x, lap=False):
    pl = ((c["link"] if link == "Ya" else c["n"] - c["link"]) + (1 if lap else 0)) / (c["n"] + (2 if lap else 0))
    pw = (c["waktu"][w] + (1 if lap else 0)) / (c["n"] + (3 if lap else 0))
    return pl, pw, npdf(x, c["mu"], c["var"])
lp = lik(pen, "Ya", "Malam", 30); ln_ = lik(nor, "Ya", "Malam", 30)
sP = pPen * lp[0] * lp[1] * lp[2]; sN = pNor * ln_[0] * ln_[1] * ln_[2]; post1 = sP / (sP + sN)
items6 = [("L5", "P(Penipuan)", pPen, f"5/12"), ("L6", "P(Link = Ya | Penipuan)", lp[0], "4/5"), ("L7", "P(Waktu = Malam | Penipuan)", lp[1], "4/5"),
          ("L8", "P(Link = Ya | Normal)", ln_[0], "2/7"), ("L9", "P(Waktu = Malam | Normal)", ln_[1], "1/7"),
          ("L10", "Mean panjang kelas Penipuan", pen["mu"], "(30 + 34 + 28 + 36 + 32)/5"), ("L11", "Variance panjang kelas Penipuan", pen["var"], "Σ(x − 32)²/5 = (4 + 4 + 16 + 16 + 0)/5"),
          ("L12", "Mean panjang kelas Normal", nor["mu"], "154/7"), ("L13", "Variance panjang kelas Normal", nor["var"], "(4 + 4 + 16 + 0 + 16 + 1 + 1)/7")]
for nm, lab, val, how in items6:
    q(nm, "K6", "num", f"{lab} adalah …", f"{lab} = {how} = <b>{f4(val)}</b>.", "[14] s11-14; ws2 Q6", answer=r4(val))
q("L14", "K6", "num", "Untuk x⁽¹⁾ = (Link = Ya, Waktu = Malam, Panjang = 30): density f(30 | Penipuan) adalah …", f"N(30; μ = {pen['mu']:g}, σ² = {pen['var']:g}) = exp(−(30 − 32)²/(2·8))/√(2π·8) = <b>{f4(lp[2])}</b>.", "[13] s28; [14] s14", answer=r4(lp[2]))
q("L15", "K6", "num", "Untuk x⁽¹⁾: density f(30 | Normal) dalam satuan ×10⁻⁴ adalah …", f"N(30; 22, 6) = exp(−64/12)/√(12π) = {ln_[2]:.4e} → <b>{f4(ln_[2] * 1e4)}</b>. Sangat kecil karena 30 jauh dari mean Normal.", "[13] s28; [14] s14", answer=r4(ln_[2] * 1e4))
q("L16", "K6", "num", "Skor tak ternormalisasi kelas Penipuan untuk x⁽¹⁾, dalam satuan ×10⁻² …", f"P(Pen)·P(Ya|Pen)·P(Malam|Pen)·f(30|Pen) = (5/12)(0,8)(0,8)({lp[2]:.6f}) = {sP:.4e} → <b>{f4(sP * 1e2)}</b>.", "[14] s15, s28-34", answer=r4(sP * 1e2))
q("L17", "K6", "num", "P(Penipuan | x⁽¹⁾) setelah normalisasi adalah …", f"Skor Normal = (7/12)(2/7)(1/7)({ln_[2]:.4e}) = {sN:.4e}. P = {sP:.4e}/({sP:.4e} + {sN:.4e}) = <b>{f4(post1)}</b> → Penipuan.", "[14] s9, s15", answer=r4(post1))
lp2n = lik(pen, "Tidak", "Pagi", 27); lp2 = lik(pen, "Tidak", "Pagi", 27, lap=True); ln2 = lik(nor, "Tidak", "Pagi", 27, lap=True)
sP2 = pPen * lp2[0] * lp2[1] * lp2[2]; sN2 = pNor * ln2[0] * ln2[1] * ln2[2]; post2 = sP2 / (sP2 + sN2)
q("L18", "K6", "num", "Untuk x⁽²⁾ = (Link = Tidak, Waktu = Pagi, Panjang = 27) <b>tanpa</b> smoothing, skor kelas Penipuan adalah …", f"P(Pagi | Penipuan) = 0/5 = 0, sehingga seluruh perkalian menjadi <b>0</b> walaupun fitur lain mendukung.", "[14] s36-37", answer=0, decimals=4)
q("L19", "K6", "mc", "Masalah pada L18 disebut …", "Zero-frequency problem: satu frekuensi nol membuat posterior nol dan mengabaikan informasi fitur lain. Solusinya Laplace estimator.", "[14] s37; ws2 Q6", answer=1,
  options=["Underflow", "Zero-frequency problem", "Curse of dimensionality", "Missing value"])
q("L20", "K6", "num", "Dengan Laplace smoothing (+1; K = 2 untuk Link, K = 3 untuk Waktu), P(Waktu = Pagi | Penipuan) adalah …", f"(0 + 1)/(5 + 3) = <b>{f4(lp2[1])}</b>. P(Link = Tidak | Penipuan) = (1 + 1)/(5 + 2) = {f4(lp2[0])}.", "[14] s37", answer=r4(lp2[1]))
q("L21", "K6", "num", "Dengan Laplace, P(Link = Tidak | Normal) adalah …", f"(5 + 1)/(7 + 2) = <b>{f4(ln2[0])}</b>. Smoothing juga diterapkan pada kelas Normal; P(Pagi | Normal) = (3 + 1)/(7 + 3) = {f4(ln2[1])}.", "[14] s37; ws2 Q6", answer=r4(ln2[0]))
q("L22", "K6", "num", "P(Penipuan | x⁽²⁾) setelah Laplace dan normalisasi adalah …",
  f"f(27|Pen) = {lp2[2]:.6f}; f(27|Nor) = {ln2[2]:.6f}.<br>Skor Pen = (5/12)({f4(lp2[0])})({f4(lp2[1])})({lp2[2]:.6f}) = {sP2:.4e}.<br>Skor Nor = (7/12)({f4(ln2[0])})({f4(ln2[1])})({ln2[2]:.6f}) = {sN2:.4e}.<br>P(Pen|x) = <b>{f4(post2)}</b> → prediksi {'Penipuan' if post2 > 0.5 else 'Normal'}.",
  "[14] s15, s37", answer=r4(post2))
q("L23", "K6", "mc", "Ekspresi yang dimaksimalkan Naive Bayes saat memilih kelas adalah …", "Naive Bayes memilih argmax posterior P(C | fitur) ∝ P(C)·ΠP(fitur|C). P(fitur|C) tanpa prior adalah maximum likelihood, bukan Naive Bayes.", "[14] s7-9; ws2 Q6", answer=2,
  options=["P(fitur | C)", "P(fitur)", "P(C | fitur) ∝ P(C)·ΠP(fitur_i | C)", "P(C) saja"])

# ===================== K7. EDA, preparation, feature selection =====================
data7 = [11, 4, 7, 9, 30, 6, 8, 5, 10]
s7 = sorted(data7); n7 = len(s7); med = s7[n7 // 2]
def median(v): v = sorted(v); m = len(v); return v[m // 2] if m % 2 else (v[m // 2 - 1] + v[m // 2]) / 2
Q1, Q3 = median(s7[:n7 // 2]), median(s7[n7 // 2 + 1:]); IQR = Q3 - Q1; RLB = Q1 - 1.5 * IQR; RUB = Q3 + 1.5 * IQR
HS = H(6, 4); Hm = 0.5 * H(4, 1) + 0.5 * H(2, 3)
chi = (4 - 3) ** 2 / 3 + (1 - 2) ** 2 / 2 + (2 - 3) ** 2 / 3 + (3 - 2) ** 2 / 2
group("K7", "Studi kasus 7. EDA, data preparation, dan feature selection",
      f"Bagian I. Waktu tunggu (menit) {n7} pelanggan: {', '.join(map(str, data7))}. Q1 = median separuh bawah, Q3 = median separuh atas (median tidak ikut).<br>"
      "Bagian II. Data 10 pelanggan: target Beli = 6 Ya, 4 Tidak. Fitur Member: Member = Ya → 4 Ya, 1 Tidak; Member = Tidak → 2 Ya, 3 Tidak. Gunakan log₂. Isian 4 desimal.")
sq = f"Urut: {', '.join(map(str, s7))}; median {med}; Q1 = {Q1}; Q3 = {Q3}."
q("D1", "K7", "num", "Q3 adalah …", sq, "[03] s29-31", answer=r4(Q3))
q("D2", "K7", "num", "RLB (batas bawah wajar) adalah …", sq + f" IQR = {IQR}; RLB = Q1 − 1,5·IQR = {Q1} − {1.5 * IQR} = <b>{f4(RLB)}</b>.", "[03] s32-33", answer=r4(RLB))
q("D3", "K7", "num", "RUB (batas atas wajar) adalah …", sq + f" RUB = Q3 + 1,5·IQR = {Q3} + {1.5 * IQR} = <b>{f4(RUB)}</b>.", "[03] s32-33", answer=r4(RUB))
q("D4", "K7", "num", "Banyak outlier menurut aturan IQR adalah …", f"Nilai di luar [{RLB}, {RUB}]: hanya 30 → <b>1</b>.", "[03] s32-33", answer=1, decimals=0)
q("D5", "K7", "mc", "Mean data lebih besar dari median. Distribusinya …", f"Mean {sum(s7) / n7:.4f} > median {med}: mean tertarik ke ekor kanan oleh 30 → skewed right, skewness positif.", "[03] s35-36", answer=1,
  options=["Skewed left", "Skewed right, skewness positif", "Simetris", "Platykurtic"])
mm = (7 - min(s7)) / (max(s7) - min(s7))
q("D6", "K7", "num", "Min-max scaling untuk x = 7 adalah …", f"(7 − {min(s7)})/({max(s7)} − {min(s7)}) = <b>{f4(mm)}</b>.", "[04] s35; [05] s25", answer=r4(mm))
q("D7", "K7", "num", "Entropy target H(S) adalah …", f"−0,6 log₂ 0,6 − 0,4 log₂ 0,4 = <b>{f4(HS)}</b>.", "[05] s46-48", answer=r4(HS))
q("D8", "K7", "num", "Information gain fitur Member adalah …", f"H(Ya) = H(4/5, 1/5) = {f4(H(4, 1))}; H(Tidak) = H(2/5, 3/5) = {f4(H(2, 3))}; entropy setelah split = {f4(Hm)}. Gain = {f4(HS)} − {f4(Hm)} = <b>{f4(HS - Hm)}</b>.", "[05] s47-49", answer=r4(HS - Hm))
q("D9", "K7", "num", "Statistik Chi-square antara Member dan Beli adalah …", f"E = baris × kolom/N: 3, 2, 3, 2. χ² = 1/3 + 1/2 + 1/3 + 1/2 = <b>{f4(chi)}</b>.", "[05] s41-45", answer=r4(chi))
q("D10", "K7", "multi", "Centang semua penanganan missing value yang sesuai materi.", "Cek ke pengumpul data; drop; isi mean untuk numerik, mode untuk kategorikal, konstanta, nearest neighbor, atau fungsi lain; atau biarkan. Mean untuk kategorikal tidak terdefinisi.", "[04] s16-21", answer=[0, 1, 3, 4],
  options=["Menanyakan ke pengumpul data", "Mengisi kolom numerik dengan mean", "Mengisi kolom kategorikal dengan mean", "Mengisi kolom kategorikal dengan mode", "Mengisi dari baris paling mirip (nearest neighbor)"])

# ===================== K8. Konsep AI dan Data Science =====================
group("K8", "Studi kasus 8. AI dan Data Science", "Pilih jawaban yang paling tepat.")
q("A1", "K8", "mc", "“Computational Intelligence is the study of the design of intelligent agents” termasuk paradigma …", "Perancangan agen yang bertindak benar = acting rationally.", "[01] s11, s16", answer=3,
  options=["Thinking humanly", "Acting humanly", "Thinking rationally", "Acting rationally"])
q("A2", "K8", "multi", "Centang semua sifat lingkungan untuk agen taksi otonom.", "Taxi driving: partially observable, multi-agent, nondeterministic, sequential, dynamic, continuous.", "[01] s22-23", answer=[0, 1, 2, 3],
  options=["Partially observable", "Multi-agent", "Nondeterministic", "Dynamic", "Discrete", "Episodic"])
q("A3", "K8", "mc", "Sistem yang merekomendasikan jumlah stok optimal minggu depan dari hasil prediksi permintaan adalah analytics …", "Prescriptive merumuskan rekomendasi tindakan terbaik berdasarkan analytics prediktif.", "[02] s11", answer=3,
  options=["Descriptive", "Diagnostic", "Predictive", "Prescriptive"])
q("A4", "K8", "mc", "Pada CRISP-DM, tahap yang bolak-balik dengan data preparation adalah …", "Data preparation ⇄ modeling.", "[02] s23", answer=1, options=["Data understanding", "Modeling", "Evaluation", "Deployment"])

# ===================== Bagian B: essay =====================
q("ES1", None, "essay", "Bank ingin mendeteksi fraud pada 50.000 transaksi (0,8% fraud). Fitur: nominal (numerik, ada outlier), kanal (ATM/mobile/web), tanggal buka rekening, dan 5% missing di pendapatan. Rancang pipeline dari preprocessing sampai evaluasi beserta alasannya.",
  "Lihat jawaban model dan rubrik.", "[04]; [05]; [09]; [12]", sec="B",
  rubric=["Preprocessing: imputasi pendapatan, age encoding tanggal, one-hot kanal, penanganan outlier", "Validasi stratified; transformasi dan resampling hanya di data training (imblearn Pipeline)",
          "Imbalance: SMOTE/varian atau cost-sensitive dengan alasan", "Metrik: bukan accuracy; recall, F2, G-mean, ROC/PR-AUC dikaitkan biaya FN"],
  model="Imputasi pendapatan dengan mean/median atau nearest neighbor (fit di training); umur akun = durasi hari (age encoding); kanal one-hot karena nominal; nominal di-log atau pakai model tree yang robust outlier. Stratified 5-fold agar fraud ada di tiap fold. SMOTE di dalam imblearn Pipeline atau class_weight='balanced'/cost FN ≫ FP. Model RF atau tree dengan max_depth dituning CV. Metrik: accuracy dilarang (dummy 99,2%); recall/F2 karena FN paling mahal, ditambah PR-AUC/ROC-AUC.")
q("ES2", None, "essay", "Jelaskan mengapa Random Forest umumnya lebih baik daripada satu decision tree, dikaitkan dengan bias-variance tradeoff. Sertakan peran bootstrap, subset fitur acak, dan majority vote.",
  "Lihat jawaban model dan rubrik.", "[07a] s64; [08] s17-32; [10] s29-30", sec="B",
  rubric=["Tree dalam: low bias, high variance, tidak stabil", "Bootstrap + agregasi menurunkan variance (σ²/k untuk prediksi i.i.d.)", "Subset fitur acak menurunkan korelasi antartree", "Bias ≈ base model; trade-off waktu dan explainability"],
  model="Tree penuh low bias tetapi high variance dan tidak stabil. RF melatih banyak tree pada bootstrap sample berbeda lalu vote/rata-rata, sehingga variance turun (σ²/k untuk prediksi i.i.d.) dengan bias kira-kira tetap. Subset d ≪ D fitur per node membuat tree kurang berkorelasi sehingga error tidak terulang. Konsekuensi: lebih banyak tree, lebih lambat, sulit dijelaskan.")
q("ES3", None, "essay", "Bandingkan KNN dan Naive Bayes untuk 1 juta sampel dengan 20 fitur campuran (numerik dan kategorikal): preprocessing, asumsi, kompleksitas, dan masalah yang mungkin muncul.",
  "Lihat jawaban model dan rubrik.", "[11] s24-42; [14] s5-41", sec="B",
  rubric=["KNN: normalisasi, encoding, pilih K dan jarak; tanpa training, testing O(knd)", "NB: generative, independen bersyarat kelas; Gaussian + categorical, P(X|y)=P(Xn|y)P(Xc|y)",
          "Masalah NB: zero-frequency (Laplace), underflow (log-likelihood), missing (abaikan suku)", "Kesimpulan beralasan untuk 1 juta sampel"],
  model="KNN menyimpan semua sampel, prediksi O(knd) sangat mahal untuk 1 juta data; perlu normalisasi, one-hot untuk nominal, K via cross-validation. NB generative dengan asumsi independen bersyarat kelas; numerik Gaussian, kategorikal frekuensi, gabung P(X|y)=P(Xn|y)P(Xc|y); training dan prediksi cepat. Masalah NB: zero-frequency (Laplace), underflow (log-likelihood). Untuk data sebesar ini NB lebih efisien; KNN bisa akurat bila batas nonlinear tetapi mahal.")

auto = [x for x in Q if x["section"] == "A"]
pa = round(70 / len(auto), 4)
for x in Q: x["points"] = pa if x["section"] == "A" else 10
exam = {"id": "kasdad-uts-simulasi-2", "title": "Simulasi UTS KASDAD (CSGE603130) Gasal 2026/2027", "course": "Kecerdasan Artifisial dan Sains Data Dasar",
        "duration_minutes": 150,
        "rules": ["Durasi 150 menit, mengikuti UTS KASDD. Soal disusun bergaya worksheet SCeLE: studi kasus berantai.",
                  "Bagian A autograde: pilihan ganda, centang semua yang benar, dan isian angka. Isian 4 desimal kecuali disebut lain; titik atau koma desimal diterima.",
                  "Bagian B essay: nilai sendiri dengan rubrik 0, 0,5, atau 1 per kriteria.",
                  "Open notes 1 lembar A4 dan kalkulator standalone. Latihan buatan sendiri dari materi /data-science, bukan soal resmi."],
        "sections": [{"id": "A", "title": "Bagian A, autograde", "points": 70}, {"id": "B", "title": "Bagian B, essay", "points": 30}],
        "groups": G, "questions": Q}
Path(sys.argv[1]).write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(G)} studi kasus, {len(auto)} soal autograde ({pa} poin), {len(Q) - len(auto)} essay")
