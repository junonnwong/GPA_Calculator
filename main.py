import math
def truncate(number:float, decimal):
        number *= math.pow(10, decimal)
        number = math.trunc(number)
        return number / math.pow(10, decimal)

print("GPA Calcalator");
cgpa = 0;
totalCreditHourCGPA = 0;
gradept=[4,3.67,3.33,3,2.67,2.33,2,0];
semester = input("How many semester that you wanted to calculate for CGPA: ")
while not semester.isdigit():
        print("Error, Please Try Again");
        semester = input("How many semester that you wanted to calculate for CGPA: ");
for j in range(int(semester)):
        subject = input(f"Enter amount of the subject for semester {j+1}: ");
        while not subject.isdigit():
                print("Error, Please Try Again");
                subject = input("Enter amount of the subject: ");
        subject = int(subject);
        gpa = 0;
        totalCreditHour = 0;
        for i in range(subject):
                creditHour = input(f"\nCredit Hour for subject {i+1}:");
                while not creditHour.isdigit():
                        print("Error, Please Try Again");
                        creditHour = input(f"Credit Hour for subject {i+1}:")
                creditHour = int(creditHour);
                while True:
                        print("Credit Hour :", creditHour);
                        print(f"The {i+1} subject's grades:\n1.A+/A\n2.A-\n3.B+\n4.B\n5.B-\n6.C+\n7.C\n8.F");
                        index = input();
                        while not index.isdigit():
                                print("Error, Please Try Again");
                                print(f"The {i+1} subject's grades:\n1.A+/A\n2.A-\n3.B+\n4.B\n5.B-\n6.C+\n7.C\n8.F");
                                index = input();
                        index = int(index) - 1
                        if index >= 0 and index < len(gradept):
                                print("Grade point obtained :", gradept[index])
                                gpa += gradept[index] * creditHour
                                totalCreditHour += creditHour
                                break;
        print(f"Your GPA for this semester is {truncate(gpa / totalCreditHour, 4)}\n");
        print(f"Credit hour earned :{totalCreditHour}\n");
        cgpa += gpa;
        totalCreditHourCGPA += totalCreditHour;
        print(f"CGPA : {truncate((cgpa / totalCreditHourCGPA), 4)}")
        print(f"Total credit hour earned : {totalCreditHourCGPA}\n");

            
