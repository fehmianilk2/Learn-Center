#Generators
#Generator bellekte yer kaplamadan veri üretir.

# def cube():
#     result=[]

#     for i in range(5):
#         result.append(i**3)
#     return result


def cube():
    for i in range(101):
        yield i**3

generator=cube()
iterator=iter(generator)
for i in range(101):
    print(next(iterator))

