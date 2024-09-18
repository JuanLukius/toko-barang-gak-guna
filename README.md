#  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

pengimplementasian data delivery diperlukan untuk mempermudah proses pertukaran informasi, menjaga keamanan data dan efisiense serta pengambilan keputusan

# Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

XML dapat melakukan semua yang JSON dapat lakukan, selain itu, XML juga dapat memuat data type seperti boolean, dates, images dan namespaces. XML biasanya digunakan untuk dokumen markups, XML memang dapat melakukan semua yang dapat dilakukan oleh JSON, namun struktur XML lebih sulit untuk dimengerti dan biasanya sulit dibaca dalam pembuatan projek kompleks. Struktur JSOn lebih mudah untuk dibaca dan dimengerti dalam pembuatan proyek besar, selain itu, meski apa yang dapat dilakukan JSON terbatas, JSON memiliki size data yang lebih kecil dan waktu pemrosesan data yang lebih cepat. Mengapa JSON lebih populer daripada XML? karena banyak pekerjaan yang tidak membutuhkan apa yang dapat dilakukan oleh XML, oleh karena itu JSON menjadi pilihan dengan alasan lebih efisien dikarenakan JSON yang lebih mudah dikonstruksi dan dibaca, memiliki size yang lebih kecil dan waktu pemrosesan yang lebih cepat. 

# Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

method is_valid() pada django berfungsi untuk mengecek data yang masuk dari user apakah sesuai dengan format field yang kita punya, method ini sangat penting untuk memastikan input dari user sesuai dengan format yang diharapkan contohnya pada field tugas ini yaitu "name", "price", "description", "type", bila format field yang dimasukkan oleh user misalnya pada kategori price bukan merupakan integer, maka input tidak valid, apabila tidak ada method is_valid() maka price yang berisikan misalnya "kucing" akan tetap dianggap input yang valid. Mengapa hal ini penting? karena dengan ketidakseragaman datatype yang dimasukan user dapat menghasilkan kekacauan pada saat program berjalan. Contohnya price yang berisikan "kucing", apabila masuk kedalam method is_not_a_waste_of_money(self) pada tugas ini. maka fungsi akan membandingkan string dengan angka.

# Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token berfungsi sebagai generator token random yang hanya digunakan sekali pakai, biasanya token yang digenerate oleh csrf berupa belasan kombinasi random yang sulit untuk ditebak. Guna csrf_token adalah untuk mencegah adanya serangan dengan mengenerate token random saat pengguna login dan mengirim request pada django sehingga setiap alamat pengaksesan unik. Bila tidak ada csrf_token, maka penyerangan siber akan lebih mudah dilakukan karena hilangnya penghalang yang sulit ditebak oleh penyerang.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. membuat format base.html yang digunakan sebagai basis format direturn
2. membuat forms.py yang berfungsi sebagai formating input pengguna berdasarkan field
3. membuat create_item_entry.html yang berfungsi sebagai entry item yang dimasukkan pengguna
4. memodifikasi main.html agar dapat mengeluarkan format item yang telah diadd oleh pengguna
5. membuat program pada views.py yang mengecek valid tidaknya input form yang diberikan oleh pengguna
6. menambahkan url path baru untuk membawa pengguna kepada path untuk menambahkan item baru
7. membuat konversi output dalam format JSON,XML dan membuat fungsi untuk mengeluarkan output item pada JSON dan XML dengan id item
8. menambahkan url yang meredirect path untuk setiap format output(JSON,XML,JSON by id dan XML by ID
9. melakukan pengecekan output pada postman 

