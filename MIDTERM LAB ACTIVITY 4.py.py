class Patient:
    def __init__(self, name, admission_date, disease, discharge_date, age):
        self.name = name
        self.admission_date = admission_date
        self.disease = disease
        self.discharge_date = discharge_date
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Admission:", self.admission_date)
        print("Disease:", self.disease)
        print("Discharge:", self.discharge_date)
        print()


class PediatricPatient(Patient):
    pass


class Professor:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Dean(Professor):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return "Status\nRank: Dean\nName: " + self.name + "\nDepartment: " + self.department + "\nSalary: " + str(self.salary)


class Executive(Dean):
    def __str__(self):
        return "Status\nRank: Executive\nName: " + self.name + "\nDepartment: " + self.department + "\nSalary: " + str(self.salary)


def run_bank():
    print("Welcome!")

    while True:
        text = input("Enter your balance: ")
        try:
            balance = float(text)
            if balance >= 0:
                break
        except ValueError:
            pass
        print("Invalid")

    while True:
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Exit")
        option = input("Enter option (1-3): ")

        if option == "1":
            while True:
                text = input("Amount to withdraw: ")
                try:
                    amount = float(text)
                    if amount < 0:
                        print("Invalid")
                    elif amount > balance:
                        print("Insufficient funds.")
                        break
                    else:
                        balance = balance - amount
                        print("Your new balance is:", balance)
                        break
                except ValueError:
                    print("Invalid")

        elif option == "2":
            while True:
                text = input("Amount to deposit: ")
                try:
                    amount = float(text)
                    if amount < 0:
                        print("Invalid")
                    else:
                        balance = balance + amount
                        print("Your new balance is:", balance)
                        break
                except ValueError:
                    print("Invalid")

        elif option == "3":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid")


def run_hospital():
    patients = []

    while True:
        print("1. Insert new patient")
        print("2. Display all patients")
        print("3. Display pediatric patients")
        print("4. Exit")
        option = input("Enter option (1-4): ")

        if option == "1":
            name = input("Name of the patient: ")
            admission_date = input("Date of admission: ")
            disease = input("Disease: ")
            discharge_date = input("Date of discharge: ")

            while True:
                text = input("Age of the patient: ")
                try:
                    age = int(text)
                    if age >= 0:
                        break
                except ValueError:
                    pass
                print("Invalid")

            if age < 12:
                patient = PediatricPatient(name, admission_date, disease, discharge_date, age)
            else:
                patient = Patient(name, admission_date, disease, discharge_date, age)
            patients.append(patient)

        elif option == "2":
            for patient in patients:
                patient.display()

        elif option == "3":
            for patient in patients:
                if patient.age < 12:
                    patient.display()

        elif option == "4":
            break

        else:
            print("Invalid")


def run_professor():
    dean = Dean("John Cena", 32000, "English")
    executive = Executive("Ronald McDonald", 42000, "Computer Science")
    print(dean)
    print(executive)


while True:
    choice = input("Select program (1 Bank, 2 Hospital, 3 Professor, q to quit): ")
    if choice == "q":
        break
    elif choice == "1":
        run_bank()
    elif choice == "2":
        run_hospital()
    elif choice == "3":
        run_professor()
    else:
        print("Invalid")