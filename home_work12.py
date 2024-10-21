"""Homework 12"""


class Student:
    """Student class"""

    name: str
    age: int
    values: list[int]

    def __init__(self, name: str, age: int) -> None:
        """Init student"""
        self.name = name
        self.age = age
        self.values = []

    def __str__(self) -> str:
        """String representation"""
        return f"{self.name} {self.age}"

    def __repr__(self) -> str:
        """String representation"""
        return f"Student({self.name}, {self.age} age)"

    def __gt__(self, other) -> bool:
        """Best grades"""
        return self.get_average() > other.get_average()

    def add_value(self, value: int) -> None:
        """Add value to student"""
        self.values.append(value)

    def get_average(self) -> float:
        """Average score"""
        try:
            return sum(self.values) / len(self.values)
        except ZeroDivisionError:
            return 0


class Group:
    """Group class"""

    students: list[Student]
    name: str

    def __init__(self, name: str) -> None:
        """Init group"""
        self.name = name
        self.students = []

    def add_student(self, student: Student) -> None:
        """Add student to group"""
        self.students.append(student)

    def del_student(self, student: Student) -> None:
        """Del student from group"""
        self.students.remove(student)

    def best_student(self) -> Student:
        """Find the best student by average score in the group"""
        return max(self.students, key=lambda student: student.get_average())

    def group_best_student(self: list["Group"]) -> "Group":
        """Find the group with the best student among all groups"""
        best_student = None
        best_group = None

        for group in self:
            for student in group.students:
                if best_student is None or student > best_student:
                    best_student = student
                    best_group = group

        return best_group

    def __str__(self) -> str:
        """String representation of the group"""
        return f"Group: {self.name}, Student: {', '.join(str(student) for student in self.students)}"


student1 = Student("Peter", 20)
student2 = Student("George", 21)
student3 = Student("Anna", 19)
student4 = Student("Katy", 22)
student5 = Student("Ivan", 20)

student1.add_value(5)
student1.add_value(6)

student2.add_value(3)
student2.add_value(4)

student3.add_value(5)
student3.add_value(6)
student3.add_value(7)

student4.add_value(10)
student4.add_value(11)

student5.add_value(1)
student5.add_value(2)

students = [student1, student2, student3, student4, student5]
the_best_student = max(students)
print(f"Best student: {the_best_student}")

group1 = Group("best")
group2 = Group("worst")

group1.add_student(student1)
group1.add_student(student2)

group2.add_student(student3)
group2.add_student(student4)
group2.add_student(student5)

print(group1)
print(group2)

group2.del_student(student5)

print(f"After delete {group2}")

the_best_group = Group.group_best_student([group1, group2])
print(f"Best group: {the_best_group}")
