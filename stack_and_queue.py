def CreateStack():
    """Creates an empty stack"""
    return []


def PushStack(item, Stack):
    """Add item to the top of stack"""
    Stack.append(item)


def PopStack(Stack):
    """Remove and return the item at the top of the stack"""
    return Stack.pop()


def TopStack(Stack):
    """Return the value of the item at the top of the stack
without removing it"""
    return Stack[-1]


def IsEmptyStack(Stack):
    """Check whether the Stack is empty"""
    return Stack == []



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

#topic1
def observe():
    my_queue = CreateQueue()
    my_stack = CreateStack()
    for i in [1,2,3,4]:
        PushQueue(i, my_queue)
        PushStack(i, my_stack)
    while not IsEmptyQueue(my_queue):
        print(PopQueue(my_queue))
    while not IsEmptyStack(my_stack):
        print(PopStack(my_stack))

#topic2
def schedule(queue):
    day = 0
    cant_done =[]
    while not IsEmptyQueue(queue):
        if day < TopQueue(queue)[0] :
            PopQueue(queue)
            day +=1
        else:
            cant_done.append(PopQueue(queue))
    return cant_done


#Sample Run of schedule func
'''q = CreateQueue()
PushQueue((1,"John"),q)
PushQueue((5,"George"),q)
PushQueue((1,"Lucy"),q)
PushQueue((2,"Arnold"),q)
PushQueue((3,"William"),q)
PushQueue((4,"Claude"),q)
print(schedule(q))'''

#topic3
def fixsorted(L):
    lenght = len(L)
    result = []
    stack = CreateStack()
    i = 0
    while i < lenght-1:
        if L[i] < L[i+1] and IsEmptyStack(stack):
            result.append(L[i])
        elif L[i] > L[i+1]:
            if not IsEmptyStack(stack):
                PushStack(L[i+1], stack)
            else:
                PushStack(L[i],stack)
                PushStack(L[i+1], stack)
        elif L[i] < L[i+1] and  not IsEmptyStack(stack):
            while not IsEmptyStack(stack):
                result.append(PopStack(stack))
        i +=1
    if not IsEmptyStack(stack):
        while not IsEmptyStack(stack):
                result.append(PopStack(stack))
    return result

#print(fixsorted([1,2,6,5,4,3,10,15,18,17]))

#topic4
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

  # if the destination is not reached, return -1
  return -1

#topic5 #unfinished
def route(roads, start, end):
  # create a queue and add the starting location to it
  queue = CreateQueue()
  PushQueue((start, 0), queue)

  # create a dictionary to map locations to the number of visited locations
  num_visited = {start: 0}

  # create a set to track visited locations
  visited = set()

  # keep processing locations until the queue is empty
  while not IsEmptyQueue(queue):
    # get the next location and number of visited locations from the queue
    location, num_visited_loc = PopQueue(queue)

    # if the location has not been visited, process it
    if location not in visited:
      # mark the location as visited
      visited.add(location)

      # update the number of visited locations for the location in the dictionary
      num_visited[location] = num_visited_loc

      # add all unvisited locations that are reachable from the current location
      for next_location in roads[location]:
        if next_location not in visited:
          PushQueue((next_location, num_visited_loc + 1), queue)

  # return the maximum number of visited locations
  return max(num_visited.values())


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

print(distance(roads,"A","L"))
print(route(roads, "A", "L")) 