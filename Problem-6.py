# The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows:
# ● Rate per Adult: Rs. 37550.0
# ● Rate per Child: 1/3rd of the rate per adult
# ● Service Tax: 7% of the ticket amount (including all passengers)
# ● As it was a holiday season, the airline also offered a 10% discount on the final ticket cost (after inclusion of the service tax).
# ● Find and display the total ticket cost for a group which had adults and children.


def ticket(adult, child):

    ticket = adult * 37550 + 37550 * (1/3) * child
    ticker_service_tax = ticket + ticket * (107/100)
    final_ticket = ticker_service_tax - ticker_service_tax * (90/100)

    return final_ticket

if __name__ == "__main__":
    
    adult = int(input("Enter the numbers of adult passengers: "))
    child = int(input("Enter the number of child passengers: "))

    ticket = ticket(adult, child)
    print(f"Total amount of your ticket is Rs. {ticket}")