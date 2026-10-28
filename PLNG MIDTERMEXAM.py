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