# You may accept the branch of study, score and course fee as inputs for each
# student 



def scholarship(branch_study, score, course_fee):

    if branch_study == "arts":
        if score >= 90:
            scholarship_amount = course_fee * 0.5
            final_fee = course_fee - scholarship_amount

            return final_fee

        elif score < 90 and score % 2 != 0:
                scholarship_amount = course_fee * (5/100)
                final_fee = course_fee - scholarship_amount

                return final_fee

        else:
            return course_fee

    if branch_study == "engineering":

        if score > 85:
            scholarship_amount = course_fee * 0.5
            final_fee = course_fee - scholarship_amount

            return final_fee

        elif score <= 85 and score % 7 == 0:
            scholarship_amount = course_fee * (5/100)
            final_fee = course_fee - scholarship_amount

            return final_fee

        else:
            return course_fee
            
if __name__ == "__main__":
    
    branch_study = input("Enter your branch of study: ")
    branch_study = branch_study.lower()

    score = int(input("Enter your score in persentage: "))
    course_fee = int(input("Enter the course fee: "))

    total = scholarship(branch_study, score, course_fee)

    print(f"Your branch is {branch_study} and your final fee to be paid is {total}")