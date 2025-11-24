from datetime import datetime
#Tarih ve saat işlemleri yapmanı sağlar.
result =datetime.now() #Şu anın tarh ve saati
result=datetime.now().year #Şu anın yılı. Year kısmını değiştirerek ay, gün, saat gibi bilgilere de ulaşabiliriz.
result=datetime.ctime(datetime.now()) #Şu anın tarih ve saatini daha okunabilir bir formatta verir.
result=datetime.strftime(datetime.now(),"%Y") #Yıl bilgisi
result=datetime.strftime(datetime.now(),"%A") #Haftanın günü
result=datetime.strftime(datetime.now(),"%B") #Ay bilgisi
t1="21 April 2023 hour 10:12:30"
dt=datetime.strptime(t1,"%d %B %Y hour %H:%M:%S") #String ifadeyi datetime objesine çevirir.

print (result)