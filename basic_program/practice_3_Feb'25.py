#problem: Create a class FizzBuzz that prints numbers from 1 to a given limit. 
#For multiples of 3, print "Fizz", 
#for multiples of 5, print "Buzz"; 
#for multiples of both, print "FizzBuzz". 

#problem:1 Create a class FizzBuzz that prints numbers from 1 to a given limit.
#For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; for multiples of both, print "FizzBuzz"

# for i in range(0,a+1):
#   if i%2==0:
#     b+=i
# print (b)


class FizzBuzz:
  def __init__(self,number):
    self.number=number

  def Multiply (self):
    for i in range (1,self.number+1):
      if i%3==0 and i%5!=0:
        print (i, "is Fizz")

      elif i%5==0 and i%3!=0:
        print (i, "is Buzz")

      elif i%3==0 and i%5==0:
        print (i, "is FizzBuzz")

      else:
        print (i, "is not devided by 3 or 5")


F=FizzBuzz(8)
F.Multiply()

#problem2: Create a class Marks to calculate average marks for two or three subjects
class Marks:
  def average (self,*Points):
    R=0
    print (Points)
    for i in Points:
      R+=i
      A=R/len(Points)
    print ("total of marks is",R)
    print ("average mark is",A)

M=Marks()
M.average(50,30,20,60)

#problem3: Create a TimeGreeting class that greets based on diffrent times.

class TimeGreeting:
  def __init__(self,time):
    self.time=time

  def greetings(self):
    return (f"welcome to my class at: {self.time}")

    #Prova
    # return("======================================")
    # return (f"welcome to my class at: {self.time}")
    # return("======================================")





T1=TimeGreeting("5.00 pm")
print (T1.greetings())
T2=TimeGreeting("10.30 am")
print (T2.greetings())
T3=TimeGreeting("7.20 pm")
print (T3.greetings())


#problem4:Create a class that calculates payment for full-time and part-time employees based on work hours and hourly rates
class Calculator:
  def __init__(self, hour, rate, flat):
    self.hour=hour
    self.rate=rate
    self.flat=flat

  def salary(self):

   if self.hour<8:
    print (f"s/he is a part-time staff and salary is BDT {self.hour*self.rate}")
   elif self.hour==8:
    print (f"s/he is a full-time staff and salary is BDT {self.flat}")
   else:
    print (f"s/he is a full-time staff but s/he did overtime and salary is BDT {(self.flat+((self.hour-8)*self.rate))}")

C1=Calculator(5,50,1000)
C1.salary()
C2=Calculator(8,50,1000)
C2.salary()
C3=Calculator(10,50,1000)
C3.salary()


#Problem5: Create a class BankAccount that supports deposits through cash, cheque or online transfer.

class BankAccount:
  def __init__(self, name, cash,cheque,online,balance):
    self.name=name
    self.cash=cash
    self.cheque=cheque
    self.online=online
    self.balance=balance
    #self.deposit=deposit


  def TotalBalance(self):
    #self.deposit=self.cash+self.cheque+self.online
    TotalDeposit=self.cash+self.cheque+self.online
    self.balance+=TotalDeposit

    print (f"Account Name {self.name} has total balance of BDT {self.balance}")

  def Update(self,cash,cheque,online):
   self.cash=cash
   self.cheque=cheque
   self.online=online


#create object

B1=BankAccount("Farzana Khan", 100,80,60,1000)
B1.TotalBalance()
B1.Update (10,20,30)
B1.TotalBalance()

print ('---------------------------')

B2=BankAccount("Imran Ahmed",10,8,6,100)
B2.TotalBalance()
B2.Update (1,2,3)
B2.TotalBalance()

print ('---------------------------')

B3=BankAccount("Wadi Saad",1000,800,600,10000)
B3.TotalBalance()
B3.Update (100,200,300)
B3.TotalBalance()

#Problem6: Creat a Car class to calculate fuel efficiency for petrol and diesel cars

class Car:
  def __init__(self,type,fuel,distance,fuel_quantity):
    self.type=type
    self.fuel=fuel
    self.distance=distance
    self.fuel_quantity=fuel_quantity


  def FuelEfficiency (self):
    FuelEfficiency=self.distance/self.fuel_quantity
    if FuelEfficiency>7:
      print (f"{self.type} car is {self.fuel} driven and fuel efficiency is {int(FuelEfficiency)} km per liter. It is fuel efficient")
    else:
      print (f"{self.type} car is {self.fuel} driven and fuel efficiency is {int(FuelEfficiency)} km per liter. It is not fuel efficient")

C1=Car("Sedan-tarbo","petrol",40,8)
C1.FuelEfficiency()
C2=Car("Sedan-hybrid","octane",40,4)
C2.FuelEfficiency()
C3=Car("Truck","diesel",40,12)
C3.FuelEfficiency()


#problem7: Create a class ExamResult to calculate the result based on percentage or letter grade.

class ExamResult:
  def __init__(self, name, subject, number):
    self.name=name
    self.subject=subject
    self.number=number


  def grade(self):
    if self.number<30:
      print (f"Student name: {self.name} got {self.number} in {self.subject} and s/he got 'F' grade")
    elif self.number>=30 and self.number<50:
      print (f"Student name: {self.name} got {self.number} in {self.subject} and s/he got 'D' grade")
    elif self.number>=50 and self.number<60:
      print (f"Student name: {self.name} got {self.number} in {self.subject} and s/he got 'C' grade")
    elif self.number>=60 and self.number<70:
      print (f"Student name: {self.name} got {self.number} in {self.subject} and s/he got 'B' grade")
    else:
      print (f"Student name: {self.name} got {self.number} in {self.subject} and s/he got 'A' grade")

E1=ExamResult("Ryna", "Python", 89)
E1.grade()
E2=ExamResult("Shuborna", "Geography", 20)
E2.grade()
E3=ExamResult("Adeeba", "Bangla", 60)
E3.grade()








            



       
