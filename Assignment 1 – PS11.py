import time
class CyclesPerMonth:
  def __init__(self, NoOfCycles, Month):
    #create a list
    self.heap = []
    self.NoOfCycles = NoOfCycles
    self.Month = Month

class MaxHeap:
  def __init__(self, max_size=1000):
    #create a list
    self.heap = []
    self.max_size = max_size

  #define max size for heap and exception

  #function to add value to the existing heap and then again heapify nodes
  #add exception for heap limit

  def heap_push(self, item):
    # Raise an exception if the heap is full
    if len(self.heap) == self.max_size:
      raise Exception("Heap is full. Cannot add more elements.")

    #add data to the list and heapify
    self.heap.append(item)
    self.heapify_up(len(self.heap) - 1)

  def heap_pop(self):
    # Raise an exception if the heap is empty
    if not self.heap:
      raise Exception("Heap is empty. Cannot remove elements.")

    #pop data -last element from the list and heapify
    if len(self.heap) == 0:
      return None
    if len(self.heap) == 1:
      return self.heap.pop()
    item = self.heap[0]
    self.heap[0] = self.heap.pop()
    self.heapify_down(0)
    return item

  def heapify_up(self, index):
    # Raise an exception if the heap is empty
    if not self.heap:
      raise Exception("Heap is empty. Cannot arrange elements.")
    if index == 0:
      return
    parent_index = (index - 1) // 2
    if self.heap[parent_index] < self.heap[index]:
      self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[
        parent_index]
      self.heapify_up(parent_index)

  def heapify_down(self, index):
    # Raise an exception if the heap is empty
    if not self.heap:
      raise Exception("Heap is empty. Cannot arrange elements.")
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    largest_index = index
    if left_index < len(
        self.heap) and self.heap[left_index] > self.heap[largest_index]:
      largest_index = left_index
    if right_index < len(
        self.heap) and self.heap[right_index] > self.heap[largest_index]:
      largest_index = right_index
    if largest_index != index:
      self.heap[index], self.heap[largest_index] = self.heap[
        largest_index], self.heap[index]

#empty output file in the beginning of program
with open("outputPS11.txt", "w") as output_file:
      output_file.write("******Assignment PS 11 - Cycle Park Using Heap Max***********")
      output_file.write("\n\n")

def ReadFileWithExceptionHandling():
  try:
    input_file = open("inputPS11.txt", "r")
    # abc = input_file.read()
    # if len(abc) == 0:
    #     raise Exception()
    # else:
    list = ReadInputFile(input_file)
    input_file.close()
    return list
  except FileNotFoundError:
    print("File not present")
    return None


#   except Exception:
#     print("File is empty. Please provide a file with data and try again.")
#     return None

#Read data from the input file
def ReadInputFile(input_file):
  parent_list = []
  # do exception handing for reading file here
  for line in input_file:
    # Split the line into park name, number of cycles, and month
    #exception handling for missing data
    park, cycles, month = line.strip().split(",")
    # Convert the number of cycles to an integer
    #exception handling for invalid/missing data
    cycles = int(cycles.strip())
    month = month.strip()
    park = park.strip()
    parent_list.append((cycles, park, month))
  return parent_list

