# STRING FORMATING (F-STRING and (,))

"""
by using f string you can print different type of data type into one print command 
"""
#this is how we print both st and int but we need different print command 
print("tufel vhora")
print(19)

name= "tufel vhora"
age = 19

print(f"my name is {name} and i am {age} years old") # suing f string and {} you can print different data types

print("my name is ", name, " and i am ", age, "years old ") #we can  also use , to do this whcih will require more "" to add multiple strings


#we can do math as well using f string inside print 

name1  = "tufel vhora"
born_year = 2007

print(f"my name is{name1} i was born in {born_year} and i am {2026 - born_year} years old ")

age1 = 19

print(f"my age is {age1} , i will be {age1 +3 } years old three years")

print(f"{name1.upper()} , was born in {born_year}")
print()
print()

#LESSON 7 EXERCISE


"""
Asks the user for their name using input()
Asks the user for their birth year using input() — convert to integer!
Asks the user for their favourite programming language using input()
Then prints this exact sentence using an f-string:
"""


#LESSON 7 SOLUTION
print()
user_name = input("What is your name  ?  ")
u_birth_year = int(input("What is your birth year ?  "))
fav_language = input("What is your favorite programming language ?   ")
current_year = 2026 
user_age = u_birth_year - current_year
print()
print(f"Helooo , my name is {user_name.upper()} , i am {user_age} years old and my favourite programming language is {fav_language.upper()} . ")
print()


