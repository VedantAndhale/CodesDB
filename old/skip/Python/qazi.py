# comments

# variables
# print('Rafeh Qazi')
# print('Rafeh Qazi')

# name = 'Clever Programmer'
# age = 25

# print(name)
# print(age)

# full_name = 'rafeh qazi'
# print(full_name)

# width, height = 400, 500
# print(width)
# print(height)

# your_name = input('Please enter your name: ')
# print('hi ' + your_name)

# num1 = input('enter a number: ')
# num2 = input('enter a number: ')
# print(int(num1) + int(num2))

# DATA TYPES
# strings
# int (1, 2, 3), float/decimal (0.2) (numbers)

# strings 'hello', "cookie" => "hellocookie"
# strings '10', "20" => "1020"

# math operators +, -, /, //, *, **, %

# # Tip Calculator App
# food_amount = float(input('Enter food amount $: '))
# tip_percentage = float(input('Enter your tip percentage %: ')) / 100
# tip_amount = food_amount * tip_percentage

# # total 👉 food_amount + tip_amount
# total = food_amount + tip_amount
# print('\n\n\n')
# print('--------------------------------')
# print(f'🥘 Food Amount: ${food_amount}')
# print(f'⚖️ Tip Amount: ${tip_amount}')
# print('\n')
# print(f'💰 Total Amount: ${total}')
# print('--------------------------------')

# string formatting

# BOOLEAN
# IF THEN ELSE
# if withdrawal amount > balance:
#    don't allow withdraw
# else:
#     allow withdrawal

# baby weather app
# if it's raining outside, grab an umbrella
# otherwise, grab your sunglasses

# BOOLEAN (True, False)
# True
# False

# weather = input('How is the weather? ')

# if weather == 'rain':
#   print('☔')

# elif weather == 'cloudy':
#   print('🌩️')

# elif weather == 'thunderstorm':
#   print('⛈️')

# else:
#   print('😎')

# comparison operators (==, <, >, <=, >=)

# >=90 👉 A
# >=80 👉 B
# >=70 👉 C
# >=60 👉 D
# <60 👉 F

# score = 53

# if score >= 90:
#   print('A')

# elif score >= 80:
#   print('B')

# elif score >= 70:
#   print('C')

# elif score >= 60:
#   print('D')

# else:
#   print('F')

# either a SUPER PASS passing grade or a failing grade
# Super Pass > 100

# score = 59
# if score >= 60 and score <= 100:
#   print('passing grade')

# if 60 <= score <= 100:
#    print('passing grade')

# if score < 60 or score > 100:
#   print('you either failed or you super passed')


# No arguments
def say_my_name():
    print('Rafeh Qazi')
    print('John')
    print('Kara')
    print('Sam')


# say_my_name()


# One Argument Inside a Function
def say_my_name_2(name):
    print(name)


# say_my_name_2('Rafeh')


# Multiple Arguments + Default arguments
def greeting(name, greet='aloha'):
    '''
  greeting takes in 2 arguments, greet & name
  and it greets the user

  >>> greeting('aloha', 'Qazi')
  "👋 aloha Qazi!"
  '''
    print(f"👋 {greet} {name}!")

    # positional arguments
    # greeting('Qazi', 'hello')

    # named arguments
    # greeting(greet='Hi', name='Qazi')

    # import
    '''
  Takes 2 integers, returns their sum
  >>> sum(1, 2)
  3
  '''


def sum(a: int, b: int) -> int:
    return a + b


# print(sum(1, 2))

### CONVERT THIS INTO A FUNCTION ###

# # Tip Calculator App
# food_amount = float(input('Enter food amount $: '))
# tip_percentage = float(input('Enter your tip percentage %: ')) / 100
# tip_amount = food_amount * tip_percentage


def calculateFoodTotal(food: float, tip_percentage: int) -> float:
  tip = food * (tip_percentage / 100)
  total = food + tip
  print('\n\n\n')
  print('--------------------------------')
  print(f'🥘 Food Amount: ${food}')
  print(f'⚖️ Tip Amount: ${tip}')
  print('\n')
  print(f'💰 Total Amount: ${total}')
  print('--------------------------------')
  return total
  
# print(calculateFoodTotal(100, 10))
# calculateFoodTotal(food=100, tip_percentage=20)

