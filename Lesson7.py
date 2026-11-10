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

