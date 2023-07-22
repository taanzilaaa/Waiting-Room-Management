class Patient:
    def __init__(self, id, name, age, blood):
        self.id = id
        self.name = name
        self.age = age
        self.blood = blood
        self.n = None
        self.prev = None

class WRM:
    def __init__(self):
        self.head = None

    def register_patient(self, id, name, age, blood):
        new= Patient(id, name, age, blood)

        if self.head is None:
            self.head = new
            new.n = new
            new.prev = new
        else:
            last = self.head.prev
            last.n = new
            new.prev = last
            new.n = self.head
            self.head.prev = new

    def serve_patient(self):
        if self.head is None:
            print("No patients in the waiting room.")
            return

        served = self.head
        if self.head.n == self.head:  # Only one patient in the waiting room
            self.head = None
        else:
            self.head = self.head.n
            self.head.prev = served.prev
            served.prev.n = self.head

        print(f"Serving patient: {served.name}")

    def cancel_all(self):
        if self.head is None:
            print("No appointments to cancel.")
            return

        self.head = None
        print("All appointments canceled. Doctor can go to lunch.")

    def can_doctor_go_home(self):
        if self.head is None:
            print("Yes, doctor can go home.")
        else:
            print("No, there are patients waiting.")

    def show_all_patients(self):
        if self.head is None:
            print("No patients in the waiting room.")
            return

        current= self.head
        while True:
            print(f"Patient ID: {current.id}")
            current = current.n
            if current == self.head:
                break
wrm = WRM()

while True:
    print("\nMenu:")
    print("1. Add Patient")
    print("2. Serve Patient")
    print("3. Show All Patients")
    print("4. Can Doctor Go Home?")
    print("5. Cancel All Appointments")
    print("6. Exit")
    c= int(input("Enter your choice: "))

    if c == 1:
        id = int(input("Enter patient ID: "))
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        blood= input("Enter patient blood group: ")
        wrm.register_patient(id, name, age, blood)
        print("Patient added successfully.")
    elif c == 2:
        wrm.serve_patient()
    elif c == 3:
        wrm.show_all_patients()
    elif c == 4:
        wrm.can_doctor_go_home()
    elif c == 5:
        wrm.cancel_all()
    elif c == 6:
        break
    else:
        print("Invalid choice. Please try again.")

print("Program exited.")
