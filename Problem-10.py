def shopOutput(one_rupee_coin, five_rupee_coin, purchase_amount):

    if (one_rupee_coin + 5 * five_rupee_coin) >= purchase_amount:

        five_rupee_requie = purchase_amount // 5
        one_rupee_require = purchase_amount - five_rupee_requie * 5

        print(f"Rs. 1 coins needed {one_rupee_require} and Rs. 5 notes needed {five_rupee_requie} ") 

    else:
        print("-1")


if __name__ == "__main__":
    
    one_rupee_coin = int(input("Enter the available Rs. 1 coins: "))
    five_rupee_coin = int(input("Enter the available Rs. 5 notes: "))
    purchase_amount = int(input("Enter amount to be made: "))

    shopOutput(one_rupee_coin, five_rupee_coin, purchase_amount)