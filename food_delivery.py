class FoodItem:
    def __init__(self,name,price):
        self.__name = name 
        self.__price = price 

    def get_name(self):
        return self.__name 

    def get_price(self):
        return self.__price 

    def get_final_price(self):
        if self.__price >1000:
            return self.__price*.9
        else:
            return self.__price 
        
class Pizza(FoodItem):
    def __init__(self,name,price,size):
        super().__init__(name,price)
        self.size = size 

    def show_detail(self):
        print(f"Pizza: {self.get_name()}, size:{self.size}, Final price:{self.get_final_price()}")

class Burger(FoodItem):
    def __init__(self,name,price,is_cheese):
        super().__init__(name,price)
        self.is_cheese = is_cheese

    def show_detail(self):
        if self.is_cheese: 
            print(f"Burger: {self.get_name()}, Cheese:{self.is_cheese}, Final price:{self.get_final_price()}")
        else:
            print(f"Burger: {self.get_name()}, Final price:{self.get_final_price()}")

pizza = Pizza("Pepperoni",1080,"Large")
burger = Burger("Chicken Burger",350,False)

pizza.show_detail()
burger.show_detail()



            



        
        
