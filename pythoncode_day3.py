


# conditional statnment 
# if statement and elif 


# Program for BMI Calculator ahaving conditions based on diff age 
print (input ('what is your name'))
hieght = float (input(" enter your hieght  "))
wieght = int ( input ("enter your wieght "))
BMI = wieght/hieght **2
if BMI < 18.5 :
    print ("you are under wight ")
    
elif BMI >= 18.5 and BMI < 25:
    print (f"you are normal wieght {BMI}")
elif BMI < 30:
    print (" you are slightly overwieght ")
elif BMI < 35 :
    print ("you are overwieght ")
else:
    print ('your are clinically obese ')



# program for checking either the year is leap or not 
# year = int (input (" enter year number"))
# if year % 4 == 0:
#     print (f" this year {year} is leap year ")
#     if year % 100 == 0:
#         print (f" this year {year} is not a leap year")
#         if year % 400 ==0:
#             print (f"this year {year} is a leap year")
#         else :
#             print (f" this year {year} is not a leap year")
#     else :
#         print ("this is leap year ")
# else :
#     print (f" this  year {year} is not a leap year ")





2nd way of doing this 
year = int (input (" enter year number"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print (f"this year {year} is a leap year")
        else :
            print (f" this year {year} is not a leap year")
    else :
        print ("this is leap year ")
else :
    print (f" this  year {year} is not a leap year ")




# conditional statnment 
# if statement and elif 


# Program for BMI Calculator ahaving conditions based on diff age 
print (input ('what is your name'))
hieght = float (input(" enter your hieght  "))
wieght = int ( input ("enter your wieght "))
BMI = wieght/hieght **2
if BMI < 18.5 :
    print ("you are under wight ")
    
elif BMI >= 18.5 and BMI < 25:
    print (f"you are normal wieght {BMI}")
elif BMI < 30:
    print (" you are slightly overwieght ")
elif BMI < 35 :
    print ("you are overwieght ")
else:
    print ('your are clinically obese ')



# program for checking either the year is leap or not 
# year = int (input (" enter year number"))
# if year % 4 == 0:
#     print (f" this year {year} is leap year ")
#     if year % 100 == 0:
#         print (f" this year {year} is not a leap year")
#         if year % 400 ==0:
#             print (f"this year {year} is a leap year")
#         else :
#             print (f" this year {year} is not a leap year")
#     else :
#         print ("this is leap year ")
# else :
#     print (f" this  year {year} is not a leap year ")





2nd way of doing this 
year = int (input (" enter year number"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print (f"this year {year} is a leap year")
        else :
            print (f" this year {year} is not a leap year")
    else :
        print ("this is leap year ")
else :
    print (f" this  year {year} is not a leap year ")

