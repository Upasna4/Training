def sum():
    a=5
    b=6
    c=a+b
    print(c)

    def sub():
        nonlocal c
        d=5
        print(c-d)
    sub()          #is func ko sum func ke andar cal krna h...this is nested func
sum()       #jo func sbse bahar h use sbse last m cal krna hai