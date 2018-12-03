import shelve


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


def use_shelve(bob, sue, tom):
    db = shelve.open('person_class_shelve')
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom
    db.close()


def dump_db_classes():
    db = shelve.open('person_class_shelve')
    for key in db:
        print(key, '==> \n', db[key].name, db[key].pay)
    db.close()


if __name__ == '__main__':
    bob = Person('Bob Smith', 35)
    sue = Person('Sue Jones', 35, 40000, 'hardware')
    tom = Manager('Tom Doe', 50, 50000)

    # use_shelve(bob, sue, tom)
    dump_db_classes()
