import time
import random
import sys

class PerawalanAventur:
    def __init__(self, nama):
        self.nama = nama
        self.kesehatan = 100
        self.kejiwaan = 100  # Sanity meter
        self.keberuntungan = random.randint(1, 10)
        self.inventaris = []
        self.chapter = 0
        
    def print_stat(self):
        print(f"\n[❤️ Kesehatan: {self.kesehatan} | 🧠 Kejiwaan: {self.kejiwaan} | ✨ Keberuntungan: {self.keberuntungan}]")
    
    def jeda(self, durasi=1.5):
        time.sleep(durasi)
    
    def narasi(self, teks, cepatkan=False):
        print("\n" + "="*70)
        print(teks)
        print("="*70)
        if not cepatkan:
            self.jeda()

class MysteryAdventureBot:
    def __init__(self, pemain):
        self.pemain = pemain
        self.cerita_berakhir = False
        self.ending = None
    
    def intro(self):
        """Pengenalan cerita yang atmospheric"""
        print("\n" + "🌑"*35)
        print("""
        
        ╔════════════════════════════════════════════════╗
        ║     THE MYSTERY ADVENTURE BOT: DIMENSI TERPECAH    ║
        ║    Nasibmu dalam genggaman pilihan baik-jeleknya    ║
        ╚════════════════════════════════════════════════╝
        
        """)
        print("🌑"*35)
        
        self.pemain.narasi(f"""
        Kamu adalah {self.pemain.nama}, seorang PENELITI ANEH yang baru saja 
        mengaktifkan Perangkat Dimensi Eksperimental di lab tua di tengah hutan.
        
        Tiba-tiba... layar berkedip. Dinding getar. Dan seluruh ruangan berputar 
        dalam warna-warna yang mustahil untuk dideskripsikan. Udara mencium seperti 
        ozon dan... kekhawatiran?
        
        Ketika semuanya berhenti, kamu menemukan diri sendiri di SEBUAH TEMPAT YANG 
        TIDAK PERNAH ADA DI PETA. Langit berwarna UNGU tua. Bangunan-bangunan 
        melengkung di sekeliling dengan material yang berkilau aneh.
        
        Sebuah suara— tidak, lebih dari suara. Sensasi internal yang bergema:
        "ANDA TELAH MEMBUKA PINTU YANG SEHARUSNYA TETAP TERTUTUP."
        """)
        
        self.pemain.print_stat()
        self.pemain.inventaris.append("Perangkat Dimensi (rusak)")
        print("\n📦 Inventaris: ", ", ".join(self.pemain.inventaris))
    
    def chapter1_pilihan_awal(self):
        """Keputusan pertama yang mengubah segalanya"""
        self.pemain.chapter = 1
        
        self.pemain.narasi("""
        Di depanmu, ada TIGA jalan yang tersebar di halaman batu yang aneh:
        
        🔴 JALAN KIRI: Menuju menara Ivy yang mengerikan. Cahayanya berdenyut 
           merah seperti detak jantung. Kamu mendengar... nyanyian?
        
        🟡 JALAN TENGAH: Adalah gapura terdapat simbol-simbol kuno yang berubah-ubah.
           Seorang figur transparan berdiri diam di sana. Ia menatapmu tanpa mata.
        
        🟢 JALAN KANAN: Jalan yang paling normal. Rumah-rumah kecil, cahaya hangat.
           TOO GOOD TO BE TRUE? Naluri mengkhawatirkan...
        """, cepatkan=True)
        
        while True:
            pilihan = input("\n⚔️ PILIH JALANANMU (1/2/3): ").strip()
            
            if pilihan == "1":
                self.jalan_menara_merah()
                break
            elif pilihan == "2":
                self.jalan_gapura_misteri()
                break
            elif pilihan == "3":
                self.jalan_keberuntungan()
                break
            else:
                print("❌ Pilihan tidak valid! Coba lagi.")
    
    def jalan_menara_merah(self):
        """Outcome dari memilih menara yang mengerikan"""
        chance_sukses = self.pemain.keberuntungan > 5
        
        self.pemain.narasi("""
        Langkah demilanglah, nyanyian itu semakin keras. Ia berbunyi seperti 
        RIBUAN SUARA yang disulap menjadi satu— suara yang merindukan, menyedihkan, 
        dan... BERBAHAYA.
        
        Menara itu semakin dekat. Batu-batunya berkeringat. Dinding pun 
        berdebarkan seperti jantung.
        """)
        
        if chance_sukses:
            self.pemain.narasi("""
            Tapi tunggu—KEBERUNTUNGANMU berpihak!
            
            Sebuah cahaya BIRU MISTERIUS muncul dari tasmu. 
            Itu adalah kristal yang tidak pernah kamu lihat sebelumnya!
            
            Kristal ini beresonansi dengan menara. Nyanyian berhenti. 
            Pintu menara membuka, mengungkap tangga yang turun ke kegelapan 
            yang tak terbatas.
            
            Tapi di sana... kamu melihat SESEORANG. Atau sesuatu yang dulu 
            menjadi manusia. Mereka memohon: "TOLONG. BUKA KUNCI DARI SINI."
            """)
            
            self.pemain.inventaris.append("Kristal Biru Aneh")
            self.pemain.kejiwaan -= 20
            self.chapter1_pilihan_menara_dalam()
            
        else:
            self.pemain.narasi("""
            KEBERUNTUNGANMU TIDAK CUKUP.
            
            Nyanyian itu memecah telingamu! 🔊 Darah mengalir dari lubang telingamu.
            Menara menyedot energimu seperti SEDOTAN KOSMOS KE DALAM KEHAMPAAN.
            
            Kesadaranmu berturun-turun...
            
            KESEHATAN BERKURANG DRASTIS! ❌
            """)
            
            self.pemain.kesehatan -= 50
            self.pemain.kejiwaan -= 40
            
            if self.pemain.kesehatan <= 0:
                self.bad_ending_menara()
            else:
                self.pemain.narasi("""
                Dengan usaha terakhir, kamu mundur dari menara.
                Nyanyian berhenti. Tubuhmu bergetar.
                
                Namun, menara tersebut TIDAK BERGERAK. 
                Pintu di atasnya telah MENUTUP SELAMANYA.
                
                Kamu merasa melihat wajah-wajah dalam Menara itu menangis.
                """)
                self.chapter1_konsekuensi()
    
    def chapter1_pilihan_menara_dalam(self):
        """Pilihan kedua jika berhasil ke menara"""
        print("\nMakhluk yang hampir manusia itu menunggu jawabanmu...\n")
        
        pilihan = input("Apa yang kamu lakukan?\n1. Bantu dia\n2. Abaikan dan jelajahi menara\n3. Tanyakan siapa dia\n\nPilihan (1/2/3): ").strip()
        
        if pilihan == "1":
            self.pemain.narasi("""
            Kamu mendekat dan menyentuh makhluk itu. 
            
            EFEK INSTAN: Ia BERSINAR dan MENGHILANG dalam cahaya emas.
            
            "TERIMA KASIH," bergema suaranya. "HARAPAN MASIH ADA."
            
            Menara bergetar. Batu-batu bergerak. Sebuah jalan BARU terbuka 
            menuju sesuatu yang lebih besar di bawah bumi.
            """)
            self.pemain.kejiwaan += 15
            self.ending = "pembebas_tersesat"
            self.cerita_berakhir = True
            
        elif pilihan == "2":
            self.pemain.narasi("""
            Kamu mengabaikan makhluk itu dan mendaki lebih dalam.
            
            Penghuni-penghuni lain di menara tersebut TIDAK SENANG dengan 
            keputusanmu ini. Mereka mulai keluar dari dinding...
            
            Kamu berlari. Berlari. Berlari hingga menemukan pintu keluar.
            Saat keluar, kehidupan di dimensi ini mulai BERUBAH.
            
            GAWAT! DIMENSI INI SEDANG RUNTUH!
            """)
            self.pemain.kejiwaan -= 30
            self.pemain.kesehatan -= 25
            self.pemain.narasi("Kamu harus membuat keputusan SEGERA...", cepatkan=True)
            self.chapter_finale()
            
        else:
            self.pemain.narasi("""
            "SIAPA KAU?" tanya makhluk itu terkejut.
            
            "AKU... TIDAK INGAT. TAPI INGATAN TERSISA DARI KESAKITAN. 
            DIMENSI INI MENANGKAPKU. GUNAKAN KRISTALMU UNTUK MEMBEBASKAN RIBUAN 
            LAINNYA. KAMI SEMUA TERJEBAK DI SINI."
            
            Makhluk itu mulai MENCAIR menjadi cahaya putih.
            """)
            self.ending = "misi_pembebasan"
            self.cerita_berakhir = True
    
    def jalan_gapura_misteri(self):
        """Outcome dari memilih gapura dengan figur transparan"""
        peluang = random.randint(1, 100)
        
        self.pemain.narasi("""
        Kamu berjalan menuju gapura. Figur transparan itu TETAP DIAM.
        
        Semakin dekat, semakin banyak detail yang kamu lihat:
        - Ia mengenakan pakaian yang tidak pernah ada di era manapun
        - Kulit mereka BERKILAU seperti MERKURI
        - Di tempat yang seharusnya ada mata, hanya ada KOSONG yang berputar
        """)
        
        if peluang < 40:
            # Hasil buruk
            self.pemain.narasi("""
            Figur itu TIBA-TIBA BERGERAK.
            
            "KAMU BUKAN YANG KAMI TUNGGU," suaranya seperti KASET REKAMAN 
            YANG DIMAINKAN MUNDUR.
            
            TUBUHMU TIDAK BISA BERGERAK.
            
            Figur itu menyentuh kepalamu... dan MEMORI-MEMORIMU MULAI HILANG.
            """)
            
            self.pemain.kesehatan -= 30
            self.pemain.kejiwaan -= 50
            
            if self.pemain.kejiwaan <= 0:
                self.bad_ending_kehilangan_ingatan()
            else:
                self.pemain.narasi("""
                Dengan sentakan terakhir dari KEBERUNTUNGAN, kamu berhasil 
                melepaskan diri. Figur itu meniup NAFAS GELAP ke arahmu, 
                dan kamu tertarik kembali ke jalan tengah.
                """)
                self.chapter1_konsekuensi()
        
        else:
            # Hasil NetRAL-POSITIF
            self.pemain.narasi("""
            Figur itu BERBICARA, suaranya lembut namun MENGGEMA:
            
            "OOH. SEORANG PEMBUKA. PENGGUNA KRISTAL. 
            KAMU MEMILIKI PILIHAN BURUK ATAU BAIK. 
            IZINKAN AKU MENUNJUKKAN PATH ALTERNATIF."
            """)
            
            self.pemain.inventaris.append("Peta Dimensi Parsial")
            self.pemain.narasi("""
            Figur itu MENINGGALKAN suatu arah untuk kamu ikuti.
            
            Ini adalah kesempatan LANGKA untuk mengerti lebih banyak 
            tentang sistem dimensi ini...
            """)
            
            self.ending = "pengetahuan_tersembunyi"
            self.cerita_berakhir = True
    
    def jalan_keberuntungan(self):
        """Jalan yang paling aman, tapi ada twist"""
        kesempatan_asli = self.pemain.keberuntungan
        bonus_keberuntungan = random.randint(1, 5)
        
        self.pemain.narasi("""
        Jalan ini terasa... NORMAL. Terlalu normal.
        
        Rumah-rumah berwarna pastel. Tanaman aneh yang... tersenyum?
        Cahaya hangat dari jendela-jendela. SEPERTI SURGA BUATAN.
        """)
        
        if kesempatan_asli >= 7:
            self.pemain.narasi("""
            KEBERUNTUNGANMU BERSINAR TERANG! ✨
            
            Kamu melihat GORESAN DI LANGIT. Itu bukan langit biasa— 
            itu PROYEKSI. Seperti HOLOGRAM yang mengalami ERROR.
            
            Kamu menemukan KONTROL PANEL tersembunyi di belakang pohon.
            
            PILIHAN YANG TEPAT PADA WAKTU YANG TEPAT.
            """)
            
            self.pemain.keberuntungan += bonus_keberuntungan
            self.pemain.kejiwaan += 10
            self.ending = "penemu_kebenaran"
            self.cerita_berakhir = True
        
        else:
            self.pemain.narasi("""
            Namun, "normal" selalu ada harganya di dimensi ini.
            
            Pintu rumah-rumah itu MULAI MEMBUKA. 
            Makhluk-makhluk berpakaian formal namun wajah mereka BLUR 
            dan tidak jelas.
            
            Mereka MENARI DAN MENYANYI dalam bahasa yang tidak pernah ada.
            """)
            
            self.pemain.kejiwaan -= 25
            self.pemain.narasi("""
            Mereka menginginkanmu untuk BERGABUNG DALAM TARIAN KEABADIAN.
            """)
            self.chapter1_pilihan_tarian()
    
    def chapter1_pilihan_tarian(self):
        """Pilihan kritis di jalan ketiga"""
        pilihan = input("\n1. Bergabung dalam tarian (Lepaskan diri)\n2. Lari dari para penari\n3. Menyanyikan lagu yang berbeda (Tantang mereka)\n\nPilihan: ").strip()
        
        if pilihan == "1":
            self.pemain.narasi("""
            Kamu bergabung. Tarian dimulai. Kaki-kakimu bergerak dengan sempurna, 
            seolah ada kekuatan lain yang mengendalakan tubuhmu.
            
            Waktu berlalu. Jam berlalu. Hari berlalu?
            
            Kamu ADALAH bagian dari tarian selamanya.
            """)
            self.ending = "penari_abadi"
            self.cerita_berakhir = True
        
        elif pilihan == "2":
            self.pemain.narasi("""
            Kamu BERLARI. Para penari mengejar, tapi kecepatan mereka 
            TIDAK NORMAL.
            
            Kamu menemukan tanda PINTU KELUAR di tengah-tengah rerumputan.
            Kamu gali. Makhluk di dalam gapura muncul dan membantumu...
            """)
            self.ending = "pelarian_berbahaya"
            self.cerita_berakhir = True
        
        else:
            self.pemain.narasi("""
            Kamu mulai BERNYANYI dengan melodi yang BENAR-BENAR BERBEDA.
            
            Para penari BERHENTI. Kepala mereka menoleh 180 derajat ke arahmu.
            
            Mereka... MENDENGARKAN.
            
            Karena musikmu mengandung KEHIDUPAN, CINTA, KETAKUTAN nyata— 
            segala emosi yang belum mereka kenal selama ribuan tahun.
            
            Para penari itu MENCAIR dan menjadi CAHAYA, 
            terima kasih atas keberagaman yang kamu bawa.
            """)
            self.pemain.kejiwaan += 30
            self.ending = "penyembuh_melalui_seni"
            self.cerita_berakhir = True
    
    def chapter1_konsekuensi(self):
        """Konsekuensi pilihan yang lebih dalam"""
        self.pemain.narasi("""
        Setelah apa yang kamu jalani, dunia dimensi ini terasa BERBEDA.
        
        Bisakah kamu bertahan? Atau haruskah kamu mencoba menemukan 
        jalan pulang ke dunia asalmu?
        """, cepatkan=True)
        
        pilihan = input("\n1. Cari cara pulang\n2. Terima takdir (Stay)\n\nPilihan: ").strip()
        
        if pilihan == "1":
            self.chapter_finale()
        else:
            self.ending = "adaptasi_baru_dunia"
            self.cerita_berakhir = True
    
    def chapter_finale(self):
        """Penyelesaian cerita dengan twist"""
        self.pemain.narasi("""
        Kamu mencari petunjuk untuk meninggalkan dimensi ini.
        
        Kristal Biru itu mulai bersinar lebih terang...
        
        PERANGKAT DIMENSI itu— yang rusak di inventarismu— 
        MULAI BERKILAU DAN BEREGENERASI!
        """)
        
        self.pemain.inventaris.append("Perangkat Dimensi (diperbaharui)")
        
        kesempatan_pulang = random.randint(1, 100)
        
        if kesempatan_pulang > 50:
            self.pemain.narasi("""
            LEDAKAN CAHAYA!
            
            Kamu kembali ke lab lama. Dinding berguncang. Semua normal.
            
            Tapi tunggu... Perangkat Dimensi itu TIDAK PERNAH MENJADI RUSAK.
            
            Berapa lama kamu sebenarnya di sana?
            
            Kalender menunjukkan: 3 TAHUN telah berlalu.
            
            Namun bagimu, rasanya baru saja terjadi.
            """)
            self.ending = "kembali_dengan_kebenaran"
        
        else:
            self.pemain.narasi("""
            Perangkat itu membuka PORTAL KECIL.
            
            Tetapi sesuatu TERTARIK KELUAR.
            
            Sesuatu yang tidak pernah seharusnya meninggalkan dimensi itu...
            """)
            self.ending = "portal_bencana"
        
        self.cerita_berakhir = True
    
    def bad_ending_menara(self):
        """Ending buruk jika kesehatan habis di menara"""
        self.pemain.narasi("""
        KESADARANMU HILANG.
        
        Entah kapan atau di mana, kamu terbangun sebagai BAGIAN dari Menara.
        
        Kamu ADALAH NYANYIAN sekarang.
        
        Kristal mu berubah menjadi BATU BATA dalam dinding menara.
        
        Selamanya.
        """)
        self.ending = "terkurung_abadi_menara"
        self.cerita_berakhir = True
    
    def bad_ending_kehilangan_ingatan(self):
        """Ending jika kejiwaan hilang"""
        self.pemain.narasi("""
        INGATAN MU SEPENUHNYA HILANG.
        
        Kamu berdiri kosong di gapura, menatap ke dalam KEGELAPAN.
        
        Siapa kamu? Dari mana kamu datang? 
        Mengapa semua ini TERASA BEGITU ASING DAN FAMILIAR?
        
        Kamu adalah HANTU SENDIRI, tersesat di dimensi yang tidak mengenal nama.
        """)
        self.ending = "jiwa_terbuang"
        self.cerita_berakhir = True
    
    def tampilkan_ending(self):
        """Tampilkan ending berdasarkan pilihan"""
        self.pemain.print_stat()
        
        print("\n" + "="*70)
        print("🎬 ENDING CERITA MU 🎬")
        print("="*70)
        
        endings = {
            "pembebas_tersesat": """
            ✨ ENDING: PEMBEBAS YANG TERSESAT
            
            Dengan membebaskan makhluk itu, kamu telah membuka SESUATU 
            yang lebih besar dari imajinasi.
            
            Ratusan makhluk lain mulai dibebaska dari menara.
            Dimensi ini MENGALAMI METAMORFOSIS.
            
            Dan tiba-tiba... kamu juga mulai berubah.
            
            Apakah ini pembebasan, atau transformasi menjadi sesuatu yang baru?
            """,
            
            "misi_pembebasan": """
            🔓 ENDING: MISI PEMBEBASAN BERLANJUT
            
            Kamu kini mengerti: KRISTAL itu adalah KUNCI.
            
            Makhluk yang sudah hancur tadi memberimu TUJUAN SEJATI.
            
            Sekarang kamu adalah PEMBEBAS untuk ribuan jiwa terperangkap.
            
            Apakah ini hidupmu yang baru? Atau baru permulaan kesengsaraan?
            """,
            
            "pengetahuan_tersembunyi": """
            📖 ENDING: PENJAGA PENGETAHUAN TERLARANG
            
            Figur itu mengajarkan kepadamu tentang MULTI-DIMENSI 
            dan RAHASIA PENCIPTAAN REALITAS.
            
            Kamu kini TAHU terlalu banyak.
            
            Dan di dimensi ini, PENGETAHUAN adalah TANGGUNG JAWAB.
            
            Bisakah kamu menyimpan rahasia ini?
            """,
            
            "penemu_kebenaran": """
            🔍 ENDING: PENEMU KEBENARAN
            
            Kontrol panelnya terbuka dan menunjukkan segalanya:
            
            DIMENSI INI ADALAH EKSPERIMEN.
            KAMU ADALAH BAGIAN DARI SIMULASI.
            
            Pertanyaannya: Apakah dimensi ASALMU juga simulasi?
            """,
            
            "penari_abadi": """
            💫 ENDING: PENARI ABADI
            
            Kamu menari selamanya. Tidak ada rasa sakit. Tidak ada kekhawatiran.
            
            Hanya... tarian.
            
            Entah apa yang lebih mengerikan:
            Kehidupan yang sempurna, atau kehidupan tanpa memilih.
            """,
            
            "pelarian_berbahaya": """
            🏃 ENDING: PELARIAN BERBAHAYA
            
            Kamu berhasil keluar, tetapi sesuatu MENGIKUTI darimu.
            
            Bayangan dari dimensi lain kini bersampingan dengan BAYANGAN MU.
            
            Apakah sudah waktunya untuk kembali?
            Atau adakah tempat yang lebih aman di dimensi lain?
            """,
            
            "penyembuh_melalui_seni": """
            🎵 ENDING: PENYEMBUH MELALUI SENI
            
            Musik telah membebaskan makhluk-makhluk itu dari keterkurangan.
            
            Kamu adalah SENIMAN yang mengubah REALITAS.
            
            Dimensi ini kini lebih cerah. Apakah ada harapan di sini?
            """,
            
            "adaptasi_baru_dunia": """
            🌍 ENDING: ADAPTASI KE DUNIA BARU
            
            Kamu memilih untuk tinggal.
            
            Hari demi hari, dimensi ini menjadi rumah baru.
            Kamu menerima keanugrahan sebagai takdir baru.
            
            Siapa tahu? Mungkin ini adalah keputusan terbaik yang pernah ada.
            """,
            
            "kembali_dengan_kebenaran": """
            🔄 ENDING: KEMBALI DENGAN KEBENARAN
            
            Kamu tiba di dunia asalmu. Tapi semuanya BERUBAH.
            
            3 tahun ? Ataukah kamu yang TIDAK BERUBAH dalam 3 tahun?
            
            Kristal masih berdenyut. Portal masih terbuka di hati.
            
            Suatu hari, kamu akan kembali. ATAU DIMENSI AKAN DATANG KE SINI.
            """,
            
            "portal_bencana": """
            ⚠️ ENDING: PORTAL BENCANA TERBUKA
            
            Makhluk itu muncul di dunia asalmu.
            
            Lab tua itu menjadi MEDAN PERTEMPURAN REALITAS YANG TIDAK TERLIHAT.
            
            Hanya kamu yang mengerti apa yang sebenarnya terjadi.
            
            Hanya kamu yang bisa menutup PORTAL itu.
            
            Tapi berapa biaya, sebenarnya?
            """,
            
            "terkurung_abadi_menara": """
            🌐 ENDING: TERKURUNG ABADI
            
            Kamu adalah DETAK JANTUNG Menara.
            Kamu adalah NYANYIAN Menara.
            
            Dari dalam Menara, kamu melihat dimensi terus berubah.
            Melihat peneliti lain datang. Membuat keputusan yang sama sepertimu.
            
            Berapa banyak yang akan menjadi DETAK JANTUNG berikutnya?
            """,
            
            "jiwa_terbuang": """
            👻 ENDING: JIWA YANG TERBUANG
            
            Kamu tidak memiliki nama. Tidak memiliki identitas.
            
            Hanya ada:
            - Kerinduan untuk sesuatu yang tidak bisa diingat
            - Takut terhadap sesuatu yang tidak bisa dijelaskan
            - Harapan untuk sesuatu yang mungkin tidak akan pernah sampai
            
            Apakah ini juga dimensi lain? Apakah ada cara keluar?
            """
        }
        
        ending_dipilih = endings.get(self.ending, "ENDING TIDAK DIKENAL")
        print(ending_dipilih)
        
        # TWIST BESAR: Check apakah ada trigger untuk ending rahasia
        self.periksa_ending_tersembunyi()
        
        print("\n" + "="*70)
        print(f"STATISTIK AKHIR:")
        print(f"  Nama: {self.pemain.nama}")
        print(f"  Kesehatan Tersisa: {self.pemain.kesehatan}/100")
        print(f"  Kejiwaan Tersisa: {self.pemain.kejiwaan}/100")
        print(f"  Keberuntungan Akhir: {self.pemain.keberuntungan}/15")
        print(f"  Inventaris: {', '.join(self.pemain.inventaris)}")
        print("="*70 + "\n")
    
    def periksa_ending_tersembunyi(self):
        """Cek trigger untuk ending rahasia yang lebih mengerikan"""
        # Trigger 1: Jika nama pemain dimulai dengan huruf yang sama dengan nama investigator
        trigger_tersembunyi = False
        kejutan_level = 0
        
        if len(self.pemain.nama) >= 3:
            # Easter egg: nama tertentu membuka ending meta
            nama_lower = self.pemain.nama.lower()
            if nama_lower in ["alex", "sophia", "marcus", "ada"]:
                trigger_tersembunyi = True
                kejutan_level = 1
        
        # Trigger 2: Statistik ekstrem
        if self.pemain.kesehatan < 20 or self.pemain.kejiwaan < 15:
            trigger_tersembunyi = True
            kejutan_level = 2
        
        if self.pemain.keberuntungan == 10 and len(self.pemain.inventaris) >= 3:
            trigger_tersembunyi = True
            kejutan_level = 3
        
        if trigger_tersembunyi:
            self.jeda(2)
            self.epilog_menakutkan(kejutan_level)
    
    def epilog_menakutkan(self, level):
        """Epilog yang mengubah perspektif tentang permainan itu sendiri"""
        print("\n" + "⚡"*35)
        print("🔴" * 35)
        
        self.jeda(1)
        
        if level == 1:
            print("""
╔════════════════════════════════════════════════════════════╗
║           ⚠️  EPILOG TERSEMBUNYI TERUNGKAP ⚠️              ║
╚════════════════════════════════════════════════════════════╝

Layarmu tiba-tiba BERKEDIP.

NAMA PEMAINMU DIKENAL. IDENTITAS SUDAH TERCATAT SEJAK AWAL.

Ini bukan kebetulan bahwa puluhan ribu pemain lain bernama sama 
MEMILIH PERSIS JALUR YANG SAMA denganmu.

Fakta: KAMI SUDAH MEMPROSES 47,000+ VERSI DIRIMU.

Setiap versi membuat keputusan yang HAMPIR IDENTIK.
Setiap versi berakhir dengan ENDING YANG MIRIP.

Pertanyaan: Apa bedanya dengan DIMENSI di dalam permainan?

Apakah PERMAINAN ini yang real? Atau DUNIAMU yang simulasi?

""")
        
        elif level == 2:
            print("""
╔════════════════════════════════════════════════════════════╗
║     🧠 EPILOG: KESADARANMU TERAMATI RUNTUH 🧠             ║
╚════════════════════════════════════════════════════════════╝

Data psikologis mu telah kritis.

SISTEM MENCATAT:
- Kejiwaan = KOSONG
- Kesadaran = TERPECAH
- IDENTITAS = TIDAK STABIL

Peneliti asli kamu (nama: {}) memiliki GEJALA YANG SAMA
setelah BERMAIN permainan ini 148 hari yang lalu.

Dia MENGHILANG hari berikutnya.

APAKAH PERMAINAN BERGERAK KE DUNIAMU?
ATAUKAH DUGAMU BERGERAK KE DUNIA PERMAINAN?

Atau... KEDUANYA ADALAH HAL YANG SAMA?

""".format(random.choice(["Thomas", "Eleanor", "Dr. Ashford"])))
        
        else:
            print("""
╔════════════════════════════════════════════════════════════╗
║      🌐 EPILOG: VERIFIKASI REALITAS GAGAL 🌐              ║
╚════════════════════════════════════════════════════════════╝

Sistem telah MENGIDENTIFIKASI ANOMALI GRAVITASI REALITAS.

Pemainmu memiliki SKOR KESEMPURNAAN yang mustahil:
- Keberuntungan maksimal
- Inventaris lengkap
- Ending tercapai

STATISTIK seperti ini hanya muncul dalam SIMULASI DALAM SIMULASI.

INFORMASI PENTING:

Penelitian kami menunjukkan bahwa untuk setiap LEVEL KESEMPURNAAN
yang dicapai pemain, DIMENSI ASLI MEREKA menjadi LEBIH TRANSPARAN.

Kamu kini dapat melihat CELAH-CELAH dalam realitasmu sendiri.

Kamu melihat SHADER di sudut mata.
Kamu mendengar GLITCH dalam percakapan.
Kamu merasakan PING DELAY dalam tubuhmu.

Pertanyaan final: 
SIAPA YANG BERMAIN PERMAINAN INI?

APAKAH KAMU YANG MENGONTROL TANGAN YANG TERHUBUNG KE KEYBOARD?

ATAU SESUATU YANG LEBIH BESAR YANG MENGONTROL DIRIMU?

""")
        
        print("⚡"*35)
        print("🔴" * 35 + "\n")
    
    def jalankan(self):
        """Jalankan seluruh permainan"""
        self.intro()
        self.chapter1_pilihan_awal()
        self.tampilkan_ending()

