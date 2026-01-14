from abc import ABC, abstractmethod
class Patient(ABC):
    def __init__(self,name,days_admitted,doctor_fee):
        self.__name = name
        self.__days_admitted = days_admitted
        self.__doctor_fee = doctor_fee

    def get_name(self):
        return self.__name 
    
    def get_days_admitted(self):
        return self.__days_admitted
    
    def get_doctor_fee(self):
        return self.__doctor_fee
    
    @abstractmethod 
    def calculate_base_bill(self):
        pass 
 
    @abstractmethod
    def calculate_tax(self,amount):
        pass

    def calculate_total_bill(self):
        base_bill = self.calculate_base_bill()
        tax = self.calculate_tax(base_bill)
        return base_bill + tax + self.get_doctor_fee()
    
class GeneralPatient(Patient):

    def calculate_base_bill(self):
        return 1000* self.get_days_admitted()
 
    def calculate_tax(self,amount):
        return amount*0.05
    
class ICUPatient(Patient):
    def calculate_base_bill(self):
        if self.get_days_admitted() > 5:
            return (3000* self.get_days_admitted())+5000
        else: 
            return 3000*self.get_days_admitted()
    
    def calculate_tax(self,amount):
        return amount*0.10

patient_info = []    
while True:
    print("\n1. add general patient")
    print("2. add ICU patient")
    print("3. show all bills")
    print("4. Exit platform")

    choice = input("\nenter your choice: ")
    if choice == "1":
        patient_name = input("enter patient name: ")
        days_admitted = int(input("enter total days admitted: "))
        doctor_fee = int(input("enter doctor fee: "))

        obj = GeneralPatient(patient_name,days_admitted,doctor_fee)
        patient_info.append(obj)
        print("General patient added")

    elif choice == "2":
        patient_name = input("enter patient name: ")
        days_admitted = int(input("enter total days admitted: "))
        doctor_fee = int(input("enter doctor fee: "))

        obj = ICUPatient(patient_name,days_admitted,doctor_fee)
        patient_info.append(obj)
        print("ICU patient added")

    elif choice == "3":
        for patient in patient_info:
            print(f"Patient Name: {patient.get_name()} | Total Bill: {patient.calculate_total_bill()}")

    elif choice == "4":
        print("Exit from the platform")
        break

    else:
        print("Invalid Input")


    






