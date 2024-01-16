import random
password_generator=int(input("Enter the required password length:"))
d="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password="".join(random.sample(d,password_generator))
print(password)