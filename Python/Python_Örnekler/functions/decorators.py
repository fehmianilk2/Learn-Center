def my_decorator(func):
    def wrapper():
        print("Fonksiyon çağrılmadan önceki işlem.")
        func()
        print("Fonksiyon çağrıldıktan sonraki işlem.")
    return wrapper

def say_hello():
    print("Merhaba")

def say_goodbye():
    print("Hoşçakal")

say_hello=my_decorator(say_hello)

say_hello()