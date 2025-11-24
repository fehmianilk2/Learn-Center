def usalma(number):
    def inner(power):
        return number ** power
    return inner
two=usalma(2)
result=two(3)

def yetki_sorgula(page):
    def inner(role):
        if role=="admin":
            return f"{page} sayfasına erişim izniniz var"
        else:
            return f"{page} Sayfasına erişim izniniz yok"
    return inner
user1=yetki_sorgula("Ürünler")
result=user1("admin")

print(result)