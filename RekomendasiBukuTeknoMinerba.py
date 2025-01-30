import webbrowser


kategori_buku = {
    "Pertambangan" : { 
        "rekomendasi" : ["Training Mine Design (Longterm) & Estimasi Cadangan"], 
        "gambar" : "https://teknominerba.com/wp-content/uploads/2023/06/Screen-Shot-2023-07-24-at-10.24.46-300x300.png"
    },
    "Mesin" : { 
        "rekomendasi" : ["Buku Permesinan Kapal"], 
        "gambar" : "https://teknominerba.com/wp-content/uploads/2023/12/WhatsApp-Image-2023-12-08-at-19.44.32-300x300.jpeg"
    },
    "Desain" : { 
        "rekomendasi" : ["Buku Dasar Autocad 2 Dimensi"], 
        "gambar" : "https://teknominerba.com/wp-content/uploads/2023/12/WhatsApp-Image-2023-12-08-at-19.44.32-1-300x300.jpeg"
    },
    "Teknologi Informatika" : { 
        "rekomendasi" : ["Buku Pengantar Teknologi Informatika dan Komunikasi Data"], 
        "gambar" : "https://teknominerba.com/wp-content/uploads/2023/12/WhatsApp-Image-2023-12-08-at-19.44.32-2-300x300.jpeg"
    },
    "Industri" : { 
        "rekomendasi" : ["Buku Analisis dan Perancangan Sistem Kerja"], 
        "gambar" : "https://teknominerba.com/wp-content/uploads/2023/12/WhatsApp-Image-2023-12-08-at-19.44.31-300x300.jpeg"
    },
    "Ekonomi" : { 
        "rekomendasi" : ["Buku Edisi Belajar Teori Ekonomi (Pendekatan Mikro) Berbasis Karakte"], 
        "gambar" : "https://teknominerba.com/wp-content/uploads/2023/11/WhatsApp-Image-2023-11-25-at-12.30.07-300x300.jpeg"
    },
}

ketik_kategori = input("Ketik salah satu kategori: Pertambangan, Mesin, Desain, Teknologi Informatika, Industri, Ekonomi")

if ketik_kategori in kategori_buku:
    print(f"Rekomendasi buku untuk kategori '{ketik_kategori}':")
    for rekomendasi in kategori_buku[ketik_kategori]["rekomendasi"]:
        print(f"-{rekomendasi}")
        print(f"\nGambar untuk kategori '{ketik_kategori}' : {kategori_buku[ketik_kategori]['gambar']}")
        webbrowser.open(kategori_buku[ketik_kategori]['gambar'])
else : print("Ketik kategori dari pilihan yang tersedia atau cek bila terdapat typo")
