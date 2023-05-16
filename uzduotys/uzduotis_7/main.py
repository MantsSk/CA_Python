def division(a, b):
    result = 0
    try:
        result = a / b
        return result
    except:
        print("Negalima dalyba iš 0")
        return None


while True:
    try:
        a = int(input("Input the first number: "))
        b = int(input("Input the second number: "))
        result = division(a, b)
        if result:
            print("Division successful. Result is:", result)
        break
    except ValueError:
        print("Please input an integer number")
        continue
