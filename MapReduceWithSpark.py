#Inisialisasi
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

# Membuat Collection RDD
number = sc.parallelize([1,2,3,4])

#kalau kita langsung print number, maka outputnya seperti baris pertama output
print(number)

#mengoutputkan number
print(number.collect())

#mengoutputkan number satu per satu
for i in number.collect():
    print(i)


#Fungsi Map
# Map Berfungsi untuk mengubah seluruh data yang ada dalam satu collection

number = sc.parallelize([1,2,3,4])

print("Sebelum Mapping")
print(number.collect())

# Mapping
# Ada 2 cara :
# 1. Membuat Function Baru
# 2. Lambda Function

# Membuat Function Baru
def addByOne(x):
    return x + 1

print("Ditambah Satu dengan Function")
number = number.map(addByOne)
print(number.collect())

# Dengan Lambda Function
# Kita contohkan, kita mau mengkalikan semua datanya dengan 2
number = number.map(lambda x : x * 2)
print("Dikali 2 dengan Lambda Function")
print(number.collect())


# Fungsi FlatMap

# Fungsi FlatMap akan membuat semua array menjadi 1 array
# Contoh

# ada sebuah variable yang menyimpan array dalam array

arr = sc.parallelize([[1,2,3,4],[5,6,7,8]])

# Kalau Kita Map si Array, outputnya akan menunjukkan array dalam array
print(arr.map(lambda x : x).collect())

# Sekarang kita coba flatmap, dia akan menggabungkan semua array di dalamnya ke dalam 1 array
print(arr.flatMap(lambda x : x).collect())


# Sekarang kita akan mengeread text dari words.txt

#Read File
words = sc.textFile("words.txt")

# Sekarang, kita ingin ngesplit kata" tersebut 1 by 1,
# Semua data yang sudah di split, dimasukkan ke dalam 1 array berdasarkan Line dari setiap text
splitWords = words.map(lambda x : x.split(" "))

# Jika kita ingin mengambil datanya sebanyak N data, maka kita perlu menggunakan function take(N)
splitWords.take(5)


# Kita Flattenkan semua datanya
flattenWords = splitWords.flatMap(lambda x : x)


# Kita Map Reduce
mapped = flattenWords.map(lambda x : (x,1))  
# Kodingan di atas akan membuat semua words menjadi sebuah tuple untuk di map reduce (kata, 1)
# Untuk membuktikannya silahkan ketikkan mapped.collect()

# Di sini kita bakal menampilkan semua word (secara distinct) dan total berapa kali nongol di words
reduced = mapped.reduceByKey(lambda x, y : (x+y))
print(reduced.take(5))