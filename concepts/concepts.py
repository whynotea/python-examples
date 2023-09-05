
def strongly_typed():
  myInt=int(1)
  myDouble=2.9
  myResult = myInt + myDouble
  print("Strongly typed, however as variables are dynamically typed, adding an int and a double implicitly sets the result type to double preventing data loss:")
  print(f"{myInt} + {myDouble} = {myResult}:\n")

strongly_typed()

def power(a, b = 2):
  return a ** b

x = power(b=2,a=3)
print(f"The result of passing by keyword, power(b=2,a=3) = {x}")
x = power(2,3)
print(f"The result of passing by position, power(2,3) = {x}")
x = power(2)
print(f"The result of passing by position with a default value, power(2) = {x}")

def append(input_list=None, to_append=None):
  if input_list is None:
    input_list = []
  if to_append is None:
    input_list.append('###')
  else:
    input_list.append(to_append)
  return input_list

my_list = append()
print(f"The contents of my list after calling append once is: {my_list}")
my_list = append(input_list=my_list)
print(f"The contents of my list after calling append twice is: {my_list}")
my_list = append(input_list=my_list, to_append="???")
print(f"The contents of my list after calling append three times but with to_append = ??? is: {my_list}")

def passByValue(myValue):
  myValue += 5
  return myValue

myValue = 5
print(f"myValue is {myValue}")
myNewValue = passByValue(myValue)
print(f"after calling passByValue: myValue is {myValue}, myNewValue is {myNewValue}")

def passByReference(myList):
  myList.append(5)
  return myList


myList = [5]
print(f"myList is {myList}")
myNewList = passByReference(myList)
print(f"after calling passByReference: myList is {myList}, myNewList is {myNewList}")
