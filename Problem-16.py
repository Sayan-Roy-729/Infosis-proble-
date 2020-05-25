def get_tickets(ai, src, dest, no):
    t_no = 101
    ai = ai.upper()
    src = src[:3]
    dest = dest[:3]

    l = []

    for i in range(no):
        s = ai + ":" + src + ":" + dest + ":" + str(t_no)
        l.append(s)
        t_no += 1

    l = l[-5:]
    return l
        
    

if __name__ == "__main__":
    airline = input("Enter the airline: ")
    source = input("Enter the source: ")
    destination = input("Enter the destination: ")
    no_of_passenger = int(input("Enter the number of passengrs: "))

    ticket = get_tickets(airline, source, destination, no_of_passenger)

    print(ticket)
