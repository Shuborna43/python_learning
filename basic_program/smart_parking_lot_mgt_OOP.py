from abc import ABC, abstractmethod
class VehicleTicket(ABC):
    def __init__(self,plate_number,hours_parked,has_membership,entry_peak):
        self.__plate_number = plate_number
        self.__hours_parked = hours_parked
        self.__has_membership = has_membership 
        self.__entry_peak = entry_peak 

    def get_plate_number(self):
        return self.__plate_number 
    
    def get_hours_parked(self):
        return self.__hours_parked
    
    def get_has_membership(self):
        return self.__has_membership
    
    def get_entry_peak(self):
        return self.__entry_peak 
    
    @abstractmethod
    def calculate_base_fee(self):
        pass

    @abstractmethod
    def calculate_surcharge(self,amount):
        pass

    @abstractmethod
    def calculate_discount(self,amount):
        pass 

    def calculate_total_fee(self):
        base_fee = self.calculate_base_fee()
        surcharge = self.calculate_surcharge(base_fee)
        sub_total = base_fee + surcharge
        discount = self.calculate_discount(sub_total)
        total_bill = sub_total - discount 

        return max(0,int(total_bill))
    
class CarTicket(VehicleTicket):
    
    def calculate_base_fee(self):
        base = self.get_hours_parked()*50  
        return min(600,base)
        
    def calculate_surcharge(self,amount):
        if self.get_entry_peak():
            return amount*0.2
        else:
            return 0 
    
    def calculate_discount(self,amount):
        if self.get_has_membership():
            return amount*0.1
        else:
            return 0 

class BikeTicket(VehicleTicket):
    
    def calculate_base_fee(self):
        base = self.get_hours_parked()*30  
        return min(300,base)
       
    def calculate_surcharge(self,amount):
        if self.get_entry_peak():
            return amount*0.10
        else:
            return 0
         
    def calculate_discount(self,amount):
        if self.get_has_membership():
            return 40
        else:
            return 0 
        
class TruckTicket(VehicleTicket):
    def calculate_base_fee(self):
        base = self.get_hours_parked()*100 
        if self.get_hours_parked()>8:
            base += 250
        return min(1200,base)
       
    def calculate_surcharge(self,amount):
        if self.get_entry_peak():
            return amount*0.25
        else:
            return 0
         
    def calculate_discount(self,amount):
        if self.get_has_membership():
            return amount*0.05
        else:
            return 0 
        
def to_bool(user_input): 
    user_input = user_input.strip().lower()
    if user_input == "y" or user_input == "Y" or user_input == "yes" or user_input == "1" or user_input == "true":
        return True 
    else:
        return False 

def main():
    tickets = []    
    number_of_tickets = int(input("enter the number of tickets: ")) 

    for ticket in range(number_of_tickets):
        print(f"\nTicket {ticket+1}:")
        vehicle_type = input("enter vehicle type: car/ bike / truck: ").strip().lower()
        plate_number = input("enter plate number").strip().lower()
        hours_parked = int(input("enter hours parked"))
        membership = to_bool(input("Do you have membership (Yes/No)? : "))
        peak_hour  = to_bool(input("Is this peak_hour (Yes/No): ?"))

        if vehicle_type == "car":
            ticket = CarTicket(plate_number, hours_parked, membership, peak_hour)

        elif vehicle_type == "bike":
            ticket = BikeTicket(plate_number, hours_parked, membership, peak_hour)

        elif vehicle_type == "truck":
            ticket = TruckTicket(plate_number, hours_parked, membership, peak_hour)

        else: 
            print("Invalid Entry, Please Try Again")

        tickets.append(ticket)
        print("\n ___________Bill Summary_________")

        for t in tickets:
            total = t.calculate_total_fee()

            if isinstance(t,CarTicket):
                v_name = "Car" 

            if isinstance(t,BikeTicket):
                v_name = "Bike"

            if isinstance(t,TruckTicket):
                v_name = "Truck" 

            print(f"Plate: {t.get_plate_number()} |, Type: {v_name} | Total Fee: {total}")

if __name__ == "__main__":
    main()


    







      

        
        




