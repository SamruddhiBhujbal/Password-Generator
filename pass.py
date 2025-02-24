import random
import string
import re

length=int(input("Enter the length of your password:"))

upper=string.ascii_uppercase
lower=string.ascii_lowercase
num=string.digits
symbols=string.punctuation

all=upper+lower+num+symbols

temp=random.sample(all,length)
psd="".join(temp)
print(psd)