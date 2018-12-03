
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


class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveraise(self, percent, bonus=0.1):
        Person.giveraise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith', 35)
    sue = Person('Sue Jones', 35, 40000, 'hardware')
    tom = Manager('Tom Doe', 50, 50000)
    print(bob.name, sue.pay, tom.name)
    for obj in (bob, sue, tom):
        obj.giveraise(.10)
        print(obj)
