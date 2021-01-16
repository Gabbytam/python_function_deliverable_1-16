#1
def sum_to(n):
    numsArr = []
    for num in range(n+1):
        numsArr.append(num)
    return sum(numsArr)

print(sum_to(4))
print(' ')

#2
def largest(arr):
    arr.sort()
    return arr.pop()

print(largest([10, 4, 2, 231, 91, 54]))
print(' ')

#3
#string method
# def occurances(string1, string2):
#     return string1.count(string2)

#longer version
#NOTE: list() method turns passed in value into a list, del keyword can be used to delete anything in python (in this case we delete a portion of the list), join() method takes in the iterable thing as an argument but must be attached to a string (attached to an empty string in this case)
def occurances(string1, string2):
    count = 0
    #getting the length of the second string will account for tests that are more than one character long
    length = len(string2)
    #while loop will run as long as string2 is in string1
    while (string2 in string1):
        #find the index of where the substring starts
        index = string1.index(string2)
        #turn the string into a list
        string1 = list(string1)
        #delete the portion of the list that consists of the substring passing in the range starting at the index of where the substring is found and stopping at the index plus the length of the substring
        del string1[index: (index + length)]
        #increment the count
        count += 1
        #the while loop conditional is on a string so the list has to be converted back to a string to keep running through
        string1 = ''.join(string1)
    #count is returned when there while loop is not evaluated to true (the substring is not in the string)
    return count

print(occurances('fleeep floop', 'e'))
print(occurances('fleep fleep', 'ee'))
print(occurances('fleep floop', 'e'))   # returns 2
print(occurances('fleep floop', 'p'))  # returns 2
print(occurances('fleep floop', 'ee')) # returns 1
print(occurances('fleep floop', 'fe'))  # returns 0
print(' ')

#4
def product(*argv):
    product = 1
    for arg in argv:
        product *= arg
    return product

print(product(4, 5, 7, 8))
