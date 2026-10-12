# KASDAD, skill /data-science

Korpus kuliah KASDAD (CSGE603130 Kecerdasan Artifisial dan Sains Data Dasar, Fasilkom UI, Gasal 2026/2027) dan skill `/data-science` yang menjawab dari korpus itu dengan rujukan nomor slide.

## Pakai

Di Claude Code ketik `/data-science`, lalu salah satu:

| Contoh | Yang terjadi |
|---|---|
| `/data-science jelaskan SMOTE` | Definisi, kapan dipakai, langkah matematis, contoh angka, rujukan slide |
| `/data-science kerjakan` + gambar soal | Pengerjaan langkah demi langkah, dicek ulang, dibulatkan sesuai soal |
| `/data-science periksa` + jawaban | Penilaian per butir dan letak kesalahan pertama |
| `/data-science latihan PCA 5` | Lima soal gaya worksheet beserta kunci |
| `/data-science pipeline` + kasus | Pemilihan pipeline dan model dengan alasan dari slide |
| `/data-science tambah materi` | Sinkronisasi materi baru dan pembaruan peta materi |

Di Codex, sebut "pakai skill data-science", atau ketik `/data-science` setelah `python3 _system/scripts/codex_prompts.py` dijalankan di mesin itu.

## Tambah materi kuliah

```sh
cd '/Users/wira/Documents/WiraOS/Business/InnovationKit/Products/kasdad'
python3 scripts/sync_sources.py --course-dir '/Users/wira/Documents/WiraOS/Study/FasilkomUI/MIK DIK/Courses/kasdad_agu-2026'
python3 scripts/sync_sources.py --course-dir '/Users/wira/Documents/WiraOS/Study/FasilkomUI/MIK DIK/Courses/kasdad_agu-2026' --check
```

Skrip menyalin berkas baru berdasarkan SHA-256 dan tidak pernah menghapus versi lama. Pola berkas yang ikut tersalin dan pemetaan topiknya diatur di `sources/topics.json`. Setelah sinkronisasi, materi baru perlu dibaca lalu dimasukkan ke `skills/data-science/references/`. Mode `tambah materi` di skill melakukan langkah itu.

## Isi

- `skills/data-science/SKILL.md`: prosedur skill dan enam mode.
- `skills/data-science/references/course-map.md`: peta topik ke halaman slide.
- `skills/data-science/references/formulas.md`: rumus dengan angka kontrol dari slide.
- `skills/data-science/references/exam-patterns.md`: bentuk soal, sinyal dosen, dan selisih antar sumber.
- `sources/`: salinan materi, ekstrak teks, `manifest.json`, `topics.json`.

## Versi publik

Repo ini private dan menyimpan semuanya. Versi publiknya ada di `github.com/wiraperdana/data-science-skill`, tanpa materi pihak ketiga: slide dosen, worksheet, soal, catatan kelas, ekstrak teks slide, dan transkripsi slide bergambar. Daftarnya ada di `.publik-kecuali`.

Terbitkan ulang setelah ada perubahan:

```sh
scripts/terbitkan_publik.sh --cek   # lihat berkas yang akan terbit
scripts/terbitkan_publik.sh         # bangun commit publik lalu push ke remote "publik"
```

Pemakai versi publik membangun korpus sendiri dari materi kuliahnya dengan `scripts/sync_sources.py`, karena skill menjawab dari `sources/text/`.
