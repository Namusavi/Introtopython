def calc(num):
 if num % 3 == 0 and num % 5 == 0:
  return 'FizzBuzz'
 elif num % 3 == 0:
  return 'Fizz'

 elif num % 5 == 0:
  return 'Buzz'
 else:
  return num


if __name__ == "__main__":

 for n in range(1, 100):
  print(calc(n))

















































