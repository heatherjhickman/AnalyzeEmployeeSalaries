"""
Author: Heather Hickman
Date: 2/11/2019
Program: hickman_exam1
Summary: The program will analyze employee salaries from the given EmployeeSalaries.txt file.

1. CONSTANTS
    none

2. VARIABLES
    inFile = ""                 # for reading the txt file
    employeeSalaries = []       # for transferring the txt file contents into a list
    sumTotal = 0                # for totalling the contents of the list
    count =                     # counter of elements in the list
    average = 0                 # sumTotal / count

3. INPUTS
    none

4. PROCESSES
    a.	Open the EmployeeSalaries.txt file for reading.
    b.	Transfer the txt file into the employeeSalaries[] list.
    c.	Use an accumulator to find the sumTotal of the salaries in the employeeSalaries[] list.
    d.	Use a counter to find the total number of elements in the list.
    e.	Find the average by dividing the sumTotal by the count.
    f.	Use the min and max functions to find the lowest and highest salaries.

5. OUTPUTS
    g.	Print the lowest and highest salaries, the sumTotal, and the average.
"""

def main():
    # initialize variables
    inFile = ""
    employeeSalaries = []
    sumTotal = 0
    count = 0
    average = 0
    minNumber = 0
    maxNumber = 0

    # opening the EmployeeSalaries.txt file for reading.
    inFile = open('EmployeeSalaries.txt', 'r')
    employeeSalaries = inFile.readlines()
    inFile.close()

    # strip the newline characters from the list
    for i in range (len(employeeSalaries)):
        employeeSalaries[i] = employeeSalaries[i].rstrip('\n')
    #print(employeeSalaries)

    # find the lowest and highest numbers using the min and max functions
    minNumber = min(employeeSalaries)
    maxNumber = max(employeeSalaries)
    #print(minNumber)
    #print(maxNumber)

    # convert the numbers in the list to integers
    # find the sumTotal of the numbers in the employeeSalaries[] list
    for eachLine in employeeSalaries:
        number = int(eachLine)
        sumTotal += number
    # print(sumTotal)

    # find the count and the average of the numbers in employeeSalaries[] list
    count = (len(employeeSalaries))
    average = sumTotal / count
    #print(average)

    # display the results for the user
    print("The lowest salary listed is \t", minNumber)
    print("The highest salary listed is \t", maxNumber)
    print("The total of the salaries is \t", sumTotal)
    print("The average of the salaries is \t", average)

main()