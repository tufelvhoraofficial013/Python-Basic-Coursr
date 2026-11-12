
# Equal to (==)

passwrod =  input("Enter password : ") #ask password input
print() #print blank 
if passwrod == "python123": # compare password  input to correct password
    print("Access Granted ") #if correct password then output

else : #for another password
    print("Wrong Password ") #if wrong password 

print()


# Not equal to (!=)

name= input("Enter your name : ") #asking user input 
print()

if name != "Tufel" : # checking if input is not eqaul (means anything but correct input will not be able to get access)
    print("Yu are not Tufel ! ") #output if input is not equal 

else: #only correct input will get access
    print("Hey  Tufel ! Welcome back ! ") #if enter correct input

print()


# Greater than and Less than


number = int(input("Enter number ")) #asking number input 

if number > 100 : #checking if number is greater than 100 
    print("This is a big number !") #if greater than 100 then this will be output

if number <0 : #checing if negative number
    print("This is a negative number ! ") # if input if negative number 

else:  #anything in between 
    print("This is a perfect number ") #for perfect number output 

print()



#Greater than or equal to (>=) and Less than or equal to (<=)


age = int(input("How old are you : ")) #asking user age as input 
print() #blank print
if age >= 18 : #checking if user is 18 or above 
    print("You can vote ! ") #if user is 18 or above 
if age <=12 : #checking if user is 12 or below
    print("You get a kids menu ") #if user is 12 or below 

print()


#Comparing strings

city = input("Enter your city :  ") #asking city name 

if city == "Sapporo" : #comapring with other
    print("Oh me to , Sapporo is amazing ") # if both are same 

else :
    print(f"Nice . may be i shoud plan my next trip to {city.upper()}") #if both are not same 


#Printing the result directly
#Remember — comparisons always return True or False. You can print that directly:

print(10>5) #if one is a is bigger than b
print(9==6) #if one is a is  equal to b
print(23<34) #if one is a is smaller than b
print(12!=12) #if one is a is not equal to  b




#LESSON 9 EXERCISE 
"""
Asks the user to enter a secret code using input()
If the code equals 311 print: verificatin success
if not print: wrong code 
"""

#LESSON 9 SOLUTION 

code = int(input("Enter the code ! "))

if code == 311 :
    print("Verificatin success")
else:
    print("Wrong code ")

    