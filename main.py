def grading(j):
        if grades[j] == 1:
            return 4;
            
        elif grades[j] == 2:
            return 3.67;
            
        elif grades[j] == 3:
            return 3.33;
            
        elif grades[j] == 4:
            return 3;
            
        elif grades[j] == 5:
            return 2.67;
            
        elif grades[j] == 6:
            return 2.33;

        elif grades[j] == 7:
            return 2;

        elif grades[j] == 8:
            return 0;

        else:
            return 999;

def gpacalc():
        gpa = 0;
        sumHour = 0;
        for k in creditHour:
                sumHour += k;
        for l in range(subject):
                gpa = gpa + (gradept[l] * creditHour[l] / sumHour);
        return gpa;


print("GPA Calcalator");
subject = input("Enter the subject of a semester: ");
while not subject.isdigit():
        print("Error, Please Try Again");
        subject = input("Enter the subject of a semester: ");
subject = int(subject);
grades=[];
gradept=[];
creditHour=[]
for i in range(subject):
        creditHour.append(input(f"Credit Hour for subject {i+1}:"))
        while not creditHour[i].isdigit():
                print("Error, Please Try Again");
                creditHour[i] = input(f"Credit Hour for subject {i+1}:")
        creditHour[i] = int(creditHour[i]);
        while True:
                print("Credit Hour :", creditHour[i]);
                print(f"The {i+1} subject's grades:\n1.A+/A\n2.A-\n3.B+\n4.B\n5.B-\n6.C+\n7.C\n8.F");
                scanf = input();
                while not scanf.isdigit():
                        print("Error, Please Try Again");
                        print(f"The {i+1} subject's grades:\n1.A+/A\n2.A-\n3.B+\n4.B\n5.B-\n6.C+\n7.C\n8.F");
                        scanf = input();
                if not 999 in gradept:
                        grades.append(int(scanf));
                        gradept.append(grading(i));
                else:
                        grades[i] = int(scanf);
                        gradept[i] = grading(i);
                print(gradept[i],creditHour[i])
                if gradept[i]!= 999:
                    break;
gpa = round(gpacalc(),4);
print(f"Your GPA for this semester is {gpa}");
    
    
