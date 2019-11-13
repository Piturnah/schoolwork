import multilines as auto

#TASK 3.4
students = int(input("Please enter the number of students:\n\n> "))
books = int(input("Please enter the number of books\n\n> "))

booksPerStudent = books // students
booksLeft = books % students

output = auto.col("Books per student: " + str(booksPerStudent) + "\nBooks left over:" + str(booksLeft), "auto", "l", ":", "")

print(auto.box(output, 15, "c"))
