import math

#1. Declare your age as integer variable
age = 25
#2. Declare your height as a float variable
height = 1.75
#3. Declare a complex number variable
polar = (4 + 5j)
#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

def areaTriangle():
   base = float(input('Ingrese la base del triangulo: '))
   altura = float(input('Ingrese la altura del triangulo: '))
   result = 'El area del triangulo es: {}'.format(0.5*base*altura)
   print( result )
#areaTriangle()
#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

def perimeterTriangle():
   a = float(input('Ingrese lado A del triangulo: '))
   b = float(input('Ingrese lado B del triangulo: '))
   c = float(input('Ingrese lado C del triangulo: '))
   print( 'El perimetro del triangulo es: {}', a+b+c )
#perimeterTriangle()
#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
def rectangle():
   base = float(input('Ingrese la base del rectangulo: '))
   altura = float(input('Ingrese la altura del rectangulo: '))
   result = 'El area del rectangulo es: {}'.format(base*altura)
   result = 'El perimetro del rectangulo es: {}'.format((base*2) + (altura*2))
   print( result )
#rectangle()
#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
def circle():
   radio = float(input('Ingrese el radio del circulo'))
   pi = 3.14
   area = 'El area del circulo es: {}'.format(pi*(radio**2))
   perimeter = 'El perimetro del circulo es: {}'.format(2*radio*pi)
   print(area)
   print(perimeter)
#circle()
#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
formula = 'y = 2x -2'

def lineEquation(y, m, b):
   y = b
   x = -b/m
   m =m
   return [m, x , y]
result = lineEquation(0, 2, -2)
print('La pendiente de {} es'.format(formula, result[0]))
print('La interseccion en X de {} es'.format(formula, result[1]))
print('La interseccion en Y de {} es'.format(formula, result[2]))
#9. Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6,10)
def pendiente(p1, p2):
   x1, y1 = p1
   x2, y2 = p2
   num = y2-y1
   den = x2-x1
   return num/den
printText = 'La pendiente de los puntos {} y {} es: {}'.format('(2, 2)', '(6,10)', pendiente((2, 2),(6,10)))
print(printText)

#10. Compare the slopes in tasks 8 and 9.
print(pendiente((2, 2),(6,10)) == lineEquation(0, 2, -2)[0])
#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
def secondOrderEq(a, b, c):
   det = (b**2 - (4*a*c))
   if det < 0:
      return 0
   x1 = (-b + math.sqrt(det))/(2*a)
   x2 = (-b - math.sqrt(det))/(2*a)
   print(det)
   return [x1, x2]
solution = secondOrderEq(1, 8, 12)
print('La solucion de {} es:'.format('y = x^2 + 6x + 9'))
print('x1 =', solution[0])
print('x2 =', solution[1])
#12. Find the length of 'python' and 'jargon' and make a falsy comparison statement.
print((len('python') == len('jargon'))==False)
#13. Use _and_ operator to check if 'on' is found in both 'python' and 'jargon'
print('on' in 'python' and 'on' in 'jargon')
#14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')
#15. There is no 'on' in both dragon and python

#16. Find the length of the text _python_ and convert the value to float and convert it to string

_str = str(float(len('python')))
print('el largo de ' + _str + ' es', len(_str))

#17. Even numbers are divisible by 2 and the remainder is zero. How do 3#you check if a number is even or not using python?
numero = int(input('Introduce un numero'))
print('El numero es impar:', numero%2 == 1)
#18. The floor division of 7 by 3 is equal to the int converted value of#2.7.
print('La division flotante de 7 y 3 es igual al valor entero de 2.7: ', 7//3 == int(2.7))
#19. Check if type of '10' is equal to 10
print('\'10\'es igual a 10',type('10')==type(10))
#20. Check if int('9.8') is equal to 10
print('El entero de 9.8 es igual a 10:',int(9.8) == 10)
#21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
no_horas = int(input('Introduzca la cantidad de horas'))
paga_por_hora = int(input('Introduzca la paga por hora'))

print(no_horas * paga_por_hora)
#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume someone lives up to hundred years
anios = int(input('Cuantos años has vivido'))

print('Has vivido: ', anios*12*30*24*3600, 'segundos')

#23. Write a python script that displays the following table

print('''      
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
      '''
)