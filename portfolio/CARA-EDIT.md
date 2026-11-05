# 📝 Cara Mengedit Website Portofolio

Semua konten ada di **satu file** saja: `index.html`. Buka dengan text editor apa pun
(Notepad, VS Code, dll.), ubah, simpan, lalu refresh browser.

Di dalam `index.html`, cari tanda komentar yang dimulai dengan `✏️` — itu penanda
semua tempat yang perlu kamu ganti dengan data aslimu.

## 1. Ganti nama
Nama sudah terisi: **Andra Sakti Pragata**. Kalau perlu mengubah, cari teks
"Andra Sakti Pragata" di `index.html` (judul halaman, hero, tentang, footer).

## 2. Ganti foto
Foto saat ini memakai file `foto-andra.jpg` di folder yang sama. Untuk mengganti,
timpa file itu dengan foto baru (pakai nama file yang sama), lalu refresh browser.
Kalau mau pakai nama file lain, ubah `src` pada tag `<img>` di bagian Tentang.

## 3. Ganti pengalaman
Bagian "Pengalaman" berisi 3 kartu (Creative Director, Wedding Organizer, Social Media
Specialist). Salin blok `<div class="t-item">...</div>` untuk menambah pengalaman baru,
atau ubah isinya. **Urutan: yang paling baru di atas.**

## 4. Ganti proyek
Setiap proyek adalah blok `<div class="project-card" data-cat="...">...</div>`.
- `data-cat` harus salah satu dari: `sosmed`, `seo`, `event` (samakan dengan tombol filter).
- Bisa ditambah/dikurangi sesukamu — tata letak menyesuaikan otomatis.

## 5. Ganti skill, kontak, dan peran di hero
- **Peran berputar di hero**: ubah daftar `ROLES` di bagian `<script>` paling bawah.
- **Email form kontak**: ubah `EMAIL_TUJUAN` di bagian `<script>` paling bawah.
- **Kontak (email/WA/domisili)**: cari komentar `✏️ GANTI info kontak`.
  Untuk WhatsApp, ganti angka di link `https://wa.me/6281234567890` (format internasional tanpa tanda +).

## 6. Ganti warna tema
Semua warna ada di blok `:root{ ... }` paling atas `<style>`:
```css
--accent-1: #8b5cf6;  /* ungu — aksen utama   */
--accent-2: #3b82f6;  /* biru — aksen kedua   */
--accent-3: #ec4899;  /* pink — aksen ketiga  */
--bg: #0a0a12;        /* warna latar          */
```
Ganti kode hex-nya, seluruh website ikut berubah.

## 7. Ganti foto & video galeri kegiatan
Section "Galeri Kegiatan" punya dua bagian:
- **Foto (galeri-1.jpg s.d. galeri-9.jpg)** — 1–2 Creative Director (chip ungu),
  3–7 Magang Nore (biru), 8–9 Crew Event (pink). Timpa filenya dengan foto baru
  (nama sama, crop mendatar 4:3).
- **Reels & Video (reels-1.jpg, reels-2.jpg)** — kartu vertikal 9:16 dengan **thumbnail
  frame asli dari video Instagram**. Ganti thumbnail: screenshot frame terbaik dari reels
  (potong bagian tombol/teks IG), lalu timpa filenya. Link video tercantum di atribut
  `data-href` pada tiap `<figure>` — klik kartu akan membukanya di tab baru.
  Kalau gambar baru tidak muncul (cache browser), tambahkan `?v=2` dst. pada `src`
  di `index.html`.
- Caption bisa diubah di `<figcaption class="gallery-cap">` dan chip kategori di
  `<span class="gallery-cat ...">`. Mau nambah slot? Salin satu blok `<figure>...</figure>`.

## 8. CV & preview saat link dibagikan
- **CV**: tombol "Download CV" memakai file `CV-Andra-Sakti-Pragata.pdf` — sekarang berisi
  **CV final buatanmu sendiri**. Untuk mengganti: timpa file itu dengan PDF baru (nama sama),
  lalu tambahkan `?v=3` dst. pada `href` di `index.html` bila browser masih memuat versi lama.
  (Generator lama `_buat_cv.py` masih ada kalau sewaktu-waktu dibutuhkan.)
- **Preview share (OG)**: `og-cover.jpg` dipakai WhatsApp/LinkedIn saat link dibagikan.
  Domain final sudah aktif (**hiandra.netlify.app**) dan OG tags di `index.html` sudah
  memakai URL absolut. Setiap kali mengubah `index.html`, **re-deploy**: buka
  app.netlify.com → situs kamu → tab **Deploys** → drag & drop folder `portfolio` lagi
  (URL tidak berubah). Tes preview: tempel link di chat WhatsApp (belum dikirim) atau
  di opengraph.xyz.

## 9. Melihat hasilnya
Cukup klik dua kali `index.html` — terbuka di browser tanpa perlu instal apa pun.

## 10. Memasang online (hosting gratis)
Upload **seluruh folder** (index.html + semua gambar + CV + og-cover):
- **Netlify Drop** (netlify.com/drop) — drag & drop folder, langsung dapat link.
- **GitHub Pages** — buat repository, upload file, aktifkan Pages.
- **Vercel** — impor dari GitHub.
