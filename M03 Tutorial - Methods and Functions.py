# I was unsure how you wanted this homework to be formatted, so I am doing my best here. Please let me know if I was supposed to
# do it differently, and if I missed that instruction somewhere, I apologise.

import math
import string

# Write a function that computes the volume of a sphere given its radius.

def vol_sphere(radius):
    return ((4/3) * math.pi * (radius ** 3))

# Output that I didn't want to take up space unnesesarily
# print(vol_sphere(3))


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def range_check(num, low, high):
    if num > low and num < high:
        print(str(num) + " is between " + str(low) + " and " + str(high))
    else: 
        print(str(num) + " is not between " + str(low) + " and " + str(high))

# Output that I didn't want to take up space unnesesarily
# range_check(3, 4, 10)


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def num_cases(stringVar):
    upper = 0
    lower = 0

    for letter in stringVar:
        if letter.isupper():
            upper += 1
        else:
            lower += 1
    
    print("The number of uppercase is: " + str(upper))
    print("The number of lowercase is: " + str(lower))

    return 

# Output that I didn't want to take up space unnesesarily
# test = "Hello"
# num_cases(test)


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(listVar):
    newList = []
    
    for item in listVar:
        if item in newList:
            pass
        else:
            newList.append(item)
    return newList

# Output that I didn't want to take up space unnesesarily
# oldList = [1,1,1,1,2,2,3,3,3,3,4,5]
# newList = unique_list(oldList)
# print(newList)


# Write a Python function to multiply all the numbers in a list.

def mult_list(listVar):
    multiplied = 1
    
    for item in listVar:
        multiplied *= item
    
    return multiplied

# Output that I didn't want to take up space unnesesarily
# listNums = [1, 2, 3, -4]
# print(mult_list(listNums))


# Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(word):
    reverse = word[::-1]
    
    if reverse == word:
        print("It is a palindrome!")
    else:
        print("It is not a palindrome.")

# Output that I didn't want to take up space unnesesarily
# palindrome("helleh")

# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

def pangram(stringVar):
    alph = string.ascii_lowercase
    stringConv = stringVar.lower()

    for letter in alph:
        if letter in stringConv:
            pass
        else:
            print("String is not a pangram.")
            return
    print("String is a pangram!")
    return

# Output that I didn't want to take up space unnesesarily
# pangram("The quick brown fox jumps over the lazy dog")