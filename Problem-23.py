#  A teacher is in the process of generating a few reports based on the marks scored by the
# students of her class in a project based assessment.
# Assume that the marks of her 10 students are available in a tuple. The marks are out of 25.
# Write a python program to implement the following functions:

# 1. find_more_than_average(): Find and return the percentage of students who have scored
# more than the average mark of the class.

# 2. generate_frequency(): Find how many students have scored the same marks. For
# example, how many have scored 0, how many have scored 1, how many have scored
# 3….how many have scored 25. The result should be populated in a list and returned.

# 3. sort_marks(): Sort the marks in the increasing order from 0 to 25. The sorted values
# should be populated in a list and returned.


def  find_more_than_average(list_of_marks):

    average = sum(list_of_marks) / 10
    count = []
    for scores in list_of_marks:
        if scores > average:
            count.append(scores)
    return len(count) * 10


def generate_frequency(list_of_marks):

    list2 = []
    count = 0
    for score in range(26):
        if score in list_of_marks:
            list2.append(list_of_marks.count(score))
        else:
            list2.append(count)
    return list2

def sort_marks(list_of_marks):

    list3 = []
    for score in list_of_marks:
        list3.append(score)
        list3.sort()
    return list3

if __name__ == "__main__":
    list_of_marks = (12,18,25,24,2,5,18,20,20,21)

    print(find_more_than_average(list_of_marks))

    print(generate_frequency(list_of_marks))

    print(sort_marks(list_of_marks))

    