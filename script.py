# Starting data
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

# Subjects & grades
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Combining subjects and grades
gradebook = [
  [subjects[0], grades[0]],
  [subjects[1], grades[1]],
  [subjects[2], grades[2]],
  [subjects[3], grades[3]]
]

# Adding more subjects
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Modifying data
gradebook[-1][-1] = 98

# Removing data
gradebook[2].remove(85)

# Adding data
gradebook[2].append("Pass")

# Combining original data with new data
full_gradebook = last_semester_gradebook + gradebook

# Priting the combined list
print(full_gradebook)
