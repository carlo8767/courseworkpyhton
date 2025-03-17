import heapq
from queue import PriorityQueue
# https://medium.com/@adithjrajeev/priority-queues-and-dijkstras-algorithm-5a45526f99ad
if __name__ == "__main__":
    # YOU CAN CREATE A PRIORITY QUEUEE WITH A LIST
    list_priority = list()
    list_priority.append((1, "Names"))
    list_priority.sort(reverse=True)

    # O (log n)
    names =  []
    heapq.heappush(names, (0,"Italy"))
    heapq.heappush(names, (1, "Germany"))
    heapq.heappush(names, (4, "Usa"))
    print(heapq.heappop(names))
    print(names[0])

    probability = []
    s = heapq
    s.heappush(probability, (2, 0.1))
    s.heappush(probability, (4, 0.2))
    s.heappush(probability, (4, 0.2))
    s.heappush(probability, (3, 0.5))
    print(s.heappop(probability))
    print(probability[1])
    probability_ts = []
    ts = heapq

    ts.heappush(probability_ts, (0.1, 2))
    ts.heappush(probability_ts, (0.2, 4))
    ts.heappush(probability_ts, (0.5, 3))
    ts.heappush(probability_ts, (0.1, 4))
    print(ts.heappop(probability_ts))


    names = PriorityQueue
