#İterators
mylist=[1,2,3,4,5]

itertor=iter(mylist)

# print(next(itertor))
# print(next(itertor))
# print(next(itertor))
# print(next(itertor))
# print(next(itertor))

while True:
    try:
        element=next(itertor)
        print(element)
    except StopIteration:
        break
#For döngüsü arka planda iterator kullanır. Bu while döngüsünün yaptığı işlemi yapar.
