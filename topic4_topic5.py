#answers to the topic 4 and 5 for stack and queue questions at pyceng

#necessary queue functions
def CreateQueue():
    """Creates an empty queue"""
    return []


def PushQueue(item, Queue):
    """Add item to the end of queue"""
    Queue.append(item)


def PopQueue(Queue):
    """Remove and return the item at the front of the queue"""
    p = Queue[0]
    del Queue[0]
    return p


def TopQueue(Queue):
    """Return the value of the item at the front of the queue
without removing it"""
    return Queue[0]


def IsEmptyQueue(Queue):
    """Check whether the Queue is empty"""
    return Queue == []

#topic4

#problem statement:
"""Write a function named distance which takes a dictionary of roads between locations, a starting point and a destination. 
It should return the shortest path between the starting point and the destination. Try to solve this problem only using 
stacks and integers as variables and without recursion.

Hint: keep the current location and the distance to that location from the starting point as a tuple in the 
queue e.g. ("B",1) or ("A",0) from starting point "A"."""

def distance(roads, start, end):
    # create a queue and add the starting location to it
    queue = CreateQueue()
    PushQueue((start, 0), queue)

    # create a set to track visited locations
    visited = set()

    # keep processing locations until the queue is empty
    while not IsEmptyQueue(queue):
    # get the next location and distance from the queue
        location, dist = PopQueue(queue)

    # if the location has not been visited, process it
        if location not in visited:
        # mark the location as visited
            visited.add(location)

        # if the location is the destination, return the distance
        if location == end:
            return dist

        # add all unvisited locations that are reachable from the current location
        for next_location in roads[location]:
            if next_location not in visited:
                PushQueue((next_location, dist + 1), queue)

#topic5

#problem statement: 
"""A courier needs to stop by several locations to deliver items. Write a function named route which takes a dictionary of roads between locations, 
a starting point and a destination. It should return the maximum number of locations that a courier can visit between and including staring 
point and the destination. Try to solve this problem only using stacks and integers as variables and without recursion.

Hint: keep the current location and the number of visited locations as a tuple in the queue e.g. ("B",2) or ("A",1) from starting point "A".
"""
def route(roads, start, end):
  # create a queue and add the starting location to it
    queue = CreateQueue()
    PushQueue((start, 1), queue)

    # create an empty list to keep track of possible results
    possible_results = []
    # keep processing locations until the queue is empty
    while not IsEmptyQueue(queue):
    # get the next location and number of visited locations from the queue
        location, num_visited_loc = PopQueue(queue)
        #if location is the end point we have a possible result
        if location == end:
            possible_results.append(num_visited_loc)

        #add every reachable point from current locations to the queue with number of visited places = num_visited_loc+1
        for next_location in roads[location]:
            PushQueue((next_location, num_visited_loc + 1), queue)

    # the result will be the maximum of possible results
    return max(possible_results)


roads = {
   "A": ["B", "C"],
   "B": ["F"],
   "C": ["D", "E"],
   "D": ["L"],
   "E": ["D"],
   "F": ["E", "G", "K"],
   "G": ["H"],
   "H": ["I", "J"],
   "I": ["L"],
   "J": ["L"],
   "K": [],
   "L": [], }
#answers to the given examples:
print("Distance from A to L is ",distance(roads,"A","L")) #should print 3
print("Maximum points can be visited from A to L is ",route(roads, "A", "L")) #should print 7