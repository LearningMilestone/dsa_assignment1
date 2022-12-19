import heapq

# Dictionary to store the number of cycles required at each park
cycles_per_park = {}

# Read the input data from the input file
with open("inputPS11.txt") as input_file:
    for line in input_file:
        # Split the line into park name, number of cycles, and month

        park, cycles, month = line.strip().split(",")
        print(park.strip(), cycles.strip(), month.strip())
        #         # Convert the number of cycles to an integer
        cycles = int(cycles.strip())
        #         # Add the data to the dictionary
        cycles_per_park[park] = (cycles, month)
    # print(cycles_per_park)

# # Dictionary to store the total number of cycles required per month
cycles_per_month = {}

# # Iterate through the values in the dictionary
for park, (cycles, month) in cycles_per_park.items():
    # Check if the month is already in the dictionary
    if month in cycles_per_month:
        # Update the total number of cycles for the month
        cycles_per_month[month] += cycles
    else:
        # Add the month to the dictionary with the total number of cycles
        cycles_per_month[month] = cycles

# # Open the output file for writing
with open("outputPS11.txt", "w") as output_file:
    # Generate a list of all cycling parks
    cycling_parks = list(cycles_per_park.keys())
    output_file.write("List of cycling parks:\n")
    output_file.write(", ".join(cycling_parks) + "\n")

    #     # Calculate the total number of cycles required per month
    output_file.write("Total number of cycles required per month:\n")
    for month, cycles in cycles_per_month.items():
        output_file.write(f"{month} {cycles}\n")

    # # Find the park with the maximum number of cycles in each month
    # for month, cycles in cycles_per_month.items():
    #     # Create a heap with the number of cycles required at each park
    #     park_heap = [(cycles, park) for park, (cycles, park_month) in cycles_per_park.items() if park_month == month]
    #     heapq.heapify(park_heap)
    #     # Find the park with the maximum number of cycles
    #     max_cycles, max_park = heapq.heappop(park_heap)
    #     output_file.write(f"{max_park} requires maximum {max_cycles} cycles in the month of {month}\n")
    #
    # #     # Add new parks to the list
    # output_file.write("Adding new parks:\n")
    # cycles_per_park["Park11"] = (70, "May2022")
    # cycles_per_park["Park11"] = (85, "June2022")
    # cycles_per_park["Park12"] = (50, "June2022")
    # cycles_per_park["Park12"] = (60, "June2022")
    # output_file.write("Done.\n")

#     # Remove a park from the list
# output_file.write("Removing a park:\n")
# del cycles_per_park["park9"]
# del cycles_per_park