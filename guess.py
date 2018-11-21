# Author:ways
import time
def print_sum(n,m):
	print(n+m)
print_sum(2,3)
age_of_oldboy=56
count=0
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