'''
weather_to_emoji takes in 1 argument as a string
(expected inputs: 'rain', 'thunderstorm', 'cloudy')
it returns nothing

>>> weather_to_emoji('rain')
'☔'

>>> weather_to_emoji('thunderstorm')
'⛈️'

>>> weather_to_emoji('sunny')
'😎'
'''
# TYPEHINTING
def weather_to_emoji(weather: str) -> None:
  if weather == 'rain':
    print('☔')
  
  elif weather == 'cloudy':
    print('🌩️')
  
  elif weather == 'thunderstorm':
    print('⛈️')
  
  else:
    print('😎')

# weather_to_emoji('rain')

# lambda - anonymous function

# implicit return
sum2 = lambda a, b: a + b
greet = lambda greet, name: f"{greet} {name}"
# print(greet('aloha', 'qazi'))

# print(sum2(5, 10))

# testing your code / unit tests


def test_sum():
  assert sum(1,2) == 3, '❌ sum(1,2) does not return 3 like it should'
  
  assert sum(-20, 20) == 0
  assert sum(20, 20) == 40
  assert sum(560, 780) == 1340
  
  print('Sum Function: All Tests Passsed (4/4) ✅')

# test_sum()

def test_calculate_food_total():
  assert calculateFoodTotal(100, 20) == 120
  # assert calculateFoodTotal(100.23, 20.43)

# test_calculate_food_total()

# LISTS (ARRAYS)
# methods list.append() vs. functions print()
# 
# fruits = ['🍎', '🍐', '🍊', '🍌', '🍪', 2, 5, 'hi', 8.5, [4, 3]]
# print(fruits)
# fruits.append('🍊')
# print(fruits)
# fruits.append('🍓')
# print(fruits)

# INDEXING
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[-1])

# how to ALWAYS get the last item in an list?

### SLICING ###
# print(fruits[0:3]) # first inclusive, 2nd exclusive
# print(fruits[0:4])
# print(fruits[0: len(fruits) - 1])
# print('HI my name is Qazi'[-1])
# print(fruits[::-1]) # reverse the list

### DICTIONARY ###
# Key 👉 Value
# Laptop (key) 👉 Apple (value)
# Mutable (change-able)


# print(person['name'])
# print(person['shirt'])
# print(person['laptop'])

def netWorth():
  return person['assets'] - person['debt']

def introducer():
  person = {
  'name': 'Qazi', 
  'shirt': 'Black', 
  'laptop': 'Apple',
  'phone_number': '224-123-3456',
  'assets': 100,
  'debt': 50,
  'favoriteFruits': ['🍎', '🍌', '🍊'],
  'netWorth': lambda: person['assets'] - person['debt']
}

  person['shirt'] = 'Orange'
  person['assets'] = 1000
  
  print(f"👋 Hi my name is {person['name']}, \n👕 I am wearing a {person['shirt']} shirt, \n👨‍💻 and the laptop I use to code is an {person['laptop']}, \n💰and my net worth is ${person['netWorth']()} USD, \n🥝My favorite fruits are {person['favoriteFruits']}")

  # print(list(person.values()))
  # print(person.keys())

# introducer()

### TUPLES () ###
# immutable
# numbers = (1, 2)
# print(numbers)
# print(type(numbers))
# print(numbers[0])

### SETS {} 👉 Used for getting unique stuff ###
# list1 = ['ruby', 'python', 'javascript']
# list2 = ['ruby', 'SQL', 'JAVA', 'javascript']

# programming_languages = set(list1 + list2)
# print(programming_languages)
# print('GO' in programming_languages) # 👉 False
# print('SQL' in programming_languages) # 👉 True

# print({1, 2, 2, 2, 2})

### SPECIAL KEYWORDS ###
# list, len, max, min, set, dict,

'''
Create a function unique, that
takes in a list and returns only unique items

>>> unique(['ruby', 'ruby', 'python'])
['ruby', 'python']
'''
# # def unique(languages): return list(set(languages))
# unique = lambda languages: list(set(languages))

# print(unique(['ruby', 'ruby', 'python']))

### LOOPS ###
# fruits = ['🍎', '🍐', '🍊', '🍌', '🍪']
# print('fruit:', fruits[0], 0)
# print('fruit:', fruits[1], 1)
# print('fruit:', fruits[2], 2)
# print('fruit:', fruits[3], 3)
# print('fruit:', fruits[4], 4)
# for fruit in fruits:
#   print(fruit)

# for index, fruit in enumerate(fruits):
#   print('fruit:', fruit, index)

# do this 5 times
# for _ in range(5):
#   print("haha")

