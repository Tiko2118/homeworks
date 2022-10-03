my_name = "tiko"
my_surname = "omanadze"
my_age = 27

my_sentence = "tiko {} omanadze {} 27 {}". format(my_name, my_surname, my_age)
print(my_sentence)

my_name = "tiko"

if "t" in my_name:
    print("sheicvalos e-s")


#input
#output

my_name = input("enter your name")
print("chemi saxelia" + my_name)
 
my_age = 27
my_age += 3
print(my_age)
my_surname = "omanadze"

my_age = input("enter your age: ")
my_name = input("enter your name: ")
my_surname =input("enter your surname: ")
print("my name is {} my surname is {} my age is {}".format(my_name,my_surname,my_age))
my_age += 3
print("after 3years i am now {} years old".format(my_age))





num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))

#საინკრებეტაციო ცვლადი
my_sum = 0
#13, 20, 7
if num1 % 2 == 1:
    my_sum += num1
if num2 % 2 ==    