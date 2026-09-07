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