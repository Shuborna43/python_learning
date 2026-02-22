
def main():

   def get_square_numbers_between(first, last):
       square_numbers =[]
       number = 1
       while True:
             square_number = (number*number)
             if square_number > last:
                break 
        
             if square_number >= first:
                square_numbers.append(square_number) 
             number += 1
       return square_numbers
    

   print(get_square_numbers_between(2,64))


   def process_user_input():
       number_list = []
       while True:
            number = int(input("please enter a number:  "))
            if number == 0:
               break 
            number_list.append(number) 
 
 
       smallest_number = number_list[0]
       largest_number = number_list[0]
       total = 0

       for num in number_list:
          if num < smallest_number:
             smallest_number = num 
          if num > largest_number:
             largest_number = num 
          total += num 
       average = total/len(number_list) 

       print (f"number list is {number_list}, smallest number is {smallest_number}, largest number is {largest_number}, total number is {total} and average number is {average:.2f}")

   process_user_input()

main()


    






       
       


