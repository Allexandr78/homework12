"""Home work 12"""


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
