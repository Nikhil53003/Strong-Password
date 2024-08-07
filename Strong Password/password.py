import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbols="!@#$%^&*"

string= lower+upper+number+symbols

lenght= 8

password= "".join(random.sample(string,lenght))

print("your strong password is: ",password)