def detail(name=None,age=None):
    if name is not None and age is not None:
        print("hello",name,"your age",age)
    elif name is None and age is None:
        print("hello user you have not defined your name or age")
    elif name is not None and age is None:
        print("hello","name")
    elif name is None and age is not None:
        print("hello user,your age is",age)
detail()
detail("upasna",23)            #funcoverloading
detail("upasna")