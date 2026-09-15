import csv as cs 
with open("data.csv", "r") as file:
    reader = cs.reader(file)
    header = next(reader)
    highest_score = 0
    highest_student = " "
    lowest_score = None
    lowest_student = ""
    total_output = 0
    count = 0

    #temp variable for sort time only
    newname = ""
    answer = 0


   

    # for row in reader:
    #     score = int(row[2])
    #     total_output = total_output + score
    #     count = count + 1
    # avrage = total_output / count
    # print(avrage)

    #for row in reader:
      #  print(row)

    

    #task is to find the greatest score from all the students
    
    #this section is to find greatest score among the students get the mark and find who gets it highest
    # for row in reader:
    #     score = int(row[2])
    #     if score > highest_score:
    #         highest_score = score
    #         highest_student = row[0]
    #     count +=1


    #this section is to find lowest score among the students get the mark and find who gets it lowest
    # for row in reader:
    #     score = int(row[2])
    #     if lowest_score is None or score < lowest_score:
    #         lowest_score = score
    #         lowest_student = row[0]
    #     count +=1

    # print("Highest score = ", highest_score)
    # print("Highest-scoring student = ", highest_student)
    # print("Total students = ", count)


    for row in reader:
        if row in reader:
            score = int(row[2])
            if score >= 85:
                print(row[0], score)

            

    print("Lowest score = ", lowest_score)
    print("lowest-scoring student = ", lowest_student)
    print("Total students = ", count)

    print(newname)
