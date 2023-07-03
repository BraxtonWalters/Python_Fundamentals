num1 = 42  # init int var
num2 = 2.3  # init float var
boolean = True  # init boolen var
string = 'Hello World'  # init str var
pizza_toppings = ['Pepperoni', 'Sausage',
                  'Jalepenos', 'Cheese', 'Olives']  # init list var
person = {'name': 'John', 'location': 'Salt Lake',  # init dick
          'age': 37, 'is_balding': False}  # init
fruit = ('blueberry', 'strawberry', 'banana')  # init turple
print(type(fruit))  # printing the type of the var in the prens
print(pizza_toppings[1])  # printing the 2 index for the list of pizza_toppings
# we put the mush on the end on topping list
pizza_toppings.append('Mushrooms')
print(person['name'])  # printing the thing from the dick
person['name'] = 'George'  # changing the key thing that changes things
# we change the value the is linked with the key thing
person['eye_color'] = 'blue'
print(fruit[2])  # printing nanner

if num1 > 45:  # check da 1st thinf is more than da sec thingy
    print("It's greater")  # if dat was type dat stuf out
else:  # dis thing with this thing : make this mean false then do dat thing
    # dat thing from before wasn right we print low to the floor
    print("It's lower")

if len(string) < 5:  # check dat string is longer than dat 5
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2, 5):
    print(x)
for x in range(2, 10, 3):
    print(x)
x = 0
while (x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break


def print_hello_ten_times():
    for num in range(10):
        print('Hello')


print_hello_ten_times()


def print_hello_x_times(x):
    for num in range(x):
        print('Hello')


print_hello_x_times(4)


def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
