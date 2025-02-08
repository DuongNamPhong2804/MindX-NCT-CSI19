"""
def uppercase(input_str):
    return input_str.upper()

uppercase("hello")

import math

def cal_diagonal(ede_lenght):
    return math.sqrt(2) * ede_lenght

cal_diagonal(4)


def sum_digits(num):
    res = 0
    while num > 0:
        res += num % 10
        num //= 10
    return res

sum_digits(1234)


input_number = int(input("Enter a number: "))
def day_of_week(n):
    days = {
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
        8: "Sunday"
    }
    return days[n]

print(day_of_week(input_number))



def find_substring(string, substring):
    
    n = len(substring)
    sub_n = len(substring)
    for i in range(n - sub_n + 1):
        if substring == string[i: + sub_n]:
            return i
    return -1

find_substring("1234567", "3459")


def is_symmetric(inp):

    n = len(inp)

    if n <= 1:
        return True
    
    for i in range(n // 2):
        if inp[i] != inp[n - i - 1]:
            return False
    return True

is_symmetric("123421")


class Person:
    #khởi tạo
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "name: {0} - age: {1}".format(self.name, self.age)
    
    def say_hi(self):
        print("Xin chào bạn " + self.name)

    def tell_the_day(self, day):
        print("Today is " + day)

class Engineer(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary

    def __str__(self):
        return "name: {0} - age: {1} - salary: {2}".format(self.name, self.age, self.salary)
    
#Engineer1 = Engineer("Marry", 24, "$1000")
#Personl = Person("John", 40)
#print(Personl)
#Personl.say_hi()
#Personl.tell_the_day("Monday")
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def caculate_perimeter(self):
        return (self.width + self.height) * 2
    
    def caculate_area(self):
        return self.width * self.height
    
rec1 = Rectangle(5, 4)
print(rec1.caculate_perimeter())
print(rec1.caculate_area())