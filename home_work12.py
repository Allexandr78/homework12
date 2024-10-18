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
