class Employee:
    raise_amout = 10
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname (self):
        return "{}{}".format(self.first,self.last)
    def applyraise(self):
        self.pay = int(self.pay * self.raise_amout)
        return self.pay


class Developer(Employee):
    raise_amout = 0.1
    def __init__(self,first,last,pay,program_lang):
        super().__init__(first,last,pay)
        self.program_lang = program_lang



obj = Developer("Rajasekhar","Reddy",5000,"Python")
print(obj.fullname())
print(obj.applyraise())
print(obj.program_lang)
