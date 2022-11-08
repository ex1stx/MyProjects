import random
low_case = 'qwertyuiopasdfghjklzxcvbnm'
up_case = 'QWERTYUIOPASDFGHJKLZXCVBNM'
num_case = '1234567890'
symvol = '!@#$%^&*'

Use_for = low_case + up_case + num_case + symvol
length_for_pass = 8

password = "".join(random.sample(Use_for, length_for_pass))

print('Password: '+ password)