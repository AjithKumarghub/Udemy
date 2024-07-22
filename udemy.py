# variables
Vrls = 'My favorite color is black'
print(Vrls)

# Datatypes
idata_type = type(12)
idt = 24
sdata_type = type('')
sdt = ''
fdata_type = type(1.2)
fdt = 1.2
bdata_type = type(True)
bdt = True
print(fdt)
print(bdata_type)

# Arithmetic
num1 = 1
num2 = 2
answer_add = num1 + num2
answer_sub = num1 - num2
answer_mul = num1 * num2
answer_div = num1 / num2
print(answer_div)

# indexing & slicing string
# [] list notation
# ':' slice
sentence = 'this is a sentence'
print(sentence[-3:])

# strings
sentence = "12345 678910"
sentence = sentence.isdigit()
print(sentence)
sentence = "A1234*&%56"
print(sentence.startswith("4*&",4))

# string using the format method
sentence = 'The sum of {0} + {1} is {2}'.format(2, 18, 20)
print(sentence)

# list
my_list = [1,2,3,4,5]
appended=my_list.append('Hai')
# my_list.pop(0) using to slice the value from list
my_list[0] = ['hello','Goodbye']
my_list.append('This is a sentence')
print(my_list)
print(appended)
my_list = [1,5,2,4,3]
my_list.sort()
my_list.reverse()
print(my_list)
another_list = [6,7,8,9,10]
print(my_list+another_list)

# Nested list
my_list = ['a', 'b', '1', '2', ['apple', 'banana', 'orange'], 'd']
fruit_list = my_list[4][1]
print(fruit_list)

# Finding index position in list
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j']
counting = my_list.count('j')
print(counting)

# Tuples
my_tuple = (1, 2, 3,  'SOME DATA', [1, 2, 3])
my_tuple[4][2] = "New value"
print(my_tuple)

# dict
my_dict = {'K1': 'Hello', 'K2': 'World', 'k3': (1, 2, 3), 'k4': [1, 2, 3]}
my_dict['K2'] = 'wow'
my_dict.pop('k4')
my_dict['k4'][2] = 1
dit = my_dict['k3']
my_dict['k3'][1] = "Hi"
print(type(my_dict['k3']))
print(my_dict['k4'][1])

# Comparison operator
val = (5!=5 or 7>8)
val2 = 2 == 4 and 5 < 4
print(val)

# creating a function
# def greet_person():
# print("Hello, this is greeting...")
# greet_person()

# args and kwargs
# def main(*args):
#     """"
#     sum of 2 inputs
#     """
#     return sum(args)
#
# result = main(10,20,30)
# print(result)

# def main(**kwargs):
# print(kwargs.get('name'))
# main(name='Aji', id=10)

# scope variable
# age = 27
# print(age)
# def increase():
# age = 20
# age = age + 1
# print(age)
# increase()




