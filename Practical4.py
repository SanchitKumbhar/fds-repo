student_roll = [1,2,3,4,23,35,57,48,56,34,74,5,24,56,35,64,35,53,63,6,34,62]

#Linear Search
def linear_search(list, key):
    for i in range (len(student_roll)):
        if student_roll[i] == key:
            return i
    else:
        print ("Student is Absent")

print("(Linear Search) The student is present at the position = ", linear_search(student_roll, 35))

#Sentinel Search 
def sentinel_search (list, key):
    last = list[-1]
    list[-1] = key 
    i = 0

    while list[i] != key:
        i = i + 1
    if i != len(list) - 1:
        return i
    if last == key:
        return len(list) - 1
    
    return -1

print("(Sentinel Search) The students is present at the position = ", sentinel_search(student_roll, 56))
