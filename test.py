  #-- Install a package on Command Prompt --#
# py -m pip install numpy #
#print('hello')
#name=('Py')
#Greet=('Hi')
#print(Greet+' '+name)
#x = 1
#if x == 1:
#    print("x is 1")
#myint = 1
#print(myint)
#myfloat = 2.0
#print(myfloat)
#myfloat = float(3)
#print(myfloat)
#mystring = ("don't")
#print(mystring)
#one = 1
#two = 2
#three = one + two
#print(three)
#a,b = 3,4
#print(a,b)
#mystring = "Hi"
#myint = 2
#myfloat = 3.0
#if mystring == "Hi":
#    print("String is %s" % mystring)
#if isinstance(myint, int) and myint == 2:
#    print("Integer: %d" % myint)
#if isinstance(myfloat, float) and myfloat == 3.0:
#    print("Float: %f" % myfloat)
#mylist = []
#mylist.append(1)
#mylist.append(2)
#mylist.append(3)
#print(mylist[0])
#for x in mylist:
#	print(x)
#names = ["John", "Eric", "Jessica"]
#second_name = names[1]
#print("The second name in the list is %s" % second_name)
#number = 1*2 + 3/4
#print(number)
#remainder = 11 % 3
#print(remainder)
#square = 3**2
#cube = 3**3
#print(square,cube)
#hellos = "hello"*10
#print(hellos)
#even = [2,4,6]
#odd = [1,3,5]
#all = even + odd
#print(all)
#print([1,2]*2)
#x = object()
#y = object()
#x_list = [x]*10
#y_list = [y]*10
#big_list = x_list + y_list
#print("x_list contains %d objects" % len(x_list))
#print("y_list contains %d objects" % len(y_list))
#print("big_list contains %d objects" % len(big_list))
#if x_list.count(x) == 10 and y_list.count(y) == 10:
#	print("almost")
#if big_list.count(x) == 10 and big_list.count(y) == 10:
#	print("great")
#name = "John"
#print("Hello %s!" %name)
#age = 23
#print("%s is %d years old" %(name,age))
#list = [1,2,3]
#print("A list of %s" %list)
#float = 3.0
#print("%.2f" %float)
#print("%x" %4095)
#data = ["John","Doe",53.2]
#format_string = "Hello"
#print("%s" %format_string, "%s" %data[0], "%s," %data[1], "your balance is RM%.2f." %data[2])
#print("'")
#print('"')
#print("\"")
#string = "Hello World!"
#print(string.count(""))
#print(string.index("o"))
#print(string[-1])
#print(string[0:6:2]) #--[start:stop:step]
#print(string.upper())
#print(string.lower())
#print(string.startswith("Hel"))
#print(string.endswith("a"))
#print(string.split(" "))
#s = "Hey there! what should this string be?"
#print("Length of s = %d" % len(s))
#print("The first occurrence of the letter a = %d" % s.index("a"))
#print("a occurs %d times" % s.count("a"))
#print("The first five characters are '%s'" % s[:5])
#print("The characters with odd index are '%s'" %s[1::2])
#x = 2
#print(x==2)
#print(x!=3)
#print(x<3)
#if x==2 and x<3:
#	print("Yes")
#if x==2 or x>3:
#	print("True")
#if x in [1,2]:
#	print("got 2")
#statement = True
#statement2 = False
#if statement is True and statement2 is True:
#	print("both True")
#elif statement is True:
#	print("1")
#	pass
#elif statement2 is True:
#	print("2")
#	pass
#else:
#	print("both False")
#	pass
#number = 100
#second_number = []
#first_array = [1,2,3]
#second_array = [1,2]
#if number > 15:
#    print("1")
#if first_array:
#    print("2")
#if len(second_array) == 2:
#    print("3")
#if len(first_array) + len(second_array) == 5:
#    print("4")
#if first_array and first_array[0] == 1:
#    print("5")
#if not second_number:
#    print("6")
#primes = [2, 3, 5, 7]
#for prime in primes:
#    print(prime)
#for x in range(5):
#    print(x)
#for x in range(3, 6):
#    print(x)
#for x in range(3, 8, 2):
#    print(x)
#count = 0
#while count < 5:
#    print(count)
#    count += 2
#count = 0
#while True:
#    print(count)
#    count += 1
#    if count >= 5:
#        break
#for x in range(10):
#    if x % 2 == 0: #--Check if x is even
#        continue
#    print(x)
#count=0
#while(count<5):
#    print(count)
#    count +=1
#else:
#    print("count value reached %d" %(count))
#for i in range(1, 10):
#    if(i%5==0):
#        break
#    print(i)
#else:
#    print("not")
#numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
#for x in numbers:
#	if x == 237:
#		break   #--decide the end range
#	if(x%2!=0):
#		continue   #--skip it
#	print(x)
#def list1():
#    return "A", "B", "C", "D"
#def sentence(l):
#    return "%s is in list" %l
#def function1():
#    listFunction = list1()
#    for l in listFunction:
#        print(sentence(l))
#function1()
  #-- function print sentence for each list element
  #-- Class is the template to create objects
