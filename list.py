#list is a built in data type  and we can also store diffrent type of data
marks =[64,7854,95,95,95,46,65,67,78,45]
print(marks)
print(type(marks))

#indexing
print(marks[2])
print(marks[4])

#different data
student = ["pratap",20,5.8,True]
print(student)

#changing value
student[0] = "Alice"
print(student)

#slicing
print(marks[3:6])
print(marks[ :7])
print(marks[2:7])

#list methods
marks.append(40)  #add one elememnt at the end
marks.sort()  #sorts in ascending order
marks.sort(reverse=True) #sorts in descending order
marks.reverse() #reverse list
marks.insert(9,80) #insert  element at the end
marks.remove(80) #remove element from list
marks.pop() #removes last element