# add 10 apples to the fruits list
# for _ in range(10):
#   fruits.append('🍎')

# print(fruits)

# print(fruits)

### TUPLE UN-PACKING ###

### WHILE LOOPS ###
# WATCHOUT FOR: 👉 INFINITE LOOP
# qazi = 'sitting'
# while qazi != 'standing':
#   print('Get Your Fat Butt Up 💯!')

# counter = 0
# while counter < 10:
#   print(counter)
#   counter += 1

'''
>>> double([1, 2, 3, 4, 5])
[2, 4, 6, 8, 10]
'''
def double(numbers: list) -> list:
  result = []
  for number in numbers:
    result.append(number * 2)
    
  return result

# print(double([1, 2, 3]))

# create empty list
# loop through & append to that list
# return that list

'''
Count Words if given a string,
should count & return the number of words

phrase: str

>>> count_words('Hi my name is Qazi')
5
'''
def count_words(phrase): return len(phrase.split())

# print(count_words('Hi my name is Qazi cookies cream soda legendary'))

'''
Create a function that given a list of numbers,
it can return their sum

>>> sum_list([1, 2, 3])
6
'''
def sum_list(numbers):
  count = 0
  for number in numbers:
    count += number

  return count

# print(sum_list([1, 2, 3]))
# print(sum_list([1, 2, 3, 4]))

'''
>>> find_max([1, 5, 10, 3])
10
'''
def find_max(numbers):
  current_max = numbers[0]
  for number in numbers:
    if number > current_max:
      current_max = number

  return current_max

# print(find_max([1, 2, 3, 10, 17, 4, 5, 6]))

# numbers = [1, 5, 10, 3]
# current_max = 1 # numbers[0]
# is 1 > current_max ? no
# go to next number
# is 5 > current_max ? yes
# current_max = 5
# is 10 > current_max ? yes
# current_max = 10
# is 3 > current_max ? no
# end the loop

### Dictionary Practice ###
'''
>>> word_frequency('I love Batman because I am Batman')
{'I': 2, 'love': 1, 'Batman': 2, 'because': 1, 'am': 1}
'''
def word_frequency(phrase):
  result = {}
  words = phrase.split()
  for word in words:
    if word not in result:
      result[word] = 1
    else:
      result[word] += 1

  return result

# print(word_frequency('I love Batman because I am Batman'))

# print(word_frequency(input('please enter your phrase: ')))

# result = {
#   'I': 2, 
#   'love': 1, 
#   'Batman': 2, 
#   'because': 1,
#   'am': 1,
# }

# # loop 1
# is 'I' in result? no
# set the key to 'I' and value to 1

# # loop 2
# is 'love' in result? no
# set the key to 'love' and value to 1

# # loop 3
# is 'Batman' in result? no
# set the key to 'Batman' and value to 1

# # loop 4
# is 'because' in result? no
# set the key to 'because' and value to 1

# # loop 5
# is 'I' in result? yes
# increment the value of 'I' key by 1

# # loop 6
# is 'am' in result? no
# set the key to 'am' and value to 1

# # loop 7
# is 'Batman' in result? yes
# increment the value of 'Batman' key by 1

### Higher Order Functions ###
# map
# filter

'''
>>> double([1, 2, 3])
[2, 4, 6]
'''
# def double_number(number):
#   return number * 2

# print(list(map(double_number, [1, 2, 3])))

# print(list(map(lambda num: num * 2, [1, 2, 3])))
# print(list(map(lambda num: num ** 2, [1, 2, 3])))
# print(double_number(1))

# def double(numbers: list) -> list:
#   result = []
#   for number in numbers:
#     result.append(number * 2)
    
#   return result

### FILTER ###
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(list(filter(lambda number: number % 2 == 0, numbers)))

### LIST COMPREHENSIONS ###
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# filter - and give me only EVEN numbers
# print([number for number in numbers if number % 2 == 0])

# # map - double numbers
# print([number * 2 for number in numbers])

# # get odd numbers
# print([number for number in numbers if number % 2 != 0])

# # give me all of the odd numbers CUBED
# print([number ** 3 for number in numbers if number % 2 != 0])

### SPECIAL BUILT-IN FUNCTIONS with Python ###
# >>> sum([1, 2, 3])
# 6
# >>> len([1, 2, 3])
# 3
# >>> max([1, 2, 3])
# 3
# >>> max([1, 2, 3, 10, 5, 7])
# 10
# >>> min([1, 50, -7, 337])
# -7

