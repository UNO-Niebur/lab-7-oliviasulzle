#Problem4.py
#Project Euler problem 4
#Name: Olivia Sulzle
#Date: 3/8/26
#Assignment: Lab 7

from NumberTests import getLargestPalindrome

def main():
  result, factors = getLargestPalindrome()
  print(f"The largest palindrome is {result}, which is the product of {factors[0]} and {factors[1]}")

if __name__ == '__main__':
  main()