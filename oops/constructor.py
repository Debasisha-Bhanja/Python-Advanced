import inspect
class Employee:
    empCount = 0
    def __init__(self, *args):

        self.name = args[0]
        self.salary = args[1]
        Employee.empCount += 1


    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

emp1 = Employee("Srinivas", 2000)
emp2 = Employee("KolapaRTHI", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
emp4=Employee(22,3333,45)