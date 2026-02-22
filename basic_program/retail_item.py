# # Create a Python file named retail_item.py. In the retail_item.py file, implement the following requirements:
# # Define a main() function with the following structure:
# # def main():
# # 	pass
# # if __name__ == "__main__":
# # 	main()
# # Create the following functions with appropriate docstrings:
# # get_retail_item_description(): Prompts the user to enter the retail item description and returns it as a string.
# # get_number_of_purchased_items(): Prompts the user to enter the quantity of items sold and returns it as an integer.
# # get_price_usd_per_unit(): Prompts the user to enter the price per unit in American dollars and returns it as a float.
# # get_tax_rate(): Prompts the user to enter the tax rate as a decimal (e.g., 0.06 for 6%) and returns it as a float.
# # calculate_subtotal_usd(price, quantity_sold): Takes the price per unit (float) and quantity sold (int) as parameters, calculates the subtotal by multiplying them, and returns the result as a float.
# # calculate_tax_usd(subtotal, tax_rate): Takes the subtotal (float) and tax rate (float) as parameters, calculates the tax amount by multiplying them, and returns the result as a float.
# # calculate_total_usd(subtotal, tax): Takes the subtotal (float) and tax amount (float) as parameters, calculates the total by adding them, and returns the result as a float.
# # In the main() function, replace the pass statement with code that:
# # Calls the input functions to get the retail item description, quantity sold, price per unit, and tax rate from the user.
# # Calls the calculation functions to compute the subtotal, tax amount, and total.
# # Displays the results in the following format:

# # Retail Item Details:
# # Description: [description]
# # Quantity Sold: [quantity]
# # Price per Unit: $[price]
# # Subtotal: $[subtotal]
# # Tax Rate: [tax_rate]%
# # Tax Amount: $[tax]
# # Total: $[total]
# # Ensure that monetary values (price, subtotal, tax, and total) are displayed with two decimal places, and the tax rate is displayed as a percentage with one decimal place.

# def get_retail_item_description():
# 	item = input("enter the item you want: ")
# 	return item 

# def get_number_of_purchased_items():
# 	quantity = int(input ("enter the quantity you want: "))
# 	return quantity 

# def get_price_usd_per_unit():
# 	price_per_unit = float(input("enter the price per quantity of the item in USD: ")) 
# 	return price_per_unit

# def get_tax_rate():
# 	tax_rate = float(input("enter the tax rate: ")) 
# 	return tax_rate

# def calculate_subtotal_usd(price, quantity_sold):  
# 	calculate_subtotal = price * quantity_sold 
# 	return calculate_subtotal

# def calculate_tax_usd(subtotal, tax_rate):
# 	calculate_tax = subtotal * tax_rate 
# 	return calculate_tax

# def calculate_total_usd(subtotal, tax):
# 	total_usd = subtotal + tax 
# 	return total_usd 

# def main():
# 	description = get_retail_item_description()
# 	quantity_sold = get_number_of_purchased_items()
# 	price = get_price_usd_per_unit()
# 	tax_rate = get_tax_rate()
# 	subtotal = calculate_subtotal_usd(price, quantity_sold)  
# 	tax = calculate_tax_usd(subtotal, tax_rate)
# 	total = calculate_total_usd(subtotal,tax)	 
	
#     print("\nRetail Item Details:") 
#     print(f"Description: {description}")
#     print(f"Quantity Sold: {quantity_sold}")
#     print(f"Price per Unit: {price}")
#     print(f"Subtotal: ${subtotal}")
#     print(f"Tax Rate: {tax_rate}%")
#     print(f"Tax Amount: ${tax}")
#     print(f"Total: ${total}")

# if __name__ == "__main__":
# 	main()



def get_retail_item_description():
    item = input("enter the item you want: ")
    return item 

def get_number_of_purchased_items():
    quantity = int(input ("enter the quantity you want: "))
    return quantity 

def get_price_usd_per_unit():
    price_per_unit = float(input("enter the price per quantity of the item in USD: ")) 
    return price_per_unit

def get_tax_rate():
    tax_rate = float(input("enter the tax rate: ")) 
    return tax_rate

def calculate_subtotal_usd(price, quantity_sold):  
    calculate_subtotal = price * quantity_sold 
    return calculate_subtotal

def calculate_tax_usd(subtotal, tax_rate):
    calculate_tax = subtotal * tax_rate 
    return calculate_tax

def calculate_total_usd(subtotal, tax):
    total_usd = subtotal + tax 
    return total_usd

def main():
    description = get_retail_item_description()
    quantity_sold = get_number_of_purchased_items()
    price = get_price_usd_per_unit()
    tax_rate = get_tax_rate()
    subtotal = calculate_subtotal_usd(price, quantity_sold)  
    tax = calculate_tax_usd(subtotal, tax_rate)
    total = calculate_total_usd(subtotal,tax)    
    
    print("\nRetail Item Details:") 
    print(f"Description: {description}")
    print(f"Quantity Sold: {quantity_sold}")
    print(f"Price per Unit: {price:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax Rate: {tax_rate:.2f}%")
    print(f"Tax Amount: ${tax:.2f}")
    print(f"Total: ${total:.2f}")
      
if __name__ == "__main__":
    main()
