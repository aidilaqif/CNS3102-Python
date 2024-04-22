# Question 2
# Write a program to find the average marks of 3 subjects.
# The program should accept the marks from the user.
# The total mark for each subject is 100.

# Declare an empty array of subject
subjects = []

# Declare variables for calculation
subject_full_mark = 100
total_marks = 0
average_marks = 0

total_subjects = int(input(f"Enter the number of subjects: "))

# Looping to accept input for 3 subject
for i in range(total_subjects):
    subject_name = input(f"Enter subject {i + 1} name: ")
    subject_marks = int(input(f"Enter marks for subject {i + 1}: "))
    subjects.append((subject_name, subject_marks))
print()

# Calculate total marks
total_marks = sum([marks for _,  marks in subjects])

# Calculate average marks
average_marks = total_marks / len(subjects)

# Print the output
print("Subjects and marks: ")
for subject in subjects:
    print(f"{subject[0]}= {subject[1]}/", subject_full_mark)
print("\nTotal marks = ", total_marks, "/", (subject_full_mark*len(subjects)))
print("Average marks = ", average_marks, "/100")