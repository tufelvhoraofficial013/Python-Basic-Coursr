# IF ,ELIF AND ELSE STATEMENTS
"""
🟢 if the light is green — go
🟡 elif the light is yellow — slow down
🔴 else the light is red — stop
"""


"""
That is an if statement in real life. A condition is checked — and if it is true — something happen
"""

age = 19 #setting age number
if age>= 18 :  #checking if age is greater than 18 which means condidion match 
    print("You are an Adult ") #than it prints Adult 
    #the indentation under the line of if which teel that this code reun under this ondition


age2 = 15 
if age >= 18 :
    print("You are an Adult  ") #this will not run cuz age is lowee than 18 



#if with user input 

password = int(input(" Enter password : ")) # asking user for password

if password == 1234 : #checking password if true or not 
    print("Login success ") #if true then login success


u_age = int(input("How old are you ?   ")) #asking age fromm user

if u_age >= 18 : #setting condidtion 
    print("You are an Adult ") #if true user will recive following message 
    print("You can Vote") 
    print("You can Drive")


#if and Else 

age3 =int(input("How old are you ? ")) #asking age 


if age3 >= 18 : #first condition
    print("You are and Adult") #output if first condition is true
 
else : #else menas if no condition above match the input then else will apply
    print("You are not an Adult ") #output if esle will apply




#if,elif and else

age4 = int(input("How old are you ? "))

if age4 >= 18 : #checking first condtion
    print("You are an Adult  !!!  ")  #the output if first condtion is true
 
elif age4 >= 13 : #checking second condition (it only run when first condtion is not true)
    print("You are an teenager !!! ") #output if second condition is ture
 
else : #everthing else  
    print("You are an children !!! ") #output if else apply 




# Multiple elif

score = int(input("How much did you score ? [0-100]  ")) #asking score

if score >= 90 : #if score is >= 90
    print("Grade : A ") #then this is grade

elif score >= 80 : #if score is >= 80
    print("Grade : B ")  #then this is grade

elif score >= 70 :#if score is >= 70
    print("Grade : C ") #then this is grade

elif score >= 60 :#if score is >= 60
    print("Grade : D ") #then this is grade
else : #anything else 
    print("Grade : F ")  #then this is grade



#LESSON 8 EXERCISE
"""
Asks the user for the temperature in celsius using input()
If temperature is above 30 — "It is very hot outside!"
If temperature is above 20 — "It is warm outside!"
If temperature is above 10 — "It is a bit cold outside!"
Otherwise — "It is very cold outside!"
"""


#LESSON 8 SOLUTION

temp = int(input("What is the temprature in your city :  "))

if temp  >= 30 :
    print("It is very hot outside")

elif temp >= 20 :
    print("It is warm outside " )

elif temp >= 10 :
    print("It is a bit cold outside ")

else :
    print("It is very cold outside ")



