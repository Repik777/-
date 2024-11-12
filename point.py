grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_grades = {'Aaron': [5, 3, 3, 5, 4], 'Bilbo': [2, 2, 2, 3], 'Johnny': [4, 5, 5, 2], 'Khendrik': [4, 4, 3], 'Steve': [5, 5, 5, 4, 5]}
sum_0 = sum(grades[0]) #sum(grades[1]), sum(grades[2]), sum(grades[3]), sum(grades[4])
name_0 = sum_0 / 5
print(name_0)
sum_1 = sum(grades[1])
name_1 = sum_1 / 4
print(name_1)
sum_2 = sum(grades[2])
name_2 = (sum_2 / 4)
print(name_2)
sum_3 = sum(grades[3])
name_3 = sum_3 / 3
print(name_3)
sum_4 = sum(grades[4])
name_4 = sum_4 / 5
print(name_4)
names = 'Aaron: ' + str(name_0), 'Bilbo: ' + str(name_1), 'Johnny: ' + str(name_2), 'Khendrik: ' + str(name_3), 'Steve: ' + str(name_4)
print(names)
