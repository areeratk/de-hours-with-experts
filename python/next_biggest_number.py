#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    #TODO: Implement me!

    #For a given number, convert the number into string
    #For all string characters, convert each character into an integer creating an array of single digit integers 
    n = len(str(num))
    number = [int(x) for x in str(num)]

    #Start from the farthest right digit of the array, find the smaller first digit next to it     
    for i in range(n-1,0,-1):
         if number[i] > number[i-1]:
             break
              
    #If find no such next smaller digit, the numbers must be in a descending order
    #Return -1 when the next biggest number cannot be created
    if i == 1 and number[i] <= number[i-1]:
        print ("-1")
        return -1
          
    #Find the smallest digit on the right side of (i-1)'th digit that is greater than number[i-1]
    x = number[i-1]
    smallest = i
    for j in range(i+1,n):
        if number[j] > x and number[j] < number[smallest]:
            smallest = j
          
    #Swapping the above found smallest digit with (i-1)'th
    number[smallest],number[i-1] = number[i-1], number[smallest]
      
    # x is the final number, in integer datatype
    x = 0
    # Converting list upto i-1 into number
    for j in range(i):
        x = x * 10 + number[j]
      
    # Sort the digits after i-1 in ascending order
    number = sorted(number[i:])
    # converting the remaining sorted digits into number
    for j in range(n-i):
        x = x * 10 + number[j]
      
    print (x)

    return x

if __name__ == "__main__":
    main()



