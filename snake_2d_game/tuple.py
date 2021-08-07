class Employee:
    __name = None
    __id = 0
    __salary = 0

    def __init__(self,name,id,salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_salary(self):
        return self.__salary



balwant= Employee('BALWANT',13,2000)
print(balwant.get_name())
print(balwant.get_id())
print(balwant.get_salary())

'''
balwant.set_name('BALWANT')
print(balwant.get_name())

harry.__name = 'harry'
harry.__id = 10
print(harry.__name)
print(harry.__id)  '''
