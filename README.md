Nama : Justin Lie
NPM : 2506591961
Kelas : PBP B

Second Year at Fasilkom UI

### Tugas 1

1. Dalam pengembangan website di tugas 1 ini, saya hanya baru menggunakan element "section" yang berguna untuk memisahkan bagian website yang tidak berkaitan dengan satu sama lain, seperti profile dan discography (masing-masing section memiliki inti tersendiri). Sayangnya, saya belum memiliki keperluan untuk mengimplementasikan "aside" ataupun "article". Hal ini karena "aside" berguna untuk menandai konten pendukung dalam suatu section, sedangkan "article" berguna untuk menandai teks yang dapat berdiri sendiri tanpa context dari websitenya. Dengan adanya element semantic ini, pengembangan website akan jauh lebih rapi karena dapat ditandai pembagian dari content web dan bukan hanya menggunakan "div" yang terlalu general.

2. Saat membuat website tetap responsive antara desktop dan mobile, ada beberapa format grid yang perlu saya ubah. Salah satu contohnya ada grid di section Discography. Di desktop, section grid ini terdiri dari 2 column, dimana bagian kiri mengandung judul, sedangkan bagian kanan ada konten intinya. Saat digunakan di mobile, grid tersebut harus berubah menjadi 1 column, dimana judul bagian atas dan konten inti di bagian bawah. Saat membuat UI section tersebut, saya memutuskan bahwa ukuran judul dari section tersebut tidak boleh berubah agar tetap jelas dilihat oleh user dari platform manapun.

3. Salah satu batasan yang saya rasakan saat membuat website static ini adalah sulitnya mengupdate konten di HTML. Hal ini karena setiap bagian konten yang berbeda-beda perlu diupdate satu per satu. Selain itu, saya merasa website saat ini kurang adanya interaksi dari user (seperti memberi komentar ataupun mengirim pesan via web). Dengan iterasi selanjutnya, saya berharap bisa menerapkan sebuah main database agar dapat menambah dan mengubah konten, serta membuat sarana agar user bisa berinteraksi dengan web secara langsung. 

#### AI Disclosure

Selama pengerjaan tugas 1 ini, saya menggunakan Gemini sebagai alat bantu, dimana saya terbantu oleh Gemini dalam menganalisa syntax sudah diberikan pada Tutorial 1, serta mencari referensi dari internet untuk lebih memahami pengunaan syntax-syntax tertentu. Selama menggunakan AI tersebut, saya hanya melakukan prompting untuk memahami cara suatu syntax bekerja dan tidak memintanya untuk membantu dalam pembuatan HTML.

Berikut tertera salah satu hasil prompting yang saya lakukan ke Gemini:

Prompt: 

>**clamp(3rem, 7vw, 5rem)**

Result: 
>The CSS declaration clamp(3rem, 7vw, 5rem) sets a responsive, fluid value that scales dynamically based on the viewport width while respecting strict minimum and maximum boundaries.
>
>How It Works
>
>- Minimum value (3rem): The property value will never shrink below 3rem (typically 48px if your root font size is 16px), ensuring it remains legible or appropriately sized on smaller screens. [1] (https://css-tricks.com/almanac/functions/c/clamp/), [2] (https://uxdesign.cc/understanding-css-clamp-for-typography-a-guide-for-ui-designers-6f522c2ed90f)
>
>- Preferred/Ideal value (7vw): The value scales fluidly as a percentage of the viewport width (7% of the current screen width).
>
>- Maximum value (5rem): The value will never grow larger than 5rem (typically 80px), preventing it from becoming disproportionately huge on wide desktop monitors
>
>Behavior Across Screen Sizes
>
>- On small screens (phones): 7vw is smaller than 3rem, so the browser clamps the value to 3rem.
>
>- On mid-sized screens (tablets/laptops): 7vw falls between 3rem and 5rem, so the element scales smoothly and dynamically as you resize the window.
>
>- On large screens (desktops): 7vw exceeds 5rem, so the browser caps the value at 5rem.

### Tugas 2

1. Saat pengguna membuka halaman portofolio baru, requestnya akan diarahkan ke urls.py dari project tersebut untuk mendapatkan semua alamat page dalam website tersebut. Dalam urls.py project, landing page ("") dari project memiliki fungsi "include()" yang merujuk kepada urls.py app main. Dengan fungsi include tersebut, url pada urls.py app akan terhubung kepada urls.py di project. Saat hendak berpindah page/url, pemanggilan url tersebut akan merujuk pada suatu function di views.py. Function tersebut akan mengambil data dari models dan lalu me-render template page yang sudah disediakan dengan data dari model. Hasil akhir template tersebut melewati kembali views.py, urls.py di app, urls.py di project dan akhirnya akan dikirimkan kembali ke browser pengguna untuk ditampilkan.

2. Data untuk website memang sebaiknya disimpan di models daripada template, karena penggunaan models adalah untuk menyimpan data dari suatu objek, seperti project. Seiring waktu, jumlah project yang akan dibangun akan meningkat sehingga perlu ada penyesuaian pada website. Apabila template digunakan untuk menyimpan data, syntax yang sama perlu di ulang berkali-kali untuk menyimpan data project baru. Alhasil, template akan terlihat kurang rapi. Di sisi lain, apabila data disimpan di dalam models, website dapat lebih mudah dikembangkan dan kode html di template menjadi lebih rapi. 

3. "makemigrations" di Django adalah command untuk menyiapkan file untuk melakukan migration suatu model ke project, sedangkan "migrate" adalah command untuk mengeksekusi file tersebut terhadap proyek. Ibaratnya, "makemigration" adalah prosedur untuk mengcompile suatu program ke "machine executable file" dan "migrate" adalah prosedur untuk menjalankan "machine executable file" tersebut. Sebagai contoh, dalam sebuah models "Project", kita ingin menambahkan field baru berupa tanggal mulai. Agar field tersebut dapat diimplementasikan dalam Django project, kita perlu menjalankan command "makemigrations" untuk membuat file yang dapat dieksekusi ke Django, lalu menjalankan "migrate" untuk menjalankan file tersebut.

#### AI Disclosure

Selama pengerjaan tugas 2 ini, saya menggunakan ChatGPT sebagai alat bantu, dimana saya terbantu olehnya dalam memahami konsep MVT dan bagaimana untuk mengimplementasinya di Django. Selama menggunakan AI tersebut, saya melakukan prompting untuk memahami konsep dari alur MVT dan tidak memintanya untuk membantu dalam pembuatan HTML secara langsung.

Berikut tertera salah satu hasil prompting yang saya lakukan ke ChatGPT:
>https://chatgpt.com/share/6aa6dbf0-e6f4-83ec-8547-aea1d912e9f9 
