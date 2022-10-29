import heapq

# By default heapq of python implements min priority queue.
heap_list = [5, 4, 3, 2]

# 1. heapify (will convert the whole list into heap.)
heapq.heapify(heap_list)


# by default top is the first element of heap.
print(f"Top element of heap : {heap_list[0]}")

# heappush will add the element into the list and rearrange.
heapq.heappush(heap_list, 6)

print(f"size of heap {len(heap_list)}")

# removes the top element of list
popped_element = heapq.heappop(heap_list)

print(f"Popped element of heap : {popped_element}")


"""
some cases how to create max heap
1. multiply the elements with minus and add it to heap and while removing multiply element with -1
"""

print("------------------------------------------------------")

max_heap_list = []
for i in range(6):
  heapq.heappush(max_heap_list, -i)

print("Popped element of max heap: ")
while(max_heap_list):
  print(-1*heapq.heappop(max_heap_list))


print("-------------------------------------------------------")
print("Priority Queue on pair element")
# if tuple is there then heap will set the priority according to first element.
tuple_heap_list = [("Apple", 1), ("Orange", 2), ("Cherry", 4), ("Banana", 3)]
heapq.heapify(tuple_heap_list)

while tuple_heap_list:
  print(heapq.heappop(tuple_heap_list))


print("----------------------------------------------------------------------------")
# Custom Sorting In heap (for this you have to create seperate class and insert the values)
class FruitCount:
  def __init__(self, fruit_name: str, fruit_count: int):
    self.fruit_name = fruit_name
    self.fruit_count = fruit_count

  def __repr__(self):
    return f"({self.fruit_name, self.fruit_count})"

  def __lt__(self, other):
    return self.fruit_count>other.fruit_count

fruit_counter_list = [FruitCount("Apple", 1), FruitCount("Orange", 2), FruitCount("Cherry", 4), FruitCount("Banana", 3)]
heapq.heapify(fruit_counter_list)

print("Custom Comparator Priority Queue: ")
while fruit_counter_list:
  print(heapq.heappop(fruit_counter_list))

