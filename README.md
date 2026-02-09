# 🌑 THE MYSTERY ADVENTURE BOT: DIMENSI TERPECAH

**Game Cerita Interaktif berbasis teks** dengan pilihan yang menentukan nasib pemain di dimensi yang penuh misteri dan bahaya.

## 📖 Konsep Cerita

Kamu adalah seorang **Peneliti** yang baru saja mengaktifkan Perangkat Dimensi Eksperimental. Tiba-tiba, segala sesuatu TERBANG ke dimensi yang tidak pernah ada di peta. Langit berwarna ungu tua, bangunan-bangunan melengkung dengan material aneh, dan suara-suara yang tidak bisa dijelaskan.

**Pilihan pertamamu akan menentukan semuanya:**
- 🔴 **Jalan Menara Merah** - Nyanyian yang mengerikan dari kedalaman, makhluk yang hampir manusia
- 🟡 **Jalan Gapura Misteri** - Figur transparan tanpa mata yang berbicara dalam bahasa kuno
- 🟢 **Jalan Keberuntungan** - Tampak normal, tapi ada hal-hal yang TIDAK BENAR

## ✨ Fitur Utama

### 🎲 Sistem Keberuntungan Dinamis
- **Random Events**: Setiap playthrough berbeda berdasarkan keberuntungan pemain
- **Chance-based Outcomes**: Pilihan yang sama bisa menghasilkan hasil berbeda di playthrough berikutnya
- **Stat System**: 
  - ❤️ **Kesehatan** - Berkurang dari ancaman fisik
  - 🧠 **Kejiwaan** - Berkurang dari kejadian mengerikan (mencapai 0 = bad ending)
  - ✨ **Keberuntungan** - Menentukan peluang sukses berbagai pilihan

### 🎭 Multiple Paths & Endings
- **12+ Unique Endings**, setiap sesuai dengan pilihan pemain
- **Branching Narrative** - Cerita berkembang berdasarkan pilihan
- **Konsequential Choices** - Setiap keputusan punya dampak nyata

### 📚 Atmospheric Writing
- **Deskripsi Vivid** - Cerita yang menggabungkan horor, fantasi, dan mystery
- **Pacing yang Dinamis** - Narasi dengan jeda dramatis
- **World Building** - Dimensi aneh dengan logika sendiri

## 🎮 Cara Bermain

```bash
python main.py
```

1. Masukkan nama karakter kamu
2. Baca narasi dengan seksama (ini penting untuk atmosfer!)
3. Pilih tindakan yang ingin kamu ambil (ketik angka 1/2/3)
4. Lihat konsekuensi dari keputusanmu
5. Nikmati ending yang unik

## 📊 Sistem Stat

Setiap karakter dimulai dengan:
- **Kesehatan**: 100 (full health)
- **Kejiwaan**: 100 (sanity meter)
- **Keberuntungan**: Random 1-10 (sangat mempengaruhi outcome!)

Keberuntungan tinggi → Hasil positif lebih mungkin
Keberuntungan rendah → Outcome lebih berbahaya atau penuh tantangan

## 🎯 Contoh Paths

### Path 1: SI Pembebas Menara
- Pilih Menara Merah
- Keberuntungan tinggi → Temukan Kristal
- Bantu makhluk dalam menara
- Akhiri dengan: PEMBEBAS YANG TERSESAT

### Path 2: Si Penari Abadi  
- Pilih Jalan Keberuntungan
- Keberuntungan rendah → Temui para penari
- Bergabung dalam tarian
- Akhiri dengan: PENARI ABADI (trapped forever)

### Path 3: Penjaga Pengetahuan
- Pilih Gapura Misteri
- Keberuntungan tinggi → Figur itu menbantu
- Pelajari rahasia dimensi
- Akhiri dengan: PENJAGA PENGETAHUAN TERLARANG

## 🎲 Element Acak yang Mempengaruhi

- **Kristal Biru** muncul random saat di Menara
- **Figur Transparan** berperilaku berbeda tergantung keberuntungan
- **Penari** hanya muncul jika keberuntungan pemain cukup rendah
- **Portal Pulang** punya 50% chance untuk membawa bencana

## 💻 Technical Stack

- **Python 3.x**
- **Library**: `random`, `time`, `sys`
- **Paradigm**: Object-Oriented Programming (OOP)

## 🏗️ Struktur Code

```
PerawalanAventur (Class)
├── Menyimpan stat pemain
└── Method untuk update stat

MysteryAdventureBot (Class)
├── Intro & narasi
├── Chapter paths (3 main branches)
├── Multiple outcomes untuk setiap path
├── Bad endings & good endings
└── Ending display system
```

## 🎬 Ending List

1. **Pembebas Tersesat** - Membebaskan makhluk dari menara
2. **Misi Pembebasan** - Belajar tentang kristal & ratusan jiwa terperangkap
3. **Pengetahuan Tersembunyi** - Belajar rahasia multi-dimensi
4. **Penemu Kebenaran** - Menyadari dimensi adalah simulasi
5. **Penari Abadi** - Terdampar menari selamanya
6. **Pelarian Berbahaya** - Escape tapi sesuatu mengikuti
7. **Penyembuh Melalui Seni** - Musik membebaskan makhluk
8. **Adaptasi Dunia Baru** - Memilih tinggal di dimensi baru
9. **Kembali dengan Kebenaran** - Pulang tapi 3 tahun telah berlalu
10. **Portal Bencana** - Makhluk aneh keluar ke dunia asli
11. **Terkurung Abadi** - Menjadi detak jantung Menara
12. **Jiwa Terbuang** - Kehilangan seluruh ingatan

## 🔄 Replayability

- Random stat keberuntungan setiap permainan
- 3 main paths berbeda
- 12+ possible endings
- Pilihan sekunder yang berbeda-beda
- **Total kemungkinan cerita:** 100+ unique story combinations!

## 💡 Tips Bermain

- 🔴 **Jangan terburu-buru** membaca! Narasi itu penting untuk pengalaman
- 🎲 **Keberuntungan tinggi** tidak selalu berarti "good ending"
- 🧠 **Perhatikan statistik** - kejiwaan bisa jadi kunci
- 🔁 **Main berkali-kali** untuk menemukan semua path tersembunyi

---

**Dibuat oleh:** Mystery Adventure Bot Development Team
**Versi**: 1.0
**Genre**: Interactive Fiction / Text Adventure / Horror-Fantasy
**Tema**: Misteri Dimensi, Konsekuensi Pilihan, Survival

*"Setiap pilihan membawa konsekuensi yang berbeda. Bisakah kamu keluar dari dimensi ini? Atau apakah kamu akan menjadi bagian darinya?"*