#Problem5.py
#Project Euler problem 5
#Name: Olivia Sulzle
#Date: 3/8/26
#Assignment: Lab 7

from NumberTests import lcmUpTo

def main():
    result = lcmUpTo(20)
    print(f"The smallest positive number that is evenly divisible by all numbers from 1 to 20 is {result}")

if __name__ == '__main__':
  main()