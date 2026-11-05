from fpdf import FPDF

ACC = (122, 105, 246)   # violet
DARK = (24, 24, 30)
GRAY = (105, 105, 115)
BODY = (70, 70, 80)

pdf = FPDF(format="A4")
pdf.set_margins(16, 14, 16)
pdf.set_auto_page_break(True, margin=12)
pdf.add_page()
W = pdf.w - 32

# ===== KEPALA (gaya ATS: tengah, teks biasa) =====
pdf.set_font("helvetica", "B", 19)
pdf.set_text_color(*ACC)
pdf.cell(0, 9, "ANDRA SAKTI PRAGATA", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("helvetica", "", 9)
pdf.set_text_color(*GRAY)
pdf.cell(0, 5.2, "Semarang, Jawa Tengah  |  +62 895-7071-67716  |  andrasakti05@gmail.com",
         align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 5.2, "instagram.com/andraskti  |  linkedin.com/in/andra-sakti-4a56b1448",
         align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("helvetica", "B", 9)
pdf.set_text_color(*ACC)
pdf.cell(0, 5.2, "Terbuka untuk: Full-time  |  Internship  |  Freelance",
         align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(2.5)

def sec(t):
    if pdf.get_y() > 248:
        pdf.add_page()
    pdf.ln(1.2)
    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(*ACC)
    pdf.cell(0, 6, t.upper(), new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(30, 30, 36)
    pdf.set_line_width(0.6)
    pdf.line(16, pdf.get_y() + 0.6, 16 + W, pdf.get_y() + 0.6)
    pdf.ln(1.8)

def entry(judul, kanan=None, sub=None):
    if pdf.get_y() > 258:
        pdf.add_page()
    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(*DARK)
    if kanan:
        pdf.cell(W - 58, 5, judul)
        pdf.set_font("helvetica", "", 8.4)
        pdf.set_text_color(*GRAY)
        pdf.cell(58, 5, kanan, align="R", new_x="LMARGIN", new_y="NEXT")
    else:
        pdf.cell(0, 5, judul, new_x="LMARGIN", new_y="NEXT")
    if sub:
        pdf.set_font("helvetica", "I", 8.8)
        pdf.set_text_color(*ACC)
        pdf.cell(0, 4.4, sub, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(0.7)

def bullet(t):
    pdf.set_font("helvetica", "", 9.2)
    pdf.set_text_color(*BODY)
    pdf.set_x(20)
    pdf.multi_cell(W - 8, 4.4, "- " + t, new_x="LMARGIN", new_y="NEXT")

def paragraf(t):
    pdf.set_font("helvetica", "", 9.3)
    pdf.set_text_color(*BODY)
    pdf.multi_cell(W, 4.6, t, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)

# ===== PROFILE =====
sec("Profile")
paragraf(
    "Fresh graduate D3 Teknik Informatika, Politeknik Negeri Semarang (IPK 3.72/4.00) dengan "
    "ketertarikan tinggi pada bidang kreatif: multimedia, konten digital, dan strategi media sosial. "
    "Berpengalaman sebagai Creative Director (part-time), Social Media Specialist & SEO Content Writer "
    "(magang), serta crew wedding organizer freelance - mengelola konten produk Hotely.id hingga "
    "artikelnya menembus peringkat atas Google. Memahami tren terkini di internet untuk menyesuaikan "
    "konten yang sedang hot atau berpeluang viral. Terbiasa bekerja kolaboratif maupun mandiri, "
    "termasuk di bawah tekanan live event."
)
pdf.ln(0.5)

# ===== EDUCATION =====
sec("Education")
entry("Politeknik Negeri Semarang", "Agustus 2023 - 2026",
      sub="Teknik Informatika - Diploma III, IPK: 3.72/4.00")
bullet("Mempelajari Algoritma, Dasar Pemrograman, Jaringan, dan Aplikasi.")
bullet("Mata kuliah relevan: Desain Grafis, Desain UI/UX, Pemrograman Game, Sistem Multimedia, "
       "dan Embedded System.")
entry("SMK Negeri 3 Semarang", "Juli 2020 - Mei 2023",
      sub="Teknik Audio Video")
bullet("Mendalami bidang elektronika, termasuk Internet of Things (IoT), serta konsep multimedia: "
       "audio, video, dan produksi konten digital.")

# ===== WORK EXPERIENCE =====
sec("Work Experience")
entry("Creative Director - PT. Royal Kreasi Sinergi, Semarang", "Mar - Sep 2026",
      sub="Part Time")
bullet("Merancang strategi media sosial, content calendar, dan storyboard untuk promosi digital.")
bullet("Memproduksi konten visual & video pendek (Canva, CapCut) dilengkapi copywriting komunikatif.")
bullet("Membangun brand awareness & konsistensi visual branding melalui riset tren dan analisis audiens.")
entry("Social Media Specialist & SEO Content Writer - CV Nore Inovasi, Semarang", "Agu - Des 2025",
      sub="Internship")
bullet("Mengelola konten Hotely.id (PMS hotel, kolaborasi Nore Innovation x PT Hano Solusi Digital): "
       "konten plan, pengambilan & editing video, editing postingan feeds.")
bullet("Copywriting artikel berbasis SEO - beberapa artikel menembus peringkat atas Google "
       "('tipe kamar hotel', 'hotel termahal di indonesia').")
entry("Wedding & Event Organizer - Crew & Media Documentation - PT. Royal Kreasi Sinergi",
      "Sep 2024 - Sekarang",
      sub="Freelance")
bullet("Menjaga kelancaran alur acara: persiapan teknis, koordinasi antarvendor, pendampingan "
       "klien, dan pengawasan rundown agar tepat waktu.")
bullet("Membuat & mengelola konten promosi serta dokumentasi media sosial (foto & video), "
       "termasuk konsep teaser acara.")
entry("Teknisi (Magang) - Mandiri Jaya Teknik, Semarang", "Jul 2023 - Jan 2024")
bullet("Perbaikan alat elektronik: pengecekan & pengukuran komponen, pembacaan skema rangkaian, "
       "dan dokumentasi laporan harian.")

# ===== ORGANIZATIONAL & VOLUNTEERING =====
sec("Organizational & Volunteering Experience")
entry("Volunteer - Event Japota x JKT48", "Mei 2025")
bullet("Pengaturan logistik & pengawasan pengunjung; koordinasi tim pelaksana demi keamanan "
       "dan kenyamanan acara.")
entry("Volunteer - Samba KIP-K & Seminar Motivasi", "Desember 2024")
bullet("Registrasi peserta, pengaturan tempat duduk, dokumentasi, dan menjadi Liaison Officer "
       "pendamping peserta selama kegiatan.")
entry("IRRTU (Ikatan Remaja RT Satu)", "Maret 2020 - Sekarang")
bullet("Dokumentasi kegiatan (foto, video, pengarsipan) serta aktif dalam kegiatan sosial "
       "dan pengembangan remaja lingkungan sekitar.")

# ===== EXPERTISE =====
sec("Expertise")
entry("Hard Skills")
bullet("Microsoft Office (Word & PowerPoint).")
bullet("Perangkat lunak: Canva, CapCut, CorelDraw, Figma, Lightroom, VN, Google Workspace.")
bullet("Editing: desain grafis, video editing, fotografi, dan UI/UX design.")
bullet("Konten: perencanaan konten, copywriting, dan SEO (riset keyword & on-page).")
bullet("Bahasa pemrograman: Python, HTML, CSS, dan PHP.")
entry("Soft Skills")
bullet("Komunikasi, kreativitas, adaptasi, dan etos kerja tinggi.")
bullet("Kerja tim maupun mandiri; perencanaan dan pengorganisasian.")
bullet("Bekerja di bawah tekanan, manajemen waktu, dan sensitif trend.")
entry("Kemampuan Bahasa")
bullet("Bahasa Indonesia (native) dan Bahasa Inggris (basic).")

# ===== CERTIFICATES =====
sec("Certificates")
bullet("Database Design - Oracle.")
bullet("Database Programming with SQL - Oracle.")

# ===== PROJECTS =====
sec("Projects")
bullet("UNIVGO - Sistem Informasi Direktori Review Kampus (Project Based Learning): "
       "Front-End Developer & Video Editor.")
bullet("Arena Ria - Game 2D berisi 3 mini games bertema berbeda (Unity): Game Developer.")

# ===== ACHIEVEMENTS =====
sec("Achievements")
bullet("Juara 2 Lomba Project H3RO (kategori editing dan cuplikan momen terbaik dari video game).")
bullet("Juara 2 Lomba Cinematic tingkat SMK.")
bullet("30.000 & 15.000 followers di dua akun TikTok berbeda dengan konten dan editing sendiri.")

pdf.output("CV-Andra-Sakti-Pragata.pdf")
import os
print("CV dibuat:", os.path.getsize("CV-Andra-Sakti-Pragata.pdf") // 1024, "KB, halaman:", pdf.pages_count)