def MethodMain():
  # create heap
  my_heap = MaxHeap()
  for item in my_list:
    my_heap.heap_push(item)
  def ListPark():
    copy_heap = my_heap.heap.copy()
    park_list = []
    for i in range(len(copy_heap)):
      park_name = copy_heap.pop()[1]
      if park_name not in park_list:
        park_list.append(park_name)

    with open("outputPS11.txt", "a") as output_file:
        output_file.write("List of cycling parks:\n")
        output_file.write(", ".join(park_list) + "\n\n")
    return(park_list)

  def ListMonth():
    copy_heap = my_heap.heap.copy()
    month_list = []
    for i in range(len(copy_heap)):
      month_name = copy_heap.pop()[2]
      if month_name not in month_list:
        month_list.append(month_name)

    # with open("outputPS11.txt", "a") as output_file:
    #     output_file.write("List of cycling parks:\n")
    #     output_file.write(", ".join(park_list) + "\n\n")
    return(month_list)


  print("""
  1. List Parks
  2. Number of cycles across a month
  3. Park with maximum number of cycles in a given month
  4. Add Park and heapify
  5. Remove a particular park in which supply is stopped from the heap and heapify
  6. Max heap tree for each month
  7. Exit from the program
  """)
  user_option=int(input("Please enter one of the option number(1,2,3,4,5,6,7) here: ").strip())

  while user_option!=7:
    if user_option==1:
      # Option 1 -list all the parks belonging to heap unique value
      ListPark()
      print("List of parks - Output is available in outputPS11.txt")
      print("""
        1. List Parks
        2. Number of cycles across a month
        3. Park with maximum number of cycles in a given month
        4. Add Park and heapify
        5. Remove a particular park in which supply is stopped from the heap and heapify
        6. Max heap tree for each month
        7. Exit from the program
        """)
      user_option = int(input("Please enter one of the option number(1,2,3,4,5,6,7) here: ").strip())

    elif user_option==2:
      #Option 2- number of cycles across a month
      with open("outputPS11.txt", "a") as output_file:
        output_file.write("Number of cycles across different months:\n")
      cycles_per_month = []
      unique_months = []
      months = []
      for node in my_heap.heap:
        cycles = node[0]
        month = node[2]
        cycles_per_month.append(CyclesPerMonth(cycles, month))
        months.append(month)
    #getting cycles month-wise
      for item1 in months:
        if item1 not in unique_months:
          unique_months.append(item1)
      for item1 in unique_months:
        total_cycles = 0
        for item in cycles_per_month:
          if item1 == item.Month:
            total_cycles += item.NoOfCycles
        with open("outputPS11.txt", "a") as output_file:
          output_file.write(f"{item1} {total_cycles} \n")

        print("Number of cycles across different months - Output is available in outputPS11.txt")
        print("""
                1. List Parks
                2. Number of cycles across a month
                3. Park with maximum number of cycles in a given month
                4. Add Park and heapify
                5. Remove a particular park in which supply is stopped from the heap and heapify
                6. Max heap tree for each month
                7. Exit from the program
                """)
        user_option = int(input("Please enter one of the option number(1,2,3,4,5,6,7) here: ").strip())
    elif user_option == 3:
      #Option 3.Find  out  which  park  requires  the  maximum  number  of  cycles in a  given  month.
      # (Note: take  minimum10  to  12  parks  for each month)
      month_heap = MaxHeap()
      print("List of months in the input file:\n",",".join(ListMonth()))
      given_month=input("Enter the month name from the available list of months: ").strip()
      for entry in my_list:
        entry_cycles = entry[0]
        entry_park = entry[1]
        entry_month = entry[2]
        if entry_month == given_month:
           month_heap.heap_push((entry_cycles, entry_park, entry_month))
      #park with maximum number of cycles in the given month
      max_park = month_heap.heap_pop()  # it will pop the root node

      with open("outputPS11.txt", "a") as output_file:
        output_file.write(f"\nPark with Maximum Cycles\n")
        output_file.write(f"{max_park[1]}  holds maximum {max_park[0]} cycles in the given month {max_park[2]}\n\n")
      print(f"{max_park[1]}  holds maximum {max_park[0]} cycles in the given month {max_park[2]}\n\n")
      print("park with maximum number of cycles in the given month - Output is available in outputPS11.txt")
      print("""
                      1. List Parks
                      2. Number of cycles across a month
                      3. Park with maximum number of cycles in a given month
                      4. Add Park and heapify
                      5. Remove a particular park in which supply is stopped from the heap and heapify
                      6. Max heap tree for each month
                      7. Exit from the program
                      """)
      user_option = int(input("Please enter one of the option number(1,2,3,4,5,6,7) here: ").strip())
    elif user_option == 4:
      #Option 4 -Add new parks to the list of parks they are currently supplying to.
      with open("outputPS11.txt", "a") as output_file:
        output_file.write("Adding a new Park..\n\n")
      print("List of parks available before adding park\n", ",".join(ListPark()))
      new_park=input("Enter the name of new park..").strip().capitalize()
      #num_cycles=int(input("Enter the number of cycles for the new park to be added: ").strip())
      num_cycles=0
      name_month="to be added"
      new_item = ((num_cycles, new_park, name_month))
      #this will also heapify after adding
      my_heap.heap_push(new_item)
      print("List of parks available after adding a park\n", ",".join(ListPark()))
      print("Added new park.New list available in the output file")
      print("""
                            1. List Parks
                            2. Number of cycles across a month
                            3. Park with maximum number of cycles in a given month
                            4. Add Park and heapify
                            5. Remove a particular park in which supply is stopped from the heap and heapify
                            6. Max heap tree for each month
                            7. Exit from the program
                            """)
      user_option = int(input("Please enter one of the option number(1,2,3,4,5,6,7) here: ").strip())
    elif user_option == 5:
      #Option 5- Remove a particular park in which supply is stopped from the heap and heapify
      #create a new list excluding the park and heapify
      print("List of parks available before removing park\n",",".join(ListPark()))
      rem_park = input("Remove the existing park.Please pick park from the list of parks available:" )
      new_list = []
      for node in my_heap.heap:
        if rem_park not in node:
          new_list.append(node)
    #clear items from a current heap
      my_heap.heap.clear()
      for item in new_list:
        #again add items from the updated list
        my_heap.heap_push(item)
      with open("outputPS11.txt", "a") as output_file:
        output_file.write(f"Removing  park {rem_park}..\n\n")
      print("List of parks available after removing park \n",",".join(ListPark()))
      print("Removed the park.New list available in the output file")
      print("""
                                  1. List Parks
                                  2. Number of cycles across a month
                                  3. Park with maximum number of cycles in a given month
                                  4. Add Park and heapify
                                  5. Remove a particular park in which supply is stopped from the heap and heapify
                                  6. Max heap tree for each month
                                  7. Exit from the program
                                  """)
      user_option = int(input("Please enter one of the option number(1,2,3,4,5,6,7) here: ").strip())

    elif user_option == 6:
      #Option 6- Maximum Heap Tree for each Months
      #Make a new heap which has elements (cycle,park)
      #assume for 2022 and make heap with nodes as (month, aggregate)
      print("Max heap monthwise..output in output file")
      list_months=ListMonth()
      month_heap_list=[]
      for i in range(len(list_months)):
        month_heap_list.append(MaxHeap())

      list_of_month_heap = list(zip(list_months, month_heap_list))
      # print(list_of_month_heap)

      for i in range(len(list_of_month_heap)):
        for node in my_heap.heap:
            entry_cycles = node[0]
            entry_park = node[1]
            entry_month = node[2]
            if entry_month==list_of_month_heap[i][0]:
               list_of_month_heap[i][1].heap_push((entry_cycles,entry_park,entry_month))

      with open("outputPS11.txt", "a") as output_file:
        output_file.write("Max Heap for Each month..\n\n")

      for i in range(len(list_of_month_heap)):
        print(list_of_month_heap[i][1].heap)
        with open("outputPS11.txt", "a") as output_file:
          output_file.write(f"{list_of_month_heap[i][0]} --> {list_of_month_heap[i][1].heap}\n")

      print("""
                                        1. List Parks
                                        2. Number of cycles across a month
                                        3. Park with maximum number of cycles in a given month
                                        4. Add Park and heapify
                                        5. Remove a particular park in which supply is stopped from the heap and heapify
                                        6. Max heap tree for each month
                                        7. Exit from the program
                                        """)
      user_option = int(input("Please enter one of the option number(1,2,3,4,5,6,7) here: ").strip())

  else:
     print("Exiting the program..")
my_list = ReadFileWithExceptionHandling()
try:
  if my_list != None:
    MethodMain()
  else:
    print("Data unavailable...")
except Exception as e:
  print(e)
