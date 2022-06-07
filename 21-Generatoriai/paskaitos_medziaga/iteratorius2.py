
for i in range(6):
    print(i)



iteratorius = iter(range(6))
while True:
    try:
        print(next(iteratorius))
    except StopIteration:
        break
