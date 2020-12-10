num_list = [4, 77, 5, 43, 7, 85]
num_tup = (7, 5, 3, 77, 4, 2, 6)
num_set = {4, 2, 4, 5, 2, 5, 22, 4}

# LISTS
# In place sorting for lists
num_list.sort(reverse=True)

# Return a sorted copy (not in place)
num_list_copy = sorted(num_list)
# print(num_list_copy)
# print(num_list)

# TUPLES
# No in place sorting for tuples
num_tup_copy = sorted(num_tup, reverse=True)  # Converts a tuple to list after sorting
# print(num_tup_copy)

# SETS
# No in place sorting for sets
num_set_copy = sorted(num_set)
# print(num_set_copy)  # Converts the set to a list

# Sorting based on keys (similar to comparator)
nums = [-6, -71, 5, 3, -3]
nums_copy = sorted(nums, key=abs)
print(nums_copy)

from operator import attrgetter


class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    def __repr__(self): return f'{self.name} , {self.designation} : ${self.salary}'  # similar to toString()

    @staticmethod
    def sort(ls):
        return sorted(ls, key=lambda emp: emp.name)  # Sort the employee objects based on name

    @staticmethod
    def sort_2(ls):
        return sorted(ls, key=attrgetter('salary'))


srini = Employee('Srinivas', 'Software Engg', 25000)
laura = Employee('Laura', 'Interpreter', 30000)
emps = [srini, laura]
print(Employee.sort(emps))

# Specialized sorting for objects using attrgetter

abha = Employee('Abha Jain', 'Financial Analyst', 35000)
emps.append(abha)
print(Employee.sort_2(emps))  # tells the function to sort based on the 'salary' attribute of the employee object
