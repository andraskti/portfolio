# 📋 PROMPT PORTOFOLIO — Siap Pakai Ulang

Dokumen ini berisi prompt lengkap untuk membuat ulang website portofolio seperti
`index.html` di folder ini — cukup salin, isi datamu, kirim ke AI apa pun
(ZCode, ChatGPT, Gemini, dll). Tidak perlu menjelaskan dari nol lagi.

---

## 🚀 CARA PAKAI

1. Salin seluruh blok **PROMPT UTAMA** di bawah.
2. Ganti setiap bagian `[DALAM KURUNG SIKU]` dengan datamu.
3. Kirim ke AI. Kalau punya foto, lampirkan + tulis urutan & kategorinya.
4. Setelah jadi, lanjutkan dengan **PROMPT REVISI** (bawah) sesuai kebutuhan.

---

## 📝 PROMPT UTAMA (salin mulai dari sini)

```
Buatkan website PORTOFOLIO PRIBADI satu halaman untuk saya, dengan spesifikasi:

== TUJUAN ==
Portofolio profesional untuk melamar kerja/magang, menonjolkan pengalaman
dan bukti karya (foto kegiatan + video). Bahasa Indonesia untuk semua teks.

== TEKNOLOGI ==
- SATU file saja: index.html (HTML + CSS + vanilla JavaScript, tanpa framework)
- Font via Google Fonts CDN: heading "Syne", body "Inter", label/meta "JetBrains Mono"
- Semua gambar lokal (foto profil + galeri), sudah dikompres < 100 KB per file
- Beri komentar ✏️ di setiap bagian yang mudah diedit pengguna

== DESAIN: DARK LIQUID GLASS ala iOS — anti-template, TANPA EMOJI ==
- DILARANG memakai emoji sebagai ikon/dekorasi. Semua ikon = SVG inline atau
  penanda tipografis: indeks "P.01", panah "→/↗", slash "/" di marquee, "+"
  sebagai bullet list.
- Latar #050509 dengan 4 orb ambient berwarna (violet #6a4dff, biru #2f6bff,
  pink #e04fb0, amber #ffb36b) blur 90px yang melayang terus (keyframes drift)
  dan ber-parallax mengikuti mouse & scroll — inilah "sumber cahaya" kaca.
- Semua permukaan = LIQUID GLASS: background gradasi putih .10→.035 +
  backdrop-filter blur(26px) saturate(170%), border putih .16, highlight
  tepi atas (inset 0 1px 0 putih .18), bayangan 0 24px 60px hitam .5,
  radius 18-26px. Kilau spesular di sudut atas + "sheen sweep" (sapuan
  cahaya diagonal) saat hover.
- Tekstur grain halus (SVG feTurbulence data-URI, opacity 4%).
- Tipografi editorial: judul Syne uppercase besar; nama hero 3 baris uppercase
  dengan glow lembut; label/tanggal/badge JetBrains Mono uppercase.
- Animasi: custom cursor (dot + ring lag, pointer:fine), progress bar baca,
  marquee skill berjalan (hover = pause), tombol magnetik, kartu proyek tilt
  3D mengikuti mouse, reveal fade-up (IntersectionObserver + fallback scroll),
  count-up angka, teks peran efek ketik di dalam pill kaca, chip skill
  stagger pop, jam lokal WIB live di footer, panah ↗ saat hover,
  hormati prefers-reduced-motion.
- Header section bernomor: "(01) TENTANG SAYA" gaya mono.
- Navbar = pill kaca melayang (fixed, radius 99); menu mobile = panel kaca
  absolut di bawah pill. Catatan penting: backdrop-filter membuat elemen
  fixed di dalamnya menjadi relative — pakai absolute + overflow visible.
- Responsif penuh: menu hamburger di bawah 768px, grid menyesuaikan

== STRUKTUR (urut) ==
1. NAVBAR: logo inisial [INISIAL.] dengan gradasi, link Beranda/Tentang/
   Pengalaman/Proyek/Galeri/Keahlian, tombol "Kontak" gradasi
2. HERO: badge hijau "Terbuka untuk kesempatan baru", H1 "Halo, saya [NAMA]"
   dengan gradasi beranimasi, peran berputar (efek ketik), bio 2-3 baris,
   2 tombol (Lihat Proyek / Hubungi Saya), ikon sosmed SVG inline
3. TENTANG: foto kotak dengan bracket sudut gaya viewfinder (grayscale →
   berwarna saat hover), chip lokasi mono, bio 2-3 paragraf, 3 statistik
   bergaya editorial (garis atas + angka count-up, tanpa kartu kotak)
4. PENGALAMAN: timeline vertikal (garis gradasi + titik), kartu berisi:
   role, perusahaan + lokasi, badge periode (warna per jenis: ungu=part-time,
   biru=magang, pink=freelance), 3 bullet tugas, chip keahlian.
   Urutan pengalaman dari terbaru. Pengalaman saya:
   [role | perusahaan, lokasi | periode, jenis | tugas 1; tugas 2; tugas 3]
5. PROYEK: tombol filter kategori (Semua + kategori), kartu flat berisi
   indeks "P.01", label kategori mono, judul, deskripsi 1-2 kalimat, tag mono,
   baris dampak berprefiks panah "→", panah "↗" muncul saat hover; kartu
   dibuat bertingkat (nth-child margin) supaya tidak seragam template
6. GALERI KEGIATAN: grid foto 3 kolom rasio 4:3, tiap foto ada chip kategori
   mono + caption mono bernomor ("01 · ..."); klik foto →
   lightbox (overlay gelap, tutup dengan klik/Esc). Lalu strip terpisah
   "Reels & Video": kartu VERTIKAL rasio 9:16 dengan tombol play di tengah;
   klik → buka link video di tab baru (Instagram/YouTube/Drive)
7. KEAHLIAN: kartu bar skill animasi mengisi saat terlihat, tag tools,
   tag soft skills, kartu pendidikan
8. KONTAK: kartu email/WhatsApp/domisili (bisa diklik) + form pesan yang
   mengirim via mailto (membuka aplikasi email dengan subjek & isi terisi),
   banner CTA besar
9. FOOTER + tombol back-to-top muncul saat discroll

== DATA SAYU ==
- Nama: [NAMA LENGKAP]
- Peran (untuk teks berputar): [PERAN 1], [PERAN 2], ...
- Bio singkat: [2-3 KALIMAT]
- Pendidikan: [JENJANG JURUSAN — KAMPUS, TAHUN, IPK]
- Kontak: email [X], WhatsApp [X], domisili [X], Instagram [X], LinkedIn [X]
- Foto profil: [lampiran] — crop persegi fokus ke wajah
- Foto galeri: [lampiran + kategori masing-masing]
- Video/reels: [LINK 1], [LINK 2] (kategori: [X])

== LULUS KUALITAS ==
- Cek tampilan desktop DAN mobile (lebar 390px)
- Semua link & tombol berfungsi; tanpa error console
- Buatkan juga file CARA-EDIT.md: panduan mengganti nama, foto, galeri,
  warna tema, dan cara hosting gratis (Netlify Drop / GitHub Pages / Vercel)
```