#class Vehicle:
#    name = ""
#   kind = "car"
#    color = ""
#    value = 0.00
#    def sentence(obj):
#        description = "%s is a %s %s worth RM%.2f." % (obj.name, obj.color, obj.kind, obj.value)
#        return description
  #-- Objects
#car1 = Vehicle()
#car1.name = "Fer"
#car1.color = "red"
#car1.kind = "convertible"
#car1.value = 60000.00
#car2 = Vehicle()
#car2.name = "Jump"
#car2.color = "blue"
#car2.kind = "van"
#car2.value = 10000.00
#print(car1.sentence())
#print(car2.sentence())
  #-- Dictionaries -do not keep order of values
#dictionaries = {}
#dictionaries["A"] = 1
#dictionaries["B"] = 2
#dictionaries["C"] = 3
#print(dictionaries)
#dictionaries = {"A": 1, "B": 2, "C": 3}
#print(dictionaries)
  #-- to iterate value pairs
#for name, number in dictionaries.items():
#    print("The number of %s is %d" % (name, number))
  #-- to delete value
#dictionaries = {"A": 1, "B": 2, "C": 3}
#del dictionaries["A"]
#print(dictionaries)
  #-- or delete
#dictionaries = {"A": 1, "B": 2, "C": 3}
#dictionaries.pop("B")
#print(dictionaries)
  #-- to add value
#dictionaries = {"A": 1, "B": 2, "C": 3}
#dictionaries["D"] = 4
#print(dictionaries)
  #--Modules & Packages
#import re
#find_members = []
#for member in dir(re):
#    if "find" in member:
#        find_members.append(member)
#print(sorted(find_members))
  #--Numpy = Arrays
#A = [1,2,3]
#B = [4,5,6]
#import numpy as np
#np_A = np.array(A)
#np_B = np.array(B)
#print(type(np_A))
#area = np_A * np_B
#print(area)
#print(area > 10)
#print(area[area > 10])
  #-- Pandas = Data frames
#dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
#       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
#       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
#       "population": [200.4, 143.5, 1252, 1357, 52.98] }
#import pandas as pd
#brics = pd.DataFrame(dict)
#brics.index = ["BR", "RU", "IN", "CH", "SA"]
#print(brics)
  #-- import csv file from same location as py
#cars = pd.read_csv('cars.csv', index_col = 0)
  #-- series
#print(cars['Industry_code_ANZSIC06'])
  #-- frames
#print(cars[['Industry_code_ANZSIC06']])
#print(cars[['Industry_code_ANZSIC06','Units']])
  #-- first 4 observations
#print(cars[0:4])
  #-- iloc - _th observation
#print(cars.iloc[2])
  #-- loc - [row or index],[column]
#cars = pd.read_csv('cars.csv')
#print(cars.loc[[10,1420],['Value']])
  #-- Generators
#import random
#def lottery():
  #-- number of integers
#    for i in range(6):
#        yield random.randint(1, 40)
  #-- next integer
#    yield random.randint(1, 15)
#for random_number in lottery():
#       print("And the next number is... %d!" %(random_number))
#def fib():
#    a, b = 1, 1
#    while 1:
#        yield a
#        a, b = b, a + b
  #-- testing code
