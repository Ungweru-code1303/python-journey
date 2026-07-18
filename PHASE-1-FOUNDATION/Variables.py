x= 5
y= "John"
print(x)
print(y)

x = float(5)  
# casting is converting a value from one
#  data type to ano
print(type(x))  
# variable names are case senstive
a= "9" 
A = "Ungweru Munyenyembe"
print(a)
print(A)
print(type(a))
print(type(A))   
# TYPES OF VARIABLE NAMES
# Camel Case e.g myFirstVariable
#Pascal Case e.g MyFirstVariable
#Snake Case e.g My_first_variable

# Assigning a value to multiple variables
x=y=z= "Orange"
# Assigning multiple values to multiple variables in one line
a,b,c = "Orange", "Apple", "Tangerine"
print(x,y,z)  
print(a)
print(b)
print(c)  
# (outputting variables. using the print function, you can output multiple values of
#  different functions, by placing a comma between the variables in the print function )
name= "Ungweru"
surname = "Munyenyembe"
print(name, surname)
# you can also use the plus sign (+)

print(name+surname)
#global variables are variables that are outside the function and can be accessed from both outside the main function 
# within a specific function 
s="AMAZING"
def myfunc(feeling):
    
    print("Python is " + feeling)
myfunc("amazing")   
myfunc("terrible") 
# inorder to assign a multiline string to a variable, you use three quotes at the beginning of the 
#    multi-line string and at the end (""")   
a = """ Hello my name is Ungweru Munyenyembe and i am a software engineering student. I am super proud of myself  """
print(a)