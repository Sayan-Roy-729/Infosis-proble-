def chicken_rabbit(total_head, total_leg):

    rabbit_head = (total_leg - 2 * total_head) // 2
    chicken_head = total_head - rabbit_head

    print(f"Total rabit are {rabbit_head} and total chicken are {chicken_head}")

if __name__ == "__main__":
    total_head = int(input("Enter the total heads: "))
    total_leg = int(input("Enter the total legs: "))

    chicken_rabbit(total_head, total_leg)