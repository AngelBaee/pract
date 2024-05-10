login = str(input("Enter your name:  "))
passw = str(input("Enter your password:  "))
repeat = str(input("Repeat the password:  "))

if passw != repeat:
    print("Password is incorrect")
    repeat = str(input("Repeat the password:  "))
else:
    print("Choose a category:  ")
    next =   next_step = str(input("Art, Music, Programming: "))
    if next == "Art":
        print(f'{login} is intersetd to art')
    if next == "Music":
        print(f'{login} is intersted to music')
    if next == "Programming":
        print(f'{login} is intersted to programming')
        
                
