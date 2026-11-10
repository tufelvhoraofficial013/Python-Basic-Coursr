# INPUT FROM USER



input("What is your name : ") #it will ask user thier name 
print()
name = input("What is your  name ?  ") # using varaible will save the users input as varaible to further use 
print()
print(name) #now you can use stored name for printing as well
print()

#give welcome message

message = "WELCOME"
name1= input("Enter your name :  ") #asking name 
print(message)
print(name1)

#print inromation by askin user

name3 = input("Enter your name :  ") #asking name 
age = input("Enter your age  :") #using only input will alwyas give str even if user enter number  , can not use to calcualation sicne its only str not int
city = input("Enter your city : ") #asking city 
print() #empty line for cleaner look
#printing 
print(name3)
print(age)
print(city)


print(type(age)) # it will print str not int 


age1 = int(input("ENer your age : ")) #using int  before input will get user input as int user can not enter anything but number
print(age1)
print(type(age1))


#math using variable and user input 

birth_year1 = int(input("Enter your birth year : ")) #it will ask and save birth year as int which can bu use for math 
current_year1 = int(input("Enter current year :")) #it will ask and save current year as int which can bu use for math 
age2 = current_year1 - birth_year1
print(age2)

"""
USE:
log in to ask username and passwors
search engine to search
ATM asking  pin to withdraw
"""

#LESSON 5 EXERCISE :
"""
ask user for name 
ask user for birth year
calculate theri age by subtracting by current year 
print  name and age 
add comments
"""


#LESSON 5 SOLUTION

name5  = input("Enter your name :  ")
birth_year2 = int(input("Enter yout birth year : "))
current_year2 = 2026

age3= current_year2 - birth_year2
print(name5)
print(age3)
