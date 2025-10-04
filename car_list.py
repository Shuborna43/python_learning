
car_list = ["Honda", 5, 6, "Wadi Saad", "Toyota", "+8801847301737", "+8801715158686", 7, "Adyan Rai", "15-1818-20"]

def car_description(car_list):
    for item in car_list: 
        if type(item) == int:
            seat = car_seat(item)
        elif ord(item(0)) == 43:
            cell = car_cell_num(item)
        elif 48 <= ord(item(0))<=57:
        #elife ord(item(0)) >= 48 and ord(item(0)) <=57:
            number = car_number(item)
        else:
            string = car_string(item)
         

def car_seat(seat,item, seat_list):
    if seat = car_seat(item): 
        seat_list.append(seat)
        return seat_list 

def car_cell_num(cell,item,cell_list):
    if cell = car_cell_num(item):
        cell_list.append(cell)
        return cell_list 

def car_number(number,item,car_number_list):
    if number = car_number(item)
        car_number_list.append(number)
        return car_number_list

def car_string (item, driver_list):
    flag = False
    for i in range (0, len(item),1):
        if ord(item(i)) == 32:
            flag = True
            name = car_driver(item)
            break
        else: continue 
    if flag == False:
        brand = car_brand(item)
    else:
        comtinue 

def car_driver(name,item,driver_list):
    if name = car_driver(item)
        driver_list.append(name)
        return driver_list

def car_brand(brand,item,brand_list):
    if brand = car_brand(item)
        brand_list.append(brand)
        return brand_list
    


def main():
    
    car_description(car_list)  
    seat_list = []
    driver_list = []
    brand_list = []
    cell_list = []
    car_number_list = []

    car_seat(seat,item, seat_list)
    car_cell_num(cell,item,cell_list)
    car_number(number,item,car_number_list)
    car_driver(name,item,driver_list)
    car_brand(brand,item,brand_list)

    print(seat_list)

main()

    
