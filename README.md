Tugas 6
# Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

- Javascript memudahkan untuk membuat website yang responsif karena javascript mampu membuat respons yang cepat dan secara real time terhadap aksi pengguna
- Javascript dapat memproses data langsung pada browser sehingga tidak perlu mengembalikan data ke server sehingga dapat meningkatkan waktu responsif sekaligus mengurangi beban yang diterima server
- Javascript memiliki AJAX yang dapat menghasilkan perubahan pada data tanpa harus merefresh kembali halaman website
- Javascript juga memiliki peran untuk memvalidasi form yang dikirim pengguna agar server tidak perlu menerima data yang tidak valid
- Javascript membutuhkan minim pemahaman baru ketika menggunakannya pada platform lain sehingga mempermudah pengguna melakukan pengembangan di platform yang berbeda

# Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?

fetch() digunakan untuk melakukan request HTTP seperti GET atau POST ke server. fetch() secara default bersifat asynchronous, artinya JavaScript tidak akan menunggu hasil dari fetch() untuk melanjutkan eksekusi kode berikutnya. bila tidak ada penggunaan await maka program akan terus berjalan tanpa hasil fetch() terlebih dahulu yang mungkin dapat menyebabkan masalah bila program selanjutnya butuh hasil dari fungsi fetch()

# Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST

Pada request AJAX POST, jika CSRF token tidak ada maka Django akan memblokir permintaan tersebut dikarenakan Django melindungi aplikasi dari serangan dengan CSRF. dengan menggunakan csrf_exempt pada view yang akan menerima request POST dari AJAX maka permintaan tersebut tidak akan diblokir oleh Django 

# Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

pemberihan data sebaiknya dilakukan di backend dikarenakan validasi data di frontend akan lebih mudah untuk dibobol dengan mengirimkan request secara manual atau penonaktifan javascript. Maka dari itu tugas tersebut diberikan ke backend yang harus melakukan pembersihan dan validasi untuk mencegah injection attacks, XSS (Cross-Site Scripting, selain itu front pada setiap platform mungkin berbeda beda sehingga pembersihan di backend lebih efisien dikarenakan konsistensi kode pada segala jenis platform

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1. memodifikasi views agar dapat menyesuaikan dengan perubahan penambahan mood dengan ajax
2. menambahkan url untuk modifikasi dengan ajax
3. merubah konfigurasi pada main.html untuk menyesuaikan dengan penambahan AJAX
4. menambahkan method method dan pada script di main agar dapat menanggapi request pada frontend
5. menambahkan modal modal yang digunakan untuk menambahkan mood
6. mengkonfigurasi ajax untuk menambahkan data mood

Tugas 5
#  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

CSS memiliki urutan prioritas spesifik untuk menentukan mana yang diterapkan saat beberapa selector digunakan pada elemen yang sama. Prioritas diurutkan dari yang tertinggi ke terendah sebagai berikut:

Inline styles
ID selectors
Class selectors, attribute selectors, dan pseudo-classes
Element selectors dan pseudo-elements

# Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Responsive design adalah pendekatan untuk memastikan aplikasi web dapat menyesuaikan tampilan dan fungsionalitasnya dengan berbagai ukuran layar dan perangkat. Ini penting karena meningkatkan pengalaman pengguna, mendukung optimasi mesin pencari (SEO), dan efisiensi dalam pengembangan dengan mengurangi kebutuhan untuk membuat beberapa versi situs.

# Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Margin adalah ruang di luar elemen yang menciptakan jarak dengan elemen lain. Border adalah garis yang mengelilingi elemen, terletak antara margin dan padding. Padding adalah ruang di dalam elemen, yang menciptakan jarak antara konten dan border.


# Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox adalah model layout untuk mengatur elemen dalam satu dimensi, memudahkan distribusi ruang dan penyelarasan. Grid Layout adalah model layout untuk mengatur elemen dalam dua dimensi, memberikan kontrol lebih besar atas tata letak, dan sangat cocok untuk desain yang kompleks.

 
# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. membuat fungsi edit model
2. membuat beberapa file html baru yang berfungsi sebagai fondasi design
3. memodifikasi file views,dan url agar dapat menerapkan edit model
4. menambahkan perubahan pada base.html dan membuat navbar yang di include oleh beberapa file yang ada di tugas 
5. memodifikasi main.html agar bisa menampilkan desain tampilan baru
6. memodfikasi desain menjadi hitam dan putih agar tidak 100% sama
7. git add push commit


