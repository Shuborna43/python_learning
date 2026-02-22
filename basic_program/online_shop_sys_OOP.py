class Product:
    def __init__(self,name,price):
        self.__name = name 
        self.__price = price 

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price  
    
    def get_final_price(self):
        return self.__price 
    
class Electronics(Product):
    def __init__(self,name,price,warranty_years):
        super().__init__(name,price)
        self.warranty_years = warranty_years

    def get_final_price(self):
        return self.get_price()*1.15   

class Clothing(Product):
    def __init__(self,name,price,size):
        super().__init__(name,price) 
        self.size = size 

    def get_final_price(self):
       if self.get_price() > 2000:
           return self.get_price()*0.80
       else:
           return self.get_price()

product_list = []

while True:
    print("\n--Online Shopping System__")
    print("1. Add Electronics")
    print("2. Add Clothing")
    print("3. Show All Products")
    print("4. Exit")


    choice = input("enter your choice: ")
    if choice == "1":
        name = input("enter the name of electronics item: ")  
        price = float(input("enter the price of electronics item: "))
        warranty = int(input("enter years of warranty of electronics item: "))  

        obj = Electronics(name,price,warranty)  
        product_list.append(obj)
        print(f"Electronics {name} added")

    elif choice == "2":
        name = input("enter the name of clothing item: ")  
        price = float(input("enter the price of clothing item: "))
        size = input("enter size of clothing item: ")  

        obj = Clothing(name,price,size)  
        product_list.append(obj)
        print(f"Clothing {name} added")

    elif choice == "3":
        print("\n--- Product List ---")
        for item in product_list:
            if isinstance(item,Electronics):
                print(f"Electronics: {item.get_name()} | Final Price: {int(item.get_final_price())}") 
            elif isinstance(item,Clothing):
                print(f"Clothing: {item.get_name()} | Final Price: {int(item.get_final_price())}") 

    elif choice == "4":
        print("Exit") 
        break 

    else: 
        print("Invalid Choice")

    


    




