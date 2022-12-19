cycles_per_park = {}
cycles_per_month = {}

def ReadInputFile():
    # do exception handing for reading file here
    with open("inputPS11.txt") as input_file:
        for line in input_file:
            # Split the line into park name, number of cycles, and month
            park, cycles, month = line.strip().split(",")
            #print(park.strip(), cycles.strip(), month.strip())
            # Convert the number of cycles to an integer
            cycles = int(cycles.strip())
            # Add the data to the dictionary
            cycles_per_park[park] = (cycles, month)


#output list of parks
def ListAllParks():
    global cycles_per_park
    ReadInputFile()
    #exception handling required here
    with open("outputPS11.txt", "w") as output_file:
        # Generate a list of all cycling parks
        cycling_parks = list(cycles_per_park.keys())
        output_file.write("List of cycling parks:\n")
        output_file.write(", ".join(cycling_parks) + "\n")


def GetCyclesPerMonth():
    for park, (cycles, month) in cycles_per_park.items():
        # Check if the month is already in the dictionary
        if month in cycles_per_month:
            # Update the total number of cycles for the month
            cycles_per_month[month] += cycles
        else:
            # Add the month to the dictionary with the total number of cycles
            cycles_per_month[month] = cycles

    # Open the output file for writing
    # exception handling required here
    with open("outputPS11.txt", "w") as output_file:
        # Generate a list of all cycling parks
        cycling_parks = list(cycles_per_park.keys())
        output_file.write("List of cycling parks:\n")
        output_file.write(", ".join(cycling_parks) + "\n")
        # Calculate the total number of cycles required per month
        output_file.write("Total number of cycles required per month:\n")
        for month, cycles in cycles_per_month.items():
            output_file.write(f"{month} {cycles}\n")



ListAllParks()
GetCyclesPerMonth()