---
schema: personal-os/agents@1
level: project
name: "kasdad"
area: Business
title: "KASDAD, skill data-science"
---

# Project: KASDAD, skill data-science

Posisi: `Business` / `InnovationKit` / `Products` / `kasdad`.

Slug kanonik project ini `kasdad`. Ikuti aturan Entity `InnovationKit`, Area `Business`, dan root. Yang di bawah ini hanya tambahan khusus project ini.

## Tujuan

Menyimpan korpus kuliah KASDAD (CSGE603130, Gasal 2026/2027) dan skill `/data-science`, yang menjelaskan konsep, mengerjakan dan memeriksa soal, membuat latihan, serta memilih pipeline model dengan rujukan slide. Kuliah masih berjalan, jadi korpusnya bertambah lewat `scripts/sync_sources.py`.

Project ini selesai saat nilai akhir KASDAD Gasal 2026/2027 keluar dan seluruh materi semester sudah masuk korpus.

## Struktur

| Path | Isi |
|---|---|
| `skills/data-science/` | Skill: `SKILL.md`, `references/` (peta materi, rumus, pola ujian), `agents/openai.yaml` |
| `sources/files/` | Salinan materi dari folder kuliah, path relatif dipertahankan |
| `sources/text/` | Ekstrak teks PDF dan HTML per halaman |
| `sources/manifest.json` | Inventaris, topik, jenis, dan SHA-256 setiap sumber |
| `sources/topics.json` | Aturan pemetaan berkas ke topik, diedit saat materi baru masuk |
| `scripts/sync_sources.py` | Sinkronisasi dan pemeriksaan korpus |

Sumber kebenarannya tetap folder kuliah `Study/FasilkomUI/MIK DIK/Courses/kasdad_agu-2026/`. Folder ini hanya salinan untuk skill.

## Konvensi lokal

Skill dipasang sebagai symlink bernama `data-science` di `~/.claude/skills/` dan `~/.agents/skills/`, menunjuk ke `skills/data-science/`. Nama produk `kasdad`, nama perintah `/data-science`. Keduanya sengaja berbeda atas permintaan Wira, 11 Oktober 2026.

## Jangan

Jangan menghapus atau menimpa isi `sources/files/`. Versi lama adalah jejak audit untuk rujukan slide, dan skrip sinkronisasi sengaja hanya menambah.

Jangan memperbarui `references/` tanpa membaca sumber barunya sampai habis. Skill ini dipercaya karena setiap rujukan slidenya bisa dicek.

## Status

Lihat `STATUS.md`. Perbarui setiap kali korpus atau skill berubah, lalu tawarkan `/monitor-refresh`.
