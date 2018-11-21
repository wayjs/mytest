# Author:ways
import os
#我是公司代码修改2
def print_name(name):
	print(name)
	print(1)
	print(1)
	print(1)
import time
def print_sum(n,m):
	print(n+m)
print_sum(2,3)
age_of_oldboy=56
count=0
print_name("ways")
while count<3:
    guess_age=int(input("guess age:"))
    if guess_age==age_of_oldboy:
        print("you get it")
        break
    elif guess_age>age_of_oldboy:
        print("think smaller")
    else:
        print("think bigger")
    count += 1
else:
    print("you have tried too many times .... fuck off")
def warpper(func):
	def inner(*args,**kwargs):
		if (1=1):
			func()
	return warpper

@warpper
def login():
	print("登陆成功")
login()