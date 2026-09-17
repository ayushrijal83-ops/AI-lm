import csv as cs 
with open("data.csv", "r") as file:

    reader = cs.reader(file)
    header = next(reader)

    highest_score = 0
    highest_student = ""
    lowest_score = None
    lowest_student = ""
    count = 0
    total_score = 0
    high_scorers = []

    for row in reader:

        score = int(row[2])
        total_score = score + total_score

        if score > highest_score:
            highest_score = score
            highest_student = row[0]

        if lowest_score is None or score < lowest_score:
            lowest_score = score
            lowest_student = row[0]

    
        if score >= 85:
            high_scorers.append((row[0], score))

        count += 1
    

#Output part 
print("----------------------STUDENT REPORT------------------------")
print("Total Students = ", count)
print("Avrage Score = ", total_score/count,"\n")

print("Highest score = ",highest_score)
print("Highest Student = ", highest_student,"\n")

print("Lowest score = ", lowest_score)
print("lowest student", lowest_student,"\n")

print("<-------------Students getting 85 or higher:-------------->")
for student, score in high_scorers:
    print(student, score)