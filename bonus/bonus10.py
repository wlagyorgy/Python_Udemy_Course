try:
    width = int(input("Recangle width: "))
    length = int(input("Rescangle length: "))
    if length == width:
        exit('It looks like a square')
    area = width * length
    print(area)
except ValueError:
    print("Please enter a number.. ")