(salin sampai sini)

---

## 🔁 PROMPT REVISI (kirim setelah web jadi, sesuai kebutuhan)

| Situasi | Prompt |
|---|---|
| Ganti identitas | `Ganti semua data: nama [X], email [X], WA [X] (format wa.me tanpa +), IG [X], LinkedIn [X], domisili [X]. Pasang foto profil dari lampiran (crop persegi fokus wajah, kompres <100KB).` |
| Galeri per kategori | `Kelompokkan galeri per kategori dengan chip warna yang sama dengan badge timeline: [kategori 1] ungu, [kategori 2] biru, [kategori 3] pink. Hapus kategori [X]. Caption: [X].` |
| Reels vertikal | `Tampilkan video sebagai kartu VERTIKAL 9:16 (format reels) di strip terpisah "Reels & Video" dengan tombol play; klik membuka link ini di tab baru: [LINK]. Thumbnail dari screenshot frame terbaik.` |
| Revisi pengalaman | `Revisi deskripsi pengalaman di [PERUSAHAAN]: saya mengerjakan [detail produk/proyek, tugas-tugas]. Sebutkan nama produknya.` |
| Ganti tema warna | `Ganti skema warna: aksen 1 [hex], aksen 2 [hex], aksen 3 [hex], latar [hex]. Semua lewat variabel CSS.` |
| Online | `Bantu saya pasang website ini online gratis (Netlify Drop / GitHub Pages) supaya dapat link publik.` |

---

## 💡 TIPS

- **PROMPT UTAMA** = cetak biru lengkap; **PROMPT REVISI** = pola percakapan
  lanjutan. Kombinasinya menghasilkan web seperti folder ini.
- Semakin spesifik bagian `DATA SAYA`, semakin sedikit revisi yang dibutuhkan.
- Untuk bukti karya, urutan daya persuasi: **link karya terbit > screenshot
  hasil/peringkat > foto kegiatan**. Surat keterangan tidak perlu di web.
- Simpan file ini bersama proyek; duplikat saja tiap mau buat portofolio baru.
