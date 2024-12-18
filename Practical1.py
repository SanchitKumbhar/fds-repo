#Creating a list for total students in SE Computer department 
SE_Comp = []
n = int(input("Number of students in Se Computer Department = "))
for i in range (0, n):
    element = input("Name of the Students in SE Computer Dept = ")
    SE_Comp.append(element)

#List for students who play cricket
cricket = [] 
n = int(input("Number of students playing cricket = "))
for i in range (0, n):
    element = input("name of the students playing cricket = ")
    cricket.append(element)  

#List for students who play Football
football = []
n = int(input("Number of students playing football = "))
for i in range (0, n):
    element = input("Name of students playing Football = ")
    football.append(element)

#List for students who play badminton
badminton = []
n = int(input("Number of students who play Badminton = "))
for i in range (0, n):
    element = input("Name of students who play Badminton = ")
    badminton.append(element)

#Removing duplicate elements in the list
def removeDuplicate(list1):
    list = []
    for i in (list1):
        if i not in list:
            list.append(i)
    return list 

print("Total students in SE_Comp are",removeDuplicate(SE_Comp)) 
print("Total students in Cricket are",removeDuplicate(cricket)) 
print("Total students in Football are",removeDuplicate(football)) 
print("Total students in Badminton are",removeDuplicate(badminton))      

#Intersection of two lists
def intersection (list1, list2):
    list3 = []
    for val in list1:
        if val in list2:
            list3.append(val)
    return list3 

#Union of two list 
def union (list1, list2):
    list3 = list1.copy()
    for val in list2:
        if val not in list3:
            list3.append(val)
    return list3

#Difference of two lists
def difference (list1, list2):
    list3 = []
    for val in list1:
        if val not in list2:
            list3.append(val)
    return list3 

print("Who play cricket and badminton are ", intersection(cricket, badminton))
print("Who play either cricket or badminton but not both ",difference(union(cricket, badminton), intersection(cricket,badminton)))
print("Who neither plays cricket nor badminton",difference(SE_Comp, union(cricket, badminton)))
print("Who plays cricket and football but not badminton", difference(intersection(cricket, football), badminton))
      
