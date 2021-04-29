class NumberMeta(type):
    class_number = 0

    def __new__(cls, name, bases, attrs):
        nr = type.__new__(cls, name, bases, attrs)
        nr.class_number = cls.class_number
        cls.class_number += 1
        return nr

class Cls1(metaclass=NumberMeta):
    
    def __init__(self, data):
        self.data = data

class Cls2(metaclass=NumberMeta):
    
    def __init__(self, data):
        self.data = data

if __name__ == "__main__":
    main()

 
 

print(Cls1.class_number)
print(Cls2.class_number)
assert (Cls1.class_number, Cls2.class_number) == (0, 1)

a, b = Cls1(''), Cls2('')

assert (a.class_number, b.class_number) == (0, 1)
