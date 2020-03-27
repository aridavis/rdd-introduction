#### Notes:
- Silahkan baca dulu teori singkat di bawah
- File untuk cloudera adalah yang .ipynb


Di pertemuan kali ini, kita bakal membahas tentang
- RDD Introduction
- RDD Operation

## Spark
Sebelum masuk lebih lanjut, kita harus mengetahui terlebih dahulu apa itu **Spark**.
**Apache Spark** adalah sebuah sebuah mesin open source yang digunakan untuk memproses dan menganalisa data yang sangat banyak. Kerjanya juga seperti **Hadoop MapReduce**.

## RDD Introduction

### Apa itu RDD?
**RDD** adalah kependekan dari "**Resilient Distributed Dataset**". **RDD** adalah data struktur fundamental dari Apache Spark. **RDD** di Apache Spark adalah sebuah **immutable collection** dari object-object yang mengkomputasi node yang berbeda dari sebuah cluster.

### Apa maksud RDD?

#### Resilient
Toleran terhadap kesalahan dengan bantuan grafik turunan RDD yaitu DAG sehingga mampu menghitung ulang partisi yang hilang atau rusak.

#### Distributed
Dikatakan distributed karena data tersebar di be.berapa nodes

#### Dataset
Mewakili records dari data yang sedang kita kerjakan. User dapat mengimport data set yang beragam seperti JSON, CSV, txt atau JDBC yang tidak ada struktur data spesifik.

### Mengapa kita menggunakan RDD?
Kunci utama dibalik konsep dari pembuatan RDD adalah:
- Iterative Algorithm
- Tools data mining yang interaktif
- Melawan DSM (Distributed Shared Memory) adalah abstraksi yang sangat umum dan sulit untuk diimplementasikan secara efisien pada kesalahan cluster. Untuk perbedaan RDD dan DSM, kalian boleh browse sendiri ya.

### Fitur Spark RDD
- **In-memory Computation**
  Spark RDD punya ketentuan dalam in-memory computation. Dia akan memasukkan data ke dalam RAM dibandingkan Disk
- **Lazy Evaluations**
  Di sini, data tidak dikomputasi secara benar-benar. Dia hanya mengingat semua operasi yang dijalankan, untuk detailnya kalian bisa kunjungi link ini https://data-flair.training/blogs/apache-spark-lazy-evaluation/
- **Fault Tolerance**
  Spark RDD toleran terhadap kesalaahn karena mereka mengambil data dari garis keturunan data untuk membangun kembali data yang hilang secara otomatis.
- **Immutability**
  Data aman untuk dibagikan di seluruh proses. Hal ini juga dapat dibuat atau diambil kapan saja dengan membuat caching, dsb.
- **Partitioning**
  Partisi adalah unit dasar paralelisme dalam Spark RDD. Setiap partisi adalah satu divisi logis dari data yang bisa berubah.
- **Persistence**
  User dapat RDD mana yang ingin mereka gunakan atau memilih strategi dalam penyimpanan untuk mereka.
- **Coarse-grained Operations**
  Jika kita ingin mengganti data dengan metode **Coarse-grained Operations**, maka semua datanya akan berubah. Kita tidak bisa mengganti datanya satu per satu.
- **Location-Stickiness**
  RDD mampu menentukan preferensi penempatan unutk menghitung partisi.


## RDD Operations

Terdapat 2 jenis transformasi:
- **Narrow Transformation**
- **Wide Transformation**

Untuk detail detail operasinya kalian bisa buka link ini
https://data-flair.training/blogs/spark-rdd-operations-transformations-actions/

Web di atas juga memberikan informasi RDD Spark yang sangat lengkap

Untuk contoh kodingan map reduce, silahkan buka file .py di atas