def percentage_score(score):

    if score <= 100 and score >= 80:
        print("Grade ----> A")

    elif score <= 79 and score >= 73:
        print("Grade ----> B")

    elif score <= 72 and score >= 65:
        print("Grade ----> C")

    elif score <= 64 and score >= 0:
        print("Grade ----> B")

    else:
        print("Grade ----> Z")



if __name__ == "__main__":
    score = int(input("Enter the score: "))
    percentage_score(score)