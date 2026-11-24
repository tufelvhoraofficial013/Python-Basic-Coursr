# Logical Operators — and, or, not

"""

and	Both conditions must be true	                            age >= 18 and has_ticket == True

or	At least one condition must be true	is_student == True      or is_senior == True

not	Flips True to False and False to True	                   not is_raining

"""

 #AND OPERATOR 
 #Both condition needed to be true 

age = int(input("How old are you : ")) #asking age 
has_ticket = input("Do you have ticket ?  yes or no :") #asking if user has ticket 

if age >=18 and has_ticket =="yes" : #verifying both ticket and age 
    print("Welcome you can watch this A-rated movie ") #if both verified successfully
else: 
    print("Sorry you can not enter ") #if one of them not match 




#OR OPERATOR 
#one of the condition is need to be true 
 
is_student = input("Are you a student ? yes or no  : " ) #verifying if student
is_elder = input("Are you a senior citizen ? yes or no  :") #verifying is senior citizen
 
if is_student == "yes" or is_elder == "yes" : 
    print("You get a 20% Discount !!") #if student of senior citizen 

else:
    print("No discount applied ") #if non of them are true 

# not operator

#not simply flips True to False and False to True:

is_raining = False

if not is_raining :
    print("Great day for walk ")

else :
    print("Better stay inside !! ")

# Combining and + or together

age = int(input("How old are you ?  "))
has_ticket2 = input("Do you have Ticket ?  yes or no :  ")
is_vip = input ("Are you VIP ?  yes or no  : ")

if age >= 18  and has_ticket2  == "yes"  or is_vip == "yes" :
    print("Welcome")

else :
    print("Sorryyy")



#Truth table 
"""
This is how and and or work with True and False:

A	      B	    A and B	  A or B
True	True	 True	   True
True	False	 False	   True
False	True	 False	   True
False	False	 False	   False

and — BOTH must be True
or — at least ONE must be True 😊
"""






