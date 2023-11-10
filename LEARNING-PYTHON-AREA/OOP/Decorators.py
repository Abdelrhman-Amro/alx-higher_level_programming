def student(f):
    def nested():
        print("Hello I am nested function inside to with decorator property")
    f()
    return nested

@student
def decorated():
    print("I am here inside with decorator property")

decorated()
