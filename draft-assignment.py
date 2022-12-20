import heapq
import os
parent_list=[]
park_list=[]
cycles_per_month = {}

#clean output file
with open("outputPS11.txt", "w") as output_file:
    output_file.write("****************PS11 Output File***************\n\n")

#Read data from the input file
def ReadInputFile():
    global parent_list
    # do exception handing for reading file here
    with open("inputPS11.txt") as input_file:
        for line in input_file:
            # Split the line into park name, number of cycles, and month
            #exception handling for missing data
            park, cycles, month = line.strip().split(",")
            # Convert the number of cycles to an integer
            #exception handling for invalid/missing data
            cycles = int(cycles.strip())
            month=month.strip()
            park=park.strip()
            parent_list.append((park,month,cycles))


# #Problem : Query 1- Generate a list of all cycling parks the startup is currently supplying cycles to.
#no heap generation here
def ListAllParks():
    global parent_list
    global park_list
    ReadInputFile()
    for entry in parent_list:
        park=entry[0]
        park_list.append(park)
        #generate unique values
        park_list=list(set(park_list))
    print(park_list)
    #file exception handling
    with open("outputPS11.txt", "a") as output_file:
        output_file.write("List of cycling parks:\n")
        output_file.write(", ".join(park_list) + "\n")
        output_file.write("\n\n")

#Problem- Query 2- Calculate the total number of cycles required across all parks per month.
#no heap here..
def GetCyclesPerMonth():
    global cycles_per_month
    for entry in parent_list:
        cycles = entry[2]
        month=entry[1]
        #getting cycles month-wise
        if month in cycles_per_month:
            # Update the total number of cycles for the month
            cycles_per_month[month] += cycles
        else:
            # Add the month to the dictionary with the total number of cycles
            cycles_per_month[month] = cycles
    print(cycles_per_month)
    #adding to putput
    with open("outputPS11.txt", "a") as output_file:
       # Calculate the total number of cycles required per month across all the parks
        output_file.write("Total number of cycles required per month:\n")
        for month, cycles in cycles_per_month.items():
            output_file.write(f"{month} {cycles}\n")
        output_file.write("\n\n")
#
# Problem- Query 3- Find out which park requires the maximum number of cycles in a given month.
# # (Note: take minimum 10 to 12 parks for each month)
# #Here we need to heapify data with max heap
#
def heapifyPark():
    #take user input here
    #given_month=input("Enter Park:")
    given_month = "May2022"
    park_heap=[]
    for entry in parent_list:
        entry_park=entry[0]
        entry_month=entry[1]
        entry_cycles = entry[2]
        if entry_month == given_month:
            #to heapify tuple value should come first
            park_heap.append((entry_cycles,entry_park,entry_month))

    print(park_heap)
    #heapify park_heap list
    heapq._heapify_max(park_heap)
    print(park_heap)

    #find the park with maximum cycles in the given month
    park_max=heapq._heappop_max(park_heap)
    #print(f"Park with maximum number of cycles for the given month of {given_month}: is {park_max[1]} with {park_max[0]} cycles")
    with open("outputPS11.txt", "a") as output_file:
       # Calculate the total number of cycles required per month across all the parks
        output_file.write(f"Park with maximum number of cycles for the given month of {given_month}: is "
                          f"{park_max[1]} with {park_max[0]} cycles\n\n")

#Add new parks to the list of parks they are currently supplying to.
def AddPark(park,cycles,month):
    #print("Add Park",park)
    #do exception handling
    ##Action --add heappush and add new data entered by the user
    with open("inputPS11.txt", "a") as input_file:
        input_file.write(f"\n{park},{cycles},{month}")

#Remove a park from the list if the startup has stopped supplying cycles to that park.
def RemovePark(park):
    #print("Removing Park if exists..",park)
    ##Action --add function to remove particular node as per data entered by the user
    with open(r"inputPS11.txt") as f, open(r"workfile.txt", "w") as working:
        for line in f:
            if park not in line:
                working.write(line)
    os.remove(r"inputPS11.txt")
    os.rename(r"workfile.txt", r"inputPS11.txt")


#Print max-heap tree for each month

ListAllParks()
GetCyclesPerMonth()
heapifyPark()
##we can also take user input here
AddPark(park="park14",cycles=30,month="May2022")
AddPark(park="park12",cycles=80,month="June2022")
RemovePark("park14")
ListAllParks()
heapifyPark()

