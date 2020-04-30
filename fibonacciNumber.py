# Input an integer n, and this program will output all fibonacci numbers less than n using a while loop

def fibonacci(n):
  a = 0
  b = 1
  while (a < n):
    print(a, end = ' ')
    a = b
    b = a + b
  print()

k = input("Please enter an integer: ")
fibonacci(k)
