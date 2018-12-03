
class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return '<%s ==> %s>' % (self.__class__.__name__, self.name)


if __name__ == '__main__':
    bob = Person('Bob Smith', 32, 30000, 'software')
    sue = Person('Sue Jones', 35, 40000, 'harfware')
    print(bob.name, sue.pay)

    print(bob.name.split()[-1])
    sue.pay *= 1.10
    print(sue.pay)
