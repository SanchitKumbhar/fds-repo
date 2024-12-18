#Creating a list of marks obtained by students
AB = None
marklist = [10, 20, 30, AB, 50, 34, 24, 45, AB, 48, 23, 34, AB, 23, 34, 1, 19, 34]

#Calculating average
sum = 0
for marks in marklist:
    if marks != AB:
        sum = sum + marks
        average = sum / len(marklist)
print("(A). The average of marks is = ", average)

#Highest And Lowest Score in class
max_value = marklist[0]
min_value = marklist[0]
for marks in marklist:
    if marks != AB:
        if marks < min_value:
            min_value = marks
        if marks > max_value:
            max_value = marks
print("(B). The minimum value is = ", min_value)
print("(B). The maximum value is = ", max_value)

#Counting the number of absent students
absent_student = 0
for marks in marklist:
    if marks == AB:
        absent_student += 1
print("(C). The number of Absent students are = ", absent_student)

#Display Marks with highest frequency
frequency = {}
for marks in marklist:
    if marks != AB:
        if frequency.get(marks) == AB:
            frequency[marks] = 1
        else:
            frequency[marks] += 1
print("(D). The Frequency of marks is = ", frequency)