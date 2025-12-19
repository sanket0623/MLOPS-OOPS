class Employee:

    _uuid = 0 ## static attribute

    def __init__(self, emp_id, designation, salary):
        self.id = Employee._uuid
        Employee._uuid += 1
        self.designation = designation
        self.salary = salary
        self.__name = "Default Name"

    @staticmethod
    def get_uuid():
        return Employee._uuid

    @staticmethod
    def set_uuid(value):
        Employee._uuid = value

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


sam = Employee(123, 'Software Engineer', 20000)
print(Employee.get_uuid())

Employee.set_uuid(100)
print(Employee.get_uuid())

sanket = Employee(123, 'Software Engineer', 20000)
print(Employee.get_uuid())