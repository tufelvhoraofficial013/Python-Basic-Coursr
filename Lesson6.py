# STRING METHODS
"""
my_string.method_name()
"""

name = "tufel vhora"
print(name.upper()) #.uuper() use to print output in uppercase

name1 = "TUFEL VHORA"
print(name1.lower()) # .lower() use to print in lowercase

name2 = " tufel vhora "
print(name2.strip())# .strip() is use to remove extra spaces from beginig and end of string 

line = "i love girl"
print(line.replace("girl" , "Princess")) #.replace("a" , "b") replcae a with b

name3 = "Tufel vhora" 
print(len(name3)) # counts the numer of charatcers in string including spaces

#mixng methods

"""
you can mix use methods as welll to complete two mathod in  one line 
"""

name4 = " Tufel Vhora  "
print(name4.strip().upper()) # first it will  remove extra speaces adn then make it in uppercase 



"""
#USE

log in syste use to lowercase your username and email
automaticly swap words though autocorrect using replace

"""


#LESSON 6 EXERCISE

"""
ask user for name 
print it in uppercase
print it in lowercase aswell
print the num of charcters in their name
"""



# LESSON 6 SOLUTION

name5 = input(" What is your name ?   ")
print(name5.upper())
print(name5.lower())
print(len(name5))

