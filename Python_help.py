homework_score = 0

assessment_score = 0

final_exam = 0

#average = 0

def add_homework(homework_score1, assessment_score1, final_exam1):
    average = 0
    while average == 0:
        if homework_score < 0 or homework_score > 25:
            break

        if assessment_score < 0 or assessment_score > 50:
            pass

        if final_exam < 0 or final_exam > 100:
            pass 
        average = ((homework_score/25) + (assessment_score/50) + (final_exam/100))/3*100
    return average

homework_score = int(input("What was your homework score: "))
assessment_score = int(input("What was your assessment score: "))
final_exam = int(input("What was your final exam score: "))

print(add_homework(homework_score, assessment_score, final_exam))
