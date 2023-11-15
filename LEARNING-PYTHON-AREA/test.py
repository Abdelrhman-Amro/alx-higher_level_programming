class tst:
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        print("I AM HERE")
        self.__size = value

obj = tst(10)
