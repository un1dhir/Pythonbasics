# list data structure

# list are mutable (changeable) line 11
# list are ordered
# list have indexes starting from 0
# uses[] and not ()
fruits=['apple', 'banana' , 'mangoes' , 'pineapple' , 'orange' , 'pear']
print(fruits)

fruits[2]="Watermelon"
print(f"I sell {fruits[2]}")

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[1:])
numbers.append(9)

wildanimals=['Buffalo', 'Giraffe' , 'Cheetah' , 'Leopard' , 'Lion', 'Crocodile']
print(wildanimals[3:])
print(wildanimals[4])
# tuples data structures

# tuples are unchangeable (imutable) line 24
# tuples are ordered
# tuples have indexes
# uses ()
cars=('Aston Martin','Lexus','Porshe','Range Rover','Mercedes','Mustang')
print(cars)
# cars[3]=Lambogini
print(cars[2])
nambari=(1,2,3,4,5,6,7,8,9,10)
print(len(nambari))

# set data structures
days=('Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday', 'Sunday')
print(days[3])

# dictionaries data structure
# Is mutable (changable)

students={"Name": "John", "Age":45,"Gender": "M", "School": "eMbolis"}
print(students["Name"])
print(students["Age"])