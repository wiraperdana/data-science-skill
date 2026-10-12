---
schema: personal-os/status@1
level: project
project: kasdad
title: "KASDAD, skill data-science"
area: Business
entity: InnovationKit
stage: active
started: 2026-10-11
owner: wira
last_updated: 2026-10-11
next_action: "Sinkronkan materi KASDAD pasca-UTS (linear regression, logistic, Ridge/Lasso, clustering, neural network) begitu slidenya terbit."
blockers: []
tags: [kasdad, skill, data-science]
tasks:
  - id: T1
    title: "Salin dan inventaris materi KASDAD [00] sampai [14], notes, worksheet, dan soal"
    status: done
  - id: T2
    title: "Tulis skill data-science: SKILL.md, peta materi, lembar rumus, pola ujian"
    status: done
  - id: T3
    title: "Pasang symlink data-science di ~/.claude/skills dan ~/.agents/skills"
    status: done
  - id: T4
    title: "Tambahkan materi pasca-UTS saat slidenya terbit"
    status: backlog
---
# Catatan

## Dari mana status ini disimpulkan

| Task | Bukti di disk |
|---|---|
| T1 | `sources/manifest.json` memuat 73 sumber; `scripts/sync_sources.py --check` melaporkan 0 masalah pada 2026-10-11. |
| T2 | `skills/data-science/SKILL.md` dan tiga berkas di `skills/data-science/references/`. |
| T3 | Symlink `~/.claude/skills/data-science` dan `~/.agents/skills/data-science` menunjuk ke `skills/data-science/`. |
| T4 | Silabus menjadwalkan materi pasca-UTS mulai 26 Oktober 2026; belum ada slidenya di folder kuliah per 11 Oktober 2026. |

## Yang belum pasti

- Format resmi UTS dan UAS belum tercatat di korpus. Pola soal di `references/exam-patterns.md` disimpulkan dari worksheet 1 dan 2 serta catatan kelas.
- Set `soal-09` sampai `soal-12` di korpus dibuat sendiri, bukan soal resmi dosen.