#import types
#if type(fib()) == types.GeneratorType:
#    print("Good, The fib function is a generator.")
#    counter = 0
#    for n in fib():
#        print(n)
#        counter += 1
#        if counter == 10:
#            break
  #-- List Comprehension
#sentence = "the brown fox jumps"
#words = sentence.split()
#word_lengths = [len(word) for word in words if word != "the"]
#print(words)
#print(word_lengths)
#numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
#newlist = [float(x) for x in numbers if x > 0]
#print(newlist)
  #-- Lambda Function
#a = 1
#b = 2
#sum = lambda x,y : x + y
#c = sum(a,b)
#print(c)

#list = [2,4,7,3,14,19]
#for i in list:
#    my_lambda = lambda x : (x % 2) == 1
#    print(my_lambda(i))

  #-- Multiple functions
#def foo(first, second, third, *therest):
#    print("First: %s" %(first))
#   print("Second: %s" %(second))
#    print("Third: %s" %(third))
#    print("And all the rest... %s" %(list(therest)))
#foo(1, 2, 3, 4, 5)

#def bar(first, second, third, **options):
#    if options.get("action") == "sum":
#        print("The sum is: %d" %(first + second + third))
#    if options.get("number") == "first":
#        return first
#result = bar(1, 2, 3, action = "sum", number = "first")
#print("Result: %d" %(result))

  #-- amount of extra arguments received
#def foo(a, b, c, *args):
#    return len(args)
  #-- if "magicnumber" matches
#def bar(a, b, c, **kwargs):
#    return kwargs["magicnumber"] == 7
#if foo(1, 2, 3, 4) == 1:
#    print("Good.")
#if foo(1, 2, 3, 4, 5) == 2:
#    print("Better.")
#if bar(1, 2, 3, magicnumber=6) == False:
#    print("Great.")
#if bar(1, 2, 3, magicnumber=7) == True:
#    print("Awesome!")

  #-- Regular Expression (Regex)
#import re
#def test_email(your_pattern):
#    pattern = re.compile(your_pattern)
#    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
#    for email in emails:
#        if not re.match(pattern, email):
#            print("You failed to match %s" % (email))
#        elif not your_pattern:
#            print("Forgot to enter a pattern!")
#        else:
#            print("Pass")
#pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
#test_email(pattern)

  #-- Exception Handling
#def do_stuff_with_number(n):
#    print(n)
#def catch_this():
#    the_list = (1, 2, 3)
#    for i in range(5):
#        try:
#            do_stuff_with_number(the_list[i])
#        except IndexError:
#            do_stuff_with_number(0)
#catch_this()

#actor = {"name": "John Cleese"}
#def get_last_name():
#    return actor["name"].split()[1]
#get_last_name()
#print("All exceptions caught! Good job!")
#print("The actor's last name is %s" % get_last_name())

  #-- Set -list with no duplicate
#print(set("1 2 3 1 3 4".split()))

#a = set(["A","B","C"])
#b = set(["A","D"])
#print(a,b)
  #-- both
#print(b.intersection(a))
  #-- only one
#print(b.symmetric_difference(a))
  #-- one & not other
#print(b.difference(a))
#print(a.difference(b))
  #-- union
#print(b.union(a))

  #-- Serialization -convert data into format which allow to store, transmit, recreate
#import json 
#json_string = json.dumps([1, 2, 3, "a", "b", "c"])
#print(json_string)
  #-- or
#import pickle
#pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
#print(pickle.loads(pickled_string))

#def add_employee(salaries_json, name, salary):
#    salaries = json.loads(salaries_json)
#    salaries[name] = salary
#    return json.dumps(salaries)
#salaries = '{"Alfred" : 300, "Jane" : 400 }'
#new_salaries = add_employee(salaries, "Me", 800)
#decoded_salaries = json.loads(new_salaries)
#print(decoded_salaries["Alfred"])
#print(decoded_salaries["Jane"])
#print(decoded_salaries["Me"])

  #-- Partial Function -variable in a function
#from functools import partial
#def multiply(x, y):
#        return x * y
#dbl = partial(multiply, 2)
#print(dbl(3))

#def func(u, v, w, x):
#    return u*1 + v*1 + w*1 + x
#p = partial(func,3,1,4)
#print(p(2))

  #-- Code Introspection
