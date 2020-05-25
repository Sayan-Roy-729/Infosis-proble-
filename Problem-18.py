# The road transport corporation (RTC) of a city wants to know whether a particular bus-route
# is running on profit or loss.

# Assume that the following information are given:
# Price per litre of fuel = 70
# Mileage of the bus in km/litre of fuel = 10
# Price(Rs) per ticket = 80

# The bus runs on multiple routes having different distance in kms and number of passengers.
# Write a function to calculate and return the profit earned (Rs) in each route. Return -1 in case
# of loss.


def road_transport_corporation(distance, passenger):

    price_ticket = 80 * passenger

    total_fuel = distance * 0.1

    fuel_cost = total_fuel * 70

    if price_ticket > fuel_cost:
        profit = price_ticket - fuel_cost
        return f"The profit earned Rs. {profit}"
    else:
        return "-1"


if __name__ == "__main__":
    distance = int(input("Enter the total distance: "))
    passenger = int(input("Enter the total numbers of passengers: "))

    cost = road_transport_corporation(distance, passenger)

    print(cost)