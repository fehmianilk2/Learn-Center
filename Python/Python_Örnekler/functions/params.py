def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme (a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi=="toplama":
        return f1(10,5)
    elif islem_adi=="cikarma":
        return f2(10,5)
    elif islem_adi=="carpma":
        return f3(10,5)
    elif islem_adi=="bolme":
        return f4(10,5)
    else:
        return "gecersiz islem"
    
result1=islem(toplama,cikarma,carpma,bolme,"carpma")
result2=islem(toplama,cikarma,carpma,bolme,"toplama")
result3=islem(toplama,cikarma,carpma,bolme,"cikarma")
result4=islem(toplama,cikarma,carpma,bolme,"bolme")
print("\n",result1,"\n",result2,"\n",result3,"\n",result4)