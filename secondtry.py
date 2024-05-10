def call_bae():
    arr = []

    
    for i in range(5):
       wishes = str(input("What do you wish?  "))
       arr.append(wishes)
    result = 0

    for wishes in arr:
        if "M" in wishes or "m" in wishes:
            result +=1 
    print(result)

if__name__="__main__"
call_bae()

    