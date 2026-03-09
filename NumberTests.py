#NumberTests.py

from math import gcd
from unittest import result


def isThreeOrFive(n):
  """Returns boolean determination if number is multiple of 3 or 5"""

  if n % 3 == 0 or n % 5 == 0:
    return True
  else:
    return False

def lcmUpTo(n):
  """Returns the least common multiple of all numbers from 1 to n."""
  lcm = 1
  for i in range(2, n + 1):
    lcm = lcm * i // gcd(lcm, i)
  return lcm

def getPrimeFactors(n):
  """Returns a list of prime factors of n with multiplicity."""
  factors = []
  while n % 2 == 0:
    factors.append(2)
    n = n // 2
  for i in range(3, int(n**0.5) + 1, 2):
    while n % i == 0:
      factors.append(i)
      n = n // i
  if n > 1:
      factors.append(n)
  return factors

def isPalindrome(n):
  """Returns true if the number is palindrome, otherwise returns false."""
  s = str(n)
  return s == s[::-1]

def getLargestPalindrome():
  """Finds largest palindrome made from the product of two 3-digit numbers."""
  max_palindrome = 0
  factors = (0, 0)
  for i in range(999, 99, -1):
    for j in range (999, 99, -1):
      product = i * j
      if isPalindrome(product) and product > max_palindrome:
        max_palindrome = product
        factors = (i, j)

  return max_palindrome, factors

def getFactors(num):
  """Returns a list of all factors of a given positive integer.

  Includes 1 and the number itself.
  """
  factors = []
  for f in range(1, num // 2 + 1):
    if num % f == 0:
      factors.append(f)

  # Every positive integer is divisible by itself.
  if num > 0:
    factors.append(num)

  return factors

def isPrime(p):
  """Returns True if p is a prime number, otherwise False.

  Handles edge cases: returns False for values less than 2.
  Uses trial division up to sqrt(p) for efficiency.
  """
  if p < 2:
    return False
  if p in (2, 3):
    return True
  if isEven(p):
    return False

  # Only need to test odd divisors up to sqrt(p).
  limit = int(p**0.5) + 1
  for div in range(3, limit, 2):
    if p % div == 0:
      return False

  return True


def isEven(n):
  """Returns boolean about given value being even."""

  if n % 2 == 0:
    return True
  else:
    return False

def addNum(numList, num):
  """Adds the given number to the list if it's not already present."""

  if num not in numList:
    numList.append(num)


def fibonacciSequence(value):
  """Returns a list of numbers in the fibonacci sequence up to the given value"""

  nums = [1, 2]
  size = 2
  n = nums[size - 1] + nums[size - 2]

  while n < value:
    addNum(nums, n)
    size = len(nums)
    n = nums[size - 1] + nums[size - 2]

  return nums

#Test your new functions in this main
def main():
  knownPrimes = [3, 7, 11, 13, 17]

  num = int(input("Enter a number: "))

  if isPrime(num):
    print("%d is a prime number" %(num))

  if isEven(num):
    print("%d is an even number" %(num))


if __name__ == '__main__':
    main()
