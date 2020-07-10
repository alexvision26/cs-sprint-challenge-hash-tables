#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # need to order all tickets
    # START ticket has a source of None
    # FINAL ticket has a destination of None
    # tickets are passed in via a list
    # needs to output in the correct order, the source needs to point to the pPREV, dest needs to point to NEXT

    route = []
    cache = {}

    for x in tickets:
        if x not in cache:
            cache[x.source] = x.destination
        else:
            continue

    # src = list(cache.keys())
    count = 0
    for x in tickets:
        if x.source == 'NONE':
            route.append(x)
        
        if x.destination in cache:
            route.append(x)

        count += 1

    return route

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                   ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

print(reconstruct_trip(tickets, 10))