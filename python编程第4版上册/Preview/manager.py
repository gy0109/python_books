
from person_start import Person


class Manager(Person):
    def giveraise(self, percent, bonus=0.1):
        # self.pay *= (1.0 + percent + bonus)
        Person.giveraise(self, percent + bonus)   # 从新增强定义它  而不是直接替换
        """
        instance.method(arg1, arg2)
        class.method(instance, args)   等价方法,第一种会转换成第二种,
        """


if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.last_name())
    tom.giveraise(.20)
    print(tom, '\n', tom.pay)