#help(dir)
#help(hasattr)
#help(id)
#help(type)
#help(repr)
#help(callable) 
#help(issubclass)
#help(isinstance)
#help(__doc__)
#help(__name__)

#class Vehicle:
#    name = ""
#    kind = "car"
#    color = ""
#    value = 100.00
#    def description(self):
#        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
#        return desc_str
#print(dir(Vehicle))

  #-- Closure
  #-Nested function
#def transmit_to_space(message):
#    "This is the enclosing function"
#    def data_transmitter():
#        "The nested function"
#        print(message)
#    data_transmitter()
#print(transmit_to_space("Test message"))

  #-Nonlocal
#def print_msg(number):
#    def printer():
#        "Here we are using the nonlocal keyword"
#        nonlocal number
#        number=3
#        print(number)
#    printer()
#    print(number)
#print_msg(9)

  #-Function object
#def transmit_to_space(message):
#    "This is the enclosing function"
#    def data_transmitter():
#        "The nested function"
#        print(message)
#    return data_transmitter
#fun2 = transmit_to_space("Burn the Sun!")
#fun2()

  #-Nested loop + closure = multiple functions
#def multiplier_of(n):
#    def multiplier(number):
#        return number*n
#    return multiplier
#multiplywith5 = multiplier_of(5)
#print(multiplywith5(9))

  #-- Decorator -simple modifications to callable objects like functions, methods, or classes
#@decorator
#def functions(arg):
#    return "value"

  # -Multiply output
#def multiply(multiplier):
#    def multiply_generator(old_function):
#        def new_function(*args, **kwds):
#            return multiplier * old_function(*args, **kwds)
#        return new_function
#    return multiply_generator 
    # "it returns the new generator"
# "Usage"
#@multiply(3) 
# "multiply is not a generator, but multiply(3) is"
#def return_num(num):
#    return num
# "Now return_num is decorated and reassigned into itself"
#print(return_num(5))

  # -check if the input is the correct type
#def type_check(correct_type):
#    def check(old_function):
#        def new_function(arg):
#            if (isinstance(arg, correct_type)):
#                return old_function(arg)
#            else:
#                print("Bad Type")
#        return new_function
#    return check

#@type_check(int)
#def times2(num):
#    return num*2

#print(times2(2))

#print(times2('A'))

#@type_check(str)
#def first_letter(word):
#    return word[0]

#print(first_letter('Hello World'))

#print(first_letter(123))

  #-- Map - map(func, *iterables)
  #- upper
#my_string = ['al', 'tab', 'will']
#uppered_string = list(map(str.upper, my_string))
#print(uppered_string)

  #- round & decimal place
#circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
#result = list(map(round, circle_areas, range(1, 6)))
#print(result)

  #- zip (combine iterables into tuple)
#my_strings = ['a', 'b', 'c', 'd', 'e']
#my_numbers = [1, 2, 3, 4, 5]
#results = list(zip(my_strings, my_numbers))
#print(results)

  #-- Filter - filter(func, iterable) - return only the true boolean values
#scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
#def is_A(score):
#    return score > 75
#over_75 = list(filter(is_A, scores))
  #OR#
#over_75 = list(filter(lambda num: num>75, scores))
#print(over_75)

  # - palindrome reads the same from both ends
#dromes = ("demigod", "rewire", "madam", "freer", "rajar", "kiosk")
#palindromes = list(filter(lambda word: word == word[::-1], dromes))
#print(palindromes)

  #-- Reduce - reduce(func, iterable[, initial]) - reduce iterables into single value, starting from initial
#from functools import reduce
#numbers = [1,2,3,4]
#def custom_sum(first, second):
#    return first + second
#result = reduce(custom_sum, numbers)
  #OR#
#result = reduce(lambda num1, num2: num1 + num2, numbers)
#print(result)

#from functools import reduce
#numbers = [1,2,3,4]
#def custom_sum(first, second):
#    return first + second
#result = reduce(custom_sum, numbers, 5)
#print(result)

from functools import reduce 
#my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
#my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]
#map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
#filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)
#print(map_result)
#print(filter_result)
print(reduce_result)


