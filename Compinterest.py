# P is the original principal sum
# P' is the new pricipal sum
# r is the annual nominal annual interest rate
# n is the compunding frequency
# t is the overall length of time the interest is appplied.

principal = 10000
n = 12
r = 8 / 100
t = int(input('Enter the amount of years that the principal will be compounded for: '))
final_amount = principal * (1 + (r / 9))**(n * t)
print('The final ampount is :', final_amount)


