num1 = 42 #- variable declaration - Numbers
num2 = 2.3 #- variable declaration - Numbers
boolean = True #- variable declaration - Boolean
string = 'Hello World' #- variable declaration - Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #- variable declaration - Strings - List initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #- variable declaration - Boolean - Numbers - Strings - Dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #- variable declaration - Strings - Tuples initialize
print(type(fruit)) #- log statement - type check
print(pizza_toppings[1]) #- log statement - list access value
pizza_toppings.append('Mushrooms') #- list add value
print(person['name']) #- log statement -Dictionary access value
person['name'] = 'George' # -Dictionary change value
person['eye_color'] = 'blue' # -Dictionary add value
print(fruit[2]) #- log statement -Tuples access value

if num1 > 45: #conditional IF
    print("It's greater") #- log statement
else: #-conditional ELSE
    print("It's lower") #- log statement

if len(string) < 5: #- length check #conditional IF
    print("It's a short word!") #- log statement
elif len(string) > 15: #- length check -conditional ELSEIF
    print("It's a long word!") #- log statement
else: #-conditional ELSE
    print("Just right!") #- log statement

for x in range(5): # - forloop start(0), stop at index 4, increment by 1, break at 5
    print(x) #- log statement
for x in range(2,5): # - forloop start(2), stop at index 4, increment by 1, break at 5
    print(x) #- log statement
for x in range(2,10,3): # forloop start(2), until (9), increment by 3
    print(x) #- log statement
x = 0
while(x < 5): #- while loop start - while loop stop 
    print(x) #- log statement
    x += 1 #- while loop increment 

pizza_toppings.pop() # - list delete value
pizza_toppings.pop(1) # - list delete value

print(person) #- log statement
person.pop('eye_color') # -Dictionary delete value
print(person) #- log statement

for topping in pizza_toppings:
    if topping == 'Pepperoni': #- Boolean #conditional IF
        continue
    print('After 1st if statement') #- log statement
    if topping == 'Olives': #- Boolean #conditional IF
        break # return

def print_hello_ten_times(): # -Function
    for num in range(10): # -for loop 
        print('Hello') #- log statement

print_hello_ten_times()

def print_hello_x_times(x): #function parameter x argument 4
    for num in range(x):
        print('Hello') #- log statement

print_hello_x_times(4) 

def print_hello_x_or_ten_times(x = 10): # function parameter x = 10, 
    for num in range(x):
        print('Hello') #- log statement

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)



"""
Bonus section #- Comment multiline
"""

print(num3) #- log statement
num3 = 72 #- variable declaration - Numbers
fruit[0] = 'cranberry' # - tuples change value
print(person['favorite_team']) # Dictionary Access value
print(pizza_toppings[7]) #- log statement list access value
print(boolean) #- log statement
fruit.append('raspberry') # - tuples add value
fruit.pop(1) # - tuples delete value