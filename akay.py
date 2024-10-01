import random

char="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length =int(input('Şİfreniz kaç karakter olsun'))

password =''
for i in range(char_length):
    password +=random.choice(char)
print('Şifreniz:',password)