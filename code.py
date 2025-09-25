import json
import pandas as pd

# Baca file JSON
with open("TI-A_ Avika Nanda J.A_V3925040.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ambil bagian "data_proyek_sipmani"
proyek = data["data_proyek_sipmani"]

# Buat ExcelWriter untuk menyimpan tiap kategori ke sheet berbeda
with pd.ExcelWriter("output_excel.xlsx", engine="openpyxl") as writer:
    for kategori, isi in proyek.items():
        # Konversi list of dict ke DataFrame
        df = pd.DataFrame(isi)
        # Simpan ke sheet dengan nama kategori
        df.to_excel(writer, sheet_name=kategori, index=False)

print("✅ Konversi JSON ke Excel berhasil! File tersimpan sebagai output_excel.xlsx")
