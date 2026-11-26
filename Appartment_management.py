
class Resident:
    def __init__(self, name, flat_no, maintenance_fee, status):
        self.name = name
        self.flat_no = flat_no
        self.maintenance_fee = maintenance_fee
        self.status = status

    def display_details(self):
        print("Resident Name:", self.name)
        print("Flat Number:", self.flat_no)
        print("Maintenance Fee:", self.maintenance_fee)
        print("Payment Status:", self.status)
        print("--------------------------")


class Society:
    def __init__(self):
        self.residents = []

    def add_resident(self):
        name = input("Enter Resident Name: ")
        flat_no = input("Enter Flat Number: ")
        fee = float(input("Enter Maintenance Fee: "))

        status = input("Enter Payment Status (Paid/Pending): ")

        resident = Resident(name, flat_no, fee, status)
        self.residents.append(resident)

        print("Resident Record Added Successfully!")

    def display_all(self):
        print("\n--- Apartment Maintenance Details ---")

        if len(self.residents) == 0:
            print("No resident records found.")
        else:
            for resident in self.residents:
                resident.display_details()


# Main Program
society = Society()

while True:
    print("\n1. Add Resident")
    print("2. Display All Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        society.add_resident()

    elif choice == "2":
        society.display_all()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
