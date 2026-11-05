import pypdfium2 as pdfium

pdf = pdfium.PdfDocument("CV-Andra-Sakti-Pragata.pdf")
for i in range(len(pdf)):
    img = pdf[i].render(scale=2).to_pil()
    img.save(f"_cv-preview-{i+1}.png")
    print(f"halaman {i+1} tersimpan", img.size)
