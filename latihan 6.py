print("========================================")
print("          RUMAH SAKIT SEHAT")
print("       SISTEM DATA PASIEN")
print("========================================")

nama = input("Masukkan nama pasien: ")

print("\nDAFTAR PENYAKIT PASIEN")
print("----------------------------------------")
print("1. Demam Berdarah (DBD)")
print("2. Tifus")
print("3. Pneumonia")
print("4. Diabetes Komplikasi")
print("5. Stroke")
print("6. Gagal Ginjal")
print("7. TBC Paru")
print("8. Infeksi Saluran Kemih Berat")
print("9. Anemia Berat")
print("10. Demam Rematik")
print("----------------------------------------")

pilihan = int(input("Pilih penyakit (1-10): "))
lama = int(input("Lama opname (hari): "))

if pilihan == 1:
    penyakit = "Demam Berdarah (DBD)"
    harga = 250000
    fasilitas = "Rawat inap, pemeriksaan darah, dan infus"
elif pilihan == 2:
    penyakit = "Tifus"
    harga = 200000
    fasilitas = "Rawat inap, pemeriksaan laboratorium, dan pemantauan dokter"
elif pilihan == 3:
    penyakit = "Pneumonia"
    harga = 350000
    fasilitas = "Rawat inap, oksigen sesuai kebutuhan, dan pemeriksaan paru"
elif pilihan == 4:
    penyakit = "Diabetes Komplikasi"
    harga = 400000
    fasilitas = "Rawat inap, pemeriksaan gula darah, dan konsultasi dokter"
elif pilihan == 5:
    penyakit = "Stroke"
    harga = 500000
    fasilitas = "Ruang perawatan khusus, pemantauan saraf, dan fisioterapi"
elif pilihan == 6:
    penyakit = "Gagal Ginjal"
    harga = 450000
    fasilitas = "Rawat inap, pemeriksaan fungsi ginjal, dan konsultasi dokter"
elif pilihan == 7:
    penyakit = "TBC Paru"
    harga = 300000
    fasilitas = "Rawat inap, pemeriksaan paru, dan pemantauan dokter"
elif pilihan == 8:
    penyakit = "Infeksi Saluran Kemih Berat"
    harga = 275000
    fasilitas = "Rawat inap, pemeriksaan urine, dan infus"
elif pilihan == 9:
    penyakit = "Anemia Berat"
    harga = 325000
    fasilitas = "Rawat inap, pemeriksaan darah, dan pemantauan hemoglobin"
elif pilihan == 10:
    penyakit = "Demam Rematik"
    harga = 350000
    fasilitas = "Rawat inap, pemeriksaan jantung, dan pemantauan dokter"
else:
    penyakit = ""
    harga = 0
    fasilitas = ""

if pilihan >= 1 and pilihan <= 10 and lama > 3:

    total = harga * lama

    print("\n========================================")
    print("             DATA PASIEN")
    print("========================================")
    print("Nama Pasien       :", nama)
    print("Jenis Penyakit    :", penyakit)
    print("Lama Opname       :", lama, "hari")
    print("Biaya Per Hari    : Rp", format(harga, ",").replace(",", "."))
    print("Total Biaya       : Rp", format(total, ",").replace(",", "."))

    print("\n========================================")
    print("         FASILITAS RUMAH SAKIT")
    print("========================================")
    print(fasilitas)

    print("\n========================================")
    print("             MENU MAKANAN")
    print("========================================")

    print("Pasien mendapatkan makanan khusus:")
    print("- Nasi atau bubur sesuai kondisi pasien")
    print("- Sayuran")
    print("- Lauk pauk sesuai diet")
    print("- Buah-buahan")
    print("- Susu sesuai kebutuhan pasien")

    print("\n========================================")
    print("           JADWAL KUNJUNGAN")
    print("========================================")

    if lama > 7:
        print("Kunjungan: Setiap hari")
        print("Waktu: 10.30 - 12.00 dan 16.00 - 18.00")
        print("Maksimal 2 pengunjung secara bergantian")
    else:
        print("Kunjungan: Setiap hari")
        print("Waktu: 16.00 - 18.00")
        print("Maksimal 2 pengunjung secara bergantian")

    print("\n========================================")
    print("           STATUS PASIEN")
    print("========================================")

    if lama > 7:
        print("Status: Opname jangka panjang")
    else:
        print("Status: Opname menengah")

    print("\n========================================")
    print("          METODE PEMBAYARAN")
    print("========================================")
    print("1. BPJS Kesehatan")
    print("2. Pembayaran Mandiri")

    bayar = int(input("Pilih pembayaran (1-2): "))

    print("\n========================================")
    print("          RINCIAN PEMBAYARAN")
    print("========================================")

    if bayar == 1:
        print("Metode Pembayaran : BPJS Kesehatan")
        print("Total Biaya       : Rp", format(total, ",").replace(",", "."))
        print("Ditanggung BPJS   : Sesuai ketentuan dan kepesertaan")
        print("Total Dibayar     : Sesuai ketentuan BPJS")

    elif bayar == 2:
        print("Metode Pembayaran : Mandiri")
        print("Total Biaya       : Rp", format(total, ",").replace(",", "."))
        print("Total Dibayar     : Rp", format(total, ",").replace(",", "."))
        print("Keterangan        : Pembayaran pribadi")

    else:
        print("Pilihan pembayaran tidak valid")

    print("\n========================================")
    print("       SEMOGA CEPAT SEMBUH!")
    print("          RUMAH SAKIT SEHAT")
    print("========================================")

else:
    print("\nData tidak valid!")
    print("Pilihan penyakit harus 1-10")
    print("Lama opname harus lebih dari 3 hari.")