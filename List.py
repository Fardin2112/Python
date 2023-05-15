Marks = [98,95,99,88,75,80]
print(Marks)
print(Marks[1])
# in python index also in negative
# ex -1 mean last index , -2 mean sec last index
print(Marks[-1])

#for print marks in range
# ex- first 2 marks
print(Marks[0:2])
#note 2 will be not count it will print from index 0 to 1

print(Marks[2:-1])

# for add more element in list
Marks.append(100)

#for adding in position
Marks.insert(0,97)
print(Marks)

# for checking that an element exist or not in list
print(100 in Marks)
print(0 in Marks)

# for find lenght of list
print(len(Marks))

# print the element of list by loop
i = 0
while i < len(Marks):
    print(Marks[i])
    i = i+1

#for clear all data
Marks.clear()
print(Marks)