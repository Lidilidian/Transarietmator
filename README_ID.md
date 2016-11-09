# Transarietmator
------
([Klik disini untuk petunjuk dengan bahasa Inggris](https://github.com/Lidilidian/Transarietmator/README.md))

Program Pyhton untuk mengecek `msgstr` yang belum diterjemahkan pada berkas Gettext (.po) dan memberikan rekomendasi terjemahan.

Program ini menggunakan Python v.2.7 dan [Microsoft Translator Text API][1] sebagai inti penerjemahan. ketika Anda menjalankan program ini, program ini akan secara otomatis mencari `msgstr` yang belum diterjemahkan dalam file .po dan memberikan rekomendasi untuk Anda berupa hasil terjemahan dan Anda dapat menggunakan hasil itu untuk memperbaiki berkas po Anda, baik itu mungkin untuk menggunakan layanan weblate dan Pootle atau bahkan penerjemahan secara manual.

## How use:
- $ git clone https://github.com/Lidilidian/Transarietmator.git
- $ cd Transariemator
- $ python2.7 transariemator.py 
- Insert Source Language : en // Masukkan bahasa dari sumber file po Anda.
- Insert Your translation language : id // Masukkan bahasa yang ingin Anda jadikan Rekomendasi penerjemahan
- [Klik disini][6] untuk melihat semua kode bahasa yang didukung oleh program ini.

catatan : secara default program ini menggunakan `administration.po` dari [Bauble Project][2] , And harus merubah itu menggunakan file po yang ingin Anda cek pada `transarietmator.py`.

>### Pustaka pendukung :

- [x] [lxml 2.2.8][3] untuk python2.7
- [x] [msti][4] (Terdapat di Repo ini)
- [x] [polib][5] for python2.7 (juga terdapat di repo ini)
- [x] json
- [x] urllib dan urlllib2

>### daftar yang harus dikembangkan lebih lanjut :

- [x] Masukkan untuk penerjemahan
- [ ] Pendeteksi otomatis untuk file sumber
- [ ] Buat argparse untuk mempemudah penggunaaan
- [ ] Simpan hasil output ke file .po yang baru
- [ ] Meningkatkan tampilan

[1]: https://www.microsoft.com/en-us/translator/translatorapi.aspx        "Microsoft Translator Text API"
[2]: https://github.com/Bauble                                            "Bauble Project"
[3]: https://pypi.python.org/pypi/lxml/2.2.8                              "lxml v.2.2.8 library for python2.7"
[4]: https://github.com/Lidilidian/Transarietmator/blob/master/msti.py    "Microsoft Translation API connector"
[5]: https://github.com/Lidilidian/Transarietmator/blob/master/polib.py   "polib library python2.7"
[6]: https://msdn.microsoft.com/en-us/library/hh456380.aspx               "Language Code"

>### Lisensi
Program ini menggunakan lisensi MIT - https://github.com/steptr/MIT-License/blob/master/MIT_License-id.txt

>### Kontribusi dan Masukan
Jika Anda ingin berkontribusi di proyek ini, Segala bentuk masukan bahkan jika hanya sekedar teguran karna kesalahan penulisan akan sangat-sangat berguna, dan jangan malu untuk bersilaturahmi dengan Saya di ([hubungi.aja@gmail.com](mailto:hubungi.aja@gmail.com))Contirbuting and suggestions

>### Terima kasih kepada
- ([@jayvdb](https://github.com/jayvdb) - Mentor Besutkode yang sudah membimbing
- ([@edawine](https://github.com/edawine)) & ([@chocochino](https://github.com/chocochino))- Yang sudah memberikan masukkan-masukkan
- Semua peserta Besutkode dan Teman-teman di Kampus Universitas Muhammadiyah Jakarta
