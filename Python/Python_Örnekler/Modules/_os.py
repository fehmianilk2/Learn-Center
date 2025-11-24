import os
#İşletim sistemi ile ilgili bilgiler ve işlemler sunar.

result=os.name
# os.chdir('C:\\')   -ye bir dizine geçmek için kullanılır.
# os.mkdir("X")      -Yeni klasör oluşturur.
# os.makedirs("x/y") -İç içe klasörler oluşturur
# os.rmdir()         -Klasör silme
os.listdir() #Dosyanın içeriğini listeler
#https://docs.python.org/3/library/os.html   Daha fazla işlem için
print(result)