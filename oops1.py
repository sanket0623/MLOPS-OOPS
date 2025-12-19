class Employee:
    def __init__(self, emp_id, designation, salary):
        self.id = emp_id
        self.designation = designation
        self.salary = salary


sam = Employee('Sammy', 'Software Engineer', 20000)
print(sam.id)
print(sam.designation)
print(sam.salary)