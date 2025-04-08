# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Houssem Ferchichi (Student ID: 101344983) / Brett Patzer (Student ID: 101323409) / Nicole Chen (Student ID: 101343450) / Shawn Pye (Student ID: 101352512)"

# Update "" with your team (e.g. T102)
__team__ = "T-28"


#==========================================#
# Place your script for your batch_UI after this line
# You are allowed to create auxiliary functions
from load_data import load_data,add_average
from sort import sort
from curve_fit import curve_fit
from histogram import histogram

def batch_ui():
    """Executes a batch process based on commands stored in a text file.

    The function reads a text file containing a series of commands, seperated by ";" , executes each command, and processes data accordingly.
    Each command in the file is processed in sequence, and the following operations are supported:
    
    - 'L': Load data from a CSV file.
    - 'S': Sort the loaded data based on a selected attribute (e.g., Age, Failures, AvgGrade, or StudyTime) in either ascending or descending order.
    - 'C': Perform polynomial curve fitting on a specified attribute to predict AvgGrade.
    - 'H': Generate a histogram of a specified attribute.
    - 'E': Exit the program.

    Command syntax in the batch file should follow this format:
    - 'L' command: 'L;filename;attribute;value' where `filename` is the name of the CSV file, `attribute` is the attribute to filter by, and `value` is the filter value.
    - 'S' command: 'S;attribute;order;display' where `attribute` is the attribute to sort by, `order` is either 'A' (ascending) or 'D' (descending), and `display` is 'Y' or 'N' to indicate if the sorted data should be printed.
    - 'C' command: 'C;attribute;order' where `attribute` is the attribute to fit a curve to, and `order` is the polynomial order.
    - 'H' command: 'H;attribute' where `attribute` is the attribute to plot a histogram.
    - 'E' command: 'E' to exit the program.

    The function assumes the existence of helper functions:
    - `load_data()` and `add_average()` from `load_data` module
    - `sort()` from `sort` module
    - `curve_fit()` from `curve_fit` module
    - `histogram()` from `histogram` module

    If the batch file or individual commands cannot be processed due to missing files or incorrect syntax, appropriate error messages will be displayed.

    Precondition:

    Example:
    Please enter the name of the file where your commands are stored:
    >>> commands.txt
    Data loaded.
    List sorted.
    """
    data = []
    headers = []
    filename = input("Please enter the name of the file where your commands are stored: ")
    try:
        file = open(filename, 'r')
        for line in file:
            line = line.strip()
            if not line:
                break
            parts = line.split(';')
            command = parts[0].upper()

            if command == 'L':
                try:
                    filename = parts[1].upper()
                    file = open(filename, "r")
                    lines = file.readlines()
                    file.close()
                    headers = lines[0].strip().split(",")
                    data = [line.strip().split(",") for line in lines[1:]]
                except FileNotFoundError:
                    print("File not found. Please try again.")
                    continue
                attribute = parts[2]
                if attribute.lower() != "all":
                    if attribute not in headers:
                        print("Invalid attribute. Please try again.")
                        continue
                    value = parts[3].upper()
                    index = headers.index(attribute)
                    data = [row for row in data if row[index] == value]
                else:
                    value = parts[3].upper()
                if data:
                    data = load_data(filename,{attribute:value})
                    data = add_average(data)
                    print("Data loaded.")
                    #print(data)
                else:
                    print("No data found with the given filter.")
            elif command == 'S':
                if not data:
                    print("File not loaded. Please, load a file first.")
                    continue
                attribute = parts[1]
                if attribute not in ['Age', 'Failures', 'AvgGrade', 'StudyTime']:
                    print("Invalid attribute. Please try again.")
                    continue
                order = parts[2].upper()
                if order != 'A' and order != 'D':
                    print("Invalid Command.")
                    continue
                sort(data,order,attribute)
                display = parts[3].upper()
                print("List sorted.")
                if display == 'Y':
                    print(data)
            elif command == 'C':
                if not data:
                    print("File not loaded. Please, load a file first.")
                    continue
                attribute = parts[1]
                if attribute not in headers:
                    print("Invalid attribute. Please try again.")
                    continue
                order = parts[2]
                print(curve_fit(data,attribute,order))
            elif command == 'H':
                if not data:
                    print("File not loaded. Please, load a file first.")
                    continue
                attribute = parts[1]
                if attribute not in headers:
                    print("Invalid attribute. Please try again.")
                    continue
                histogram(data,attribute)
            elif command == 'E':
                print("Exiting program.")
                break
            else:
                print("Invalid command.")
        file.close()
    except FileNotFoundError:
        print("Error: File not found")


# Run the function

batch_ui()