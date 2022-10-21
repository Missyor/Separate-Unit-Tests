######Creating Unit Tests in separate files

##Creating a unit test to test the largerNumbers() function

##We need to import the myProgram file to this file

import myProgram as mp #saves time writing mp instead of myProgram

##TASK 4 def a function called unit test. 
##It takes in lists of numbers with 5 elements - once you define the function, create 2 lists of 5 numbers between -1 and 100. Call the first list firstNums and the second list secondNums
def unitTest():
  firstNums = [1, 2, 3, 4, 5]
  secondNums = [-1, 6, 90, 4, 100] #testing each scenario - where the numbers are >, < or = each other. 

##We want to create a variable called fails. It will count the number of times our function fails. We have to initialise it. What value should it be equal to at the beginning?
  fails = 0

##We want to go through each item in both lists and put them through the largerNumber() function. Each time it goes through the list it stores the value, tests it and goes on to the next one. 
  for i in range (len(firstNums)):
    test1 = firstNums[i]##create the test values
    test2 = secondNums[i]
##create the test answer by running the test values through the function by calling it from the mp file
    testAnswer = mp.largerNumber(test1, test2)
##if the first number is bigger than the second but it doesnt match the test answer, increase the fails counter by 1. Or else if test2 doesnt match the test answer, increase the fails counter by 1
    if test1 > test2:
      if test1 != testAnswer:
        fails += 1
    else:
      if test2 != testAnswer:
        fails += 1

##We want to return the fail count
  return fails

##outside of our function we want to print: Total test fails: unit test result
print("Total test fails: ", unitTest()) 