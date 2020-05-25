# Write a python function, find_pairs_of_numbers() which accepts a list of positive integers
# with no repetitions and returns count of pairs of numbers in the list that adds up to n. The
# function should return 0, if no such pairs are found in the list.

def find_pairs_of_numbers(list1, n):

    count = 0
    for i in list1:
        for j in list1:
            if (i + j) == n:
                count += 1
    
    return (count // 2)

if __name__ == "__main__":
    
    list1 = [1, 2, 7, 4, 5, 6, 0, 3]
    n = 6 

    print(find_pairs_of_numbers(list1, n))