def my_name(name):
    print(f'my name is {name}')
name = input('enter your name: ')
my_name(name)
def my_meal(food ,drink):
    print(f'i like eat {food} and while drinking {drink}')
drink = input('enter your favorite drink: ')
food = input('enter your favorite food: ')
my_meal(food ,drink)
def cube(number):
    return number**3

def by_three(number):
    if number %3 == 0:
      return cube(number)
    else :
        return False

print(by_three(3))