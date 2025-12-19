class Employee:
    def __init__(self, emp_id, designation, salary):
        self.id = emp_id
        self.designation = designation
        self.salary = salary
        self.__name = "Default Name"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


sam = Employee(123, 'Software Engineer', 20000)
print(sam.get_name())
sam.set_name('sanket')
print(sam.get_name())