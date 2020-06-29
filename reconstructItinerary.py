'''Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.'''
def findItinerary(tickets):
    import collections
    itinerary = collections.defaultdict(list)
        
    for departure, arrival in tickets:
        itinerary[departure].append(arrival)
        
    len_tickets = len(tickets)
        
    def dfs(start_airport, curr_hop, len_tickets):
        if len(curr_hop) == len_tickets:
            return curr_hop + [start_airport]
            
        if start_airport not in itinerary:
            return None 
            
        for next_hop in sorted(itinerary[start_airport]):
            itinerary[start_airport].remove(next_hop)
            travel_graph = dfs(next_hop, curr_hop + [start_airport], len_tickets)
            if travel_graph:
                return travel_graph
            itinerary[start_airport].append(next_hop)
                
    return dfs('JFK', [], len_tickets)
    
    
Input1 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output1 = ["JFK","ATL","JFK","SFO","ATL","SFO"]
print(findItinerary(Input1))
`
