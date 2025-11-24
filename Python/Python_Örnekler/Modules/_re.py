import re
#Arama İlemleri için kullanılır. Regular expression.
str="Fehmi Anıl Karabıyık çok büyük bir yazılımcı"
result=re.findall("çok",str)   #İstenen karakteri bulur
result=re.split(" ",str)       #İstenen karakterden sonrasını ayırır
result=re.sub("a","e",str)     #İstenen karakteri değiştirme
result=re.search("Anıl",str)
print(result)