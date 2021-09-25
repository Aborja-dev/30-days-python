import math

print('\nDia 2 de programacion en python\n')

print('\nEjercicio 1\n')
#Declare a first name variable and assign a value to it
firstName = 'Rick'
#Declare a last name variable and assign a value to it
lastName = 'Sanchez'
#Declare a full name variable and assign a value to it
fullName = 'Beth Sanchez'
#Declare a country variable and assign a value to it
country = 'Mexico'
#Declare a city variable and assign a value to it
city = 'Montreal'
#Declare an age variable and assign a value to it
age = 25
#Declare a year variable and assign a value to it
year = 2021
#Declare a variable is_married and assign a value to it
isMarried = False
#Declare a variable is_true and assign a value to it
isTrue = False
#Declare a variable is_light_on and assign a value to it
isLightOn = True
#Declare multiple variable on one line
uno,dos,tres,cuatro = ['Estas','Son','Muchas','Variables']
print('\nEjercicio 2\n')
#Check the data type of all your variables using type() built-in function
print(firstName,type(firstName))
print(lastName,type(lastName))
print(fullName,type(fullName))
print(country,type(country))
print(city,type(city))
print(age,type(age))
print(year,type(year))
print(isMarried,type(isMarried))
print(isTrue,type(isTrue))
print(isLightOn,type(isLightOn))
print(uno,dos,tres,cuatro,type(uno),type(dos),type(tres),type(cuatro))
#Using the len() built-in function, find the length of your first name
print(len(firstName))
#Compare the length of your first name and your last name
print(len(firstName) == len(lastName))


#Declare 5 as num_one and 4 as num_two
numOne = 5
numTwo = 4
#Add num_one and num_two and assign the value to a variable total
total = numOne + numTwo
#Subtract num_two from num_one and assign the value to a variable diff
diff = numOne - numTwo
#Multiply num_two and num_one and assign the value to a variable product
product = numOne * numTwo
#Divide num_one by num_two and assign the value to a variable division
division = numOne / numTwo
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = numOne % numTwo
#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = numOne**numTwo
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floorDiv = numOne//numTwo
#The radius of a circle is 30 meters.
radio = 30
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
areaCircle = (math.pi) * (radio**2)
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
perimeter = 2*math.pi*radio
#Take radius as user input and calculate the area.
userRadio = input('Cual es el radio del circulo ')
print((math.pi) * (radio**2))
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
def storeData(data):
   print(data)
   user = {   
      'firstname': data['name'],
      'lastName': data['last'],
      'country': data['country'],
      'age': data['age'],
   }
   print(user)
storeData(data= {   
   'name': firstName,
   'last': lastName,
   'country': country,
   'age': age,
}
)
#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

