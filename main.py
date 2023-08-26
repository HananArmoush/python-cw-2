my_name= input("your name is : ")
my_age=input("your age is :")
print(f"my name is {my_name} and i am {my_age} years old")

first_number= int(input('enter num'))
secound_number= int(input('enter secound num'))

operation=input('/*-+')

if operation == '*':
   print(first_number * secound_number)

elif operation == '-':
  print(first_number - secound_number)

elif operation == '+':
  print(first_number + secound_number)

elif operation == '-':
  print(first_number/secound_number)

else :
  print('the operation is not vaild')


bus_capacity= 50
people_inbus= int(input('people in the bus'))
pepole_waiting= int(input('pepole who wait'))
empty_seates= bus_capacity - people_inbus

if empty_seates > pepole_waiting:
  print(f'هناك مقاعد خالية عددها {empty_seates}')

elif empty_seates<= pepole_waiting:
  print(f'الباص ممتلئ')


