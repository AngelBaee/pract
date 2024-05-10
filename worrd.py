nn = int(input("Enter the size of array: "))

arr = []
prr = []

for i in range(nn):
    dd = str(input("Enter the word: "))
    arr.append(dd)
    if "Y" in dd or "y" in dd:
        prr.append(dd)

print(prr)    