import string
import random



def new_func(lowerCase, upperCase, numbers, symbols, passLenght):
    password="".join(random.sample(lowerCase+upperCase+numbers+symbols,passLenght))
    return password

lowerCase=string.ascii_lowercase
upperCase=string.ascii_uppercase
numbers=string.digits
symbols='[]{}()*?!+%&.,-_'

passLenght=16

password = new_func(lowerCase, upperCase, numbers, symbols, passLenght)

print(password)