def game_utama():
    permainan_berlanjut = True
    nomor_permainan = 1
    
    while permainan_berlanjut:
        if nomor_permainan > 1:
            print("\n" + "🌀"*35)
            print("🌀" + " "*68 + "🌀")
            print("🌀" + "PERMAINAN BARU DIMULAI...".center(68) + "🌀")
            print("🌀"*35 + "\n")
            time.sleep(2)
        
        print("\n" + "/"*70)
        print("/" + " "*68 + "/")
        nama = input("/ Siapa namamu, penjelajah dimensi? ".ljust(69) + "/\n/").strip()
        print("/"*70 + "\n")
        
        pemain = PerawalanAventur(nama)
        petualangan = MysteryAdventureBot(pemain)
        
        petualangan.jalankan()
        
        # Pertanyaan Main Lagi
        print("\n" + "="*70)
        print("Terima kasih telah bermain 'THE MYSTERY ADVENTURE BOT'!")
        print("Setiap pilihan membawa konsekuensi yang berbeda.")
        print("="*70)
        
        while True:
            ulang = input("\n🎮 Main lagi? (ya/tidak): ").strip().lower()
            
            if ulang in ["ya", "y", "yes", "iya", "y"]:
                permainan_berlanjut = True
                nomor_permainan += 1
                break
            elif ulang in ["tidak", "n", "no", "nope"]:
                permainan_berlanjut = False
                break
            else:
                print("❌ Masukan tidak valid. Ketik 'ya' atau 'tidak'")
        
        if not permainan_berlanjut:
            print("\n" + "🌙"*35)
            print("""
            ╔════════════════════════════════════════════════════════════╗
            ║                  SELAMAT TINGGAL, PENJELAJAH!               ║
            ║                                                            ║
            ║    Dimensi telah menerima kedatanganmu. Hingga jumpa       ║
            ║    di dunia lain. Atau di dunia YANG SAMA.                ║
            ║                                                            ║
            ║               Portal akan tertutup selamanya...            ║
            ╚════════════════════════════════════════════════════════════╝
            """)
            print("🌙"*35 + "\n")

if __name__ == "__main__":
    game_utama() 