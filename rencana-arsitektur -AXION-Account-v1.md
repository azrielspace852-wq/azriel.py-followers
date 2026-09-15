# RENCANA ARSITEKTUR AXION ACCOUNT
* **Status Dokumen :Draft**
* **Di Buat Oleh : AZRIEL (Owner/CEO)**
* **Di Sempurnakan Oleh : -**
---
## Teknologi mobile Yang Di Gunakan

**Nitron (pembungkus Web Ke Apk)**

***dengan catatan :*** ***Dapat Berubah menjadi Gradle sewaktu waktu. tergantung fitur, dan kebutuhan.***

---
## Account Menggunakan
1. Email inbound only
2. Domain :
* -axn.cc.cd
## workers 
1. Database Account
2. Gateway Pembayaran
* ***(akan di diskusikan)***
---
## Fitur
**1. upgrade To Go (Paket Go. Berbayar)**

**penjelasan :**
* Perlu Membayar Kepada Layanan. Senilai [akan di tentukan...] per bulan.
* Mendapatkan fitur yang terkunci di fitur paket free.
* mendapatkan akses membuat 10 akun per minggu per perangkat
* mendapatkan Akses penyimpanan ke R2 Database
* mendapatkan 2gb storage (1GB D1 Database, 1GB R2 Database)

**catatan :**
* Fitur Go, adalah Per Akun Per Perangkat.
(Lalu yang di maksud mendapatkan 10 akun per minggu per perangkat itu apa? itu adalah akun yang di Tautkan dengan akun Go tersebut, bisa 10 akun per minggu per perangkat)
* Sudah Bisa Login Sebagai Go Di Layanan AXION Lainya yang mendukung fitur User Go
---
**2. Free. (Paket Free. Gratis Terbatas)**

**penjelasan :**
* User Free, Tidak Perlu Membayar Tagihan Bulanan kepada Layanan Kami.
Dengan ***Catatan*** Beberapa Fitur Akan Di Batasi.
* Akses Penyimpanan, Bukan Di R2. Melainkan Di Github. Sedangkan kalau Hanya Teks. itu Tetap di D1.
* Batas Penyimpanan Hanya 500mb (250mb di Github untuk file, contoh nya ,gambar, video, dsb. Dan 250mb. Di D1 untuk Teks)
---
**3. Iklan : Iklan yang di gunakan menggunakan Google Ads (untuk pendapatan tambahan), Hanya untuk User Free.**

**penjelasan :**

* Iklan Hanya Tampil Di pengguna Free. Pengguna Go, Tidak akan mendapatkan iklan.
---
**4. Membuat Akun (2 Akun per minggu per perangkat untuk user free. Dan 10 akun per perangkat per minggu, untuk User Go), dan akun kedua dan seterusnya, harus menggunakan akun pemulihan (wajib, dan harus dari AXION Account. Account pemulihan Hanya bisa Menggunakan Account utama, Account utama Adalah Account pertama yang di buat user)
Sedangkan Akun Utama, bisa di Tautkan Dengan Akun Google, Atau Email dari pihak lain, seperti Hotmail, yahoo, dsb.**

**Penjelasan :**
* Membuat 2 akun per minggu per perangkat untuk user free. dan 10 akun per perangkat per minggu untuk user Go, Agar user tidak bisa spam membuat akun secara masal.
* Akun Ke 2 dan seterusnya. Harus menakutkan Akun utama (Bisa di Gunakan untuk pemulihan, dan agar sistem tidak harus scan perangkat per akun, jadi informasi perangkat, hanya berdasarkan akun utama user.) dan wajib menggunakan AXION Account.
* Akun utama, bisa di Tautkan dengan akun Google, atau email dari pihak Lain. contohnya Hotmail, Proton mail, yahoo, dsb.
Dan Email sementara juga bisa di gunakan. akan tetapi. resiko di tanggung user. dan harus di berikan peringatan. karna, jika user menggunakan email sementara untuk pemulihan akun utama, dan jika email sementara sudah expired, maka email tersebut sudah tidak aktif, dan tidak bisa di gunakan.
---