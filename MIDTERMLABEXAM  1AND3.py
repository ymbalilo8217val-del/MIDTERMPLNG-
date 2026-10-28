class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


    def __str__(self):
        return (
            f"Book: {self.title} | Author: {self.author}\n"
            f"Price: PHP {self.price:.2f}"
        )




class Ebook(Book):
    def __init__(self, title, author, price, file_size_mb):
        super().__init__(title, author, price)
        self.file_size_mb = file_size_mb


    def __str__(self):
        return (
            f"EBook: {self.title} | Author: {self.author}\n"
            f"Price: PHP {self.price:.2f} | "
            f"File size: {self.file_size_mb} MB"
        )




book1 = Book("Python Basics", "Maria Santos", 450.00)
ebook1 = Ebook("Learning OOP", "Ana Cruz", 300.00, 5)
ebook2 = Ebook("Data Science", "Juan Dela Cruz", 550.00, 10)


print(book1)
print()
print(ebook1)
print()
print(ebook1)
class Student:
    def __init__(self, name, student_id, tuition_fee):
        self.name = name
        self.student_id = student_id
        self.tuition_fee = tuition_fee


    def __str__(self):
        return (f"Name: {self.name} | Student ID: {self.student_id}\n"
                f"Tuition fee: PHP {self.tuition_fee:.2f}")




class ScholarStudent(Student):
    def __init__(self, name, student_id, tuition_fee, scholarship_percentage):
        super().__init__(name, student_id, tuition_fee)
        if not (0 <= scholarship_percentage <= 100):
            raise ValueError("Scholarship percentage must be between 0 and 100.")
        self.scholarship_percentage = scholarship_percentage


    def calculate_payable_fee(self):
        return self.tuition_fee - (self.tuition_fee * self.scholarship_percentage / 100)


    def __str__(self):
        payable_fee = self.calculate_payable_fee()
        return (f"{super().__str__()}\n"
                f"Scholarship: {self.scholarship_percentage}%\n"
                f"Payable fee: PHP {payable_fee:.2f}")




student1 = ScholarStudent("Carlo Reyes", "2026-001", 40000.00, 50)
student2 = ScholarStudent("Jane Doe", "2026-002", 50000.00, 20)


print(student1)
print()
print(student2)