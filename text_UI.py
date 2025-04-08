# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Houssem Ferchichi (Student ID: 101344983) / Brett Patzer (Student ID: 101323409) / Nicole Chen (Student ID: 101343450) / Shawn Pye (Student ID: 101352512)"

# Update "" with your team (e.g. T102)
__team__ = "T-28"


#==========================================#
# Place your script for your text_UI after this line
# You are allowed to create auxiliary functions
from load_data import load_data,add_average
from sort import sort
from curve_fit import curve_fit
from histogram import histogram

def Text_UI():
    """Launches a text-based user interface for interacting with student performance data.

    This function provides the following options via a command-line menu:
    - L)oad Data: Load data from a specified CSV file and apply optional filtering based on a selected attribute.
    - S)ort Data: Sort the loaded data based on selected numeric attributes such as Age, Failures, AvgGrade, or StudyTime.
    - C)urve Fit: Fit a polynomial curve to predict AvgGrade based on a chosen attribute and polynomial order.
    - H)istogram: Plot a histogram for the selected attribute using the current dataset.
    - E)xit: Exit the program.

    The function assumes access to helper functions to either calculate or show the data according to user's needs:
    - `load_data()` and `add_average()` from `load_data` module
    - `sort()` from `sort` module
    - `curve_fit()` from `curve_fit` module
    - `histogram()` from `histogram` module

    Precondition:

    Example:
    >>> Text_UI()
    L)oad Data
    S)ort Data
    C)urve Fit
    H)istogram
    E)xit
    Please type your command:
    >>> L
    Please enter the name of the file:
    >>> student-test.csv
    Please enter the attribute to use as a filter:
    >>> School
    Please enter the value of the attribute:
    >>> GP
    Data loaded.
    
    L)oad Data
    S)ort Data
    C)urve Fit
    H)istogram
    E)xit
    Please type your command:
    >>> S
    Please enter the attribute you want to use for sorting:
    'Age', 'Failures', 'AvgGrade', 'StudyTime':
    >>> Age
    Ascending (A) or Descending (D) order:
    >>> A
    Do you want to display the data? (Y/N):
    >>> N
    List Sorted.

    L)oad Data
    S)ort Data
    C)urve Fit
    H)istogram
    E)xit
    Please type your command:
    >>> E
    Exiting program.
    """
    data = []
    headers = []
    while True:
        print("\nL)oad Data")
        print("S)ort Data")
        print("C)urve Fit")
        print("H)istogram")
        print("E)xit")
        print("Please type your command:", end=' ')
        command = input().upper()
        if command == 'L':
            filename = input("Please enter the name of the file: ")
            try:
                file = open(filename, "r")
                lines = file.readlines()
                file.close()
                headers = lines[0].strip().split(",")
                data = [line.strip().split(",") for line in lines[1:]]
            except FileNotFoundError:
                print("File not found. Please try again.")
                continue
            attribute = input("Please enter the attribute to use as a filter: ")
            if attribute.lower() != "all":
                if attribute not in headers:
                    print("Invalid attribute. Please try again.")
                    continue
                value = input("Please enter the value of the attribute: ")
                index = headers.index(attribute)
                data = [row for row in data if row[index] == value]
            else:
                value = 999
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
            attribute = input("Please enter the attribute you want to use for sorting: \n'Age', 'Failures', 'AvgGrade', 'StudyTime': ")
            if attribute not in ['Age', 'Failures', 'AvgGrade', 'StudyTime']:
                print("Invalid attribute. Please try again.")
                continue
            order = input("Ascending (A) or Descending (D) order: ").upper()
            if order != 'A' and order != 'D':
                print("Invalid Command.")
                continue
            sort(data,order,attribute)
            display = input("Do you want to display the data? (Y/N): ").upper()
            print("List sorted.")
            if display == 'Y':
                print(data)
        elif command == 'C':
            if not data:
                print("File not loaded. Please, load a file first.")
                continue
            attribute = input("Please enter the attribute you want to use to find the best fit for AvgGrade: ")
            if attribute not in headers:
                print("Invalid attribute. Please try again.")
                continue
            order = int(input("Please enter the order of the polynomial to be fitted: "))
            print(curve_fit(data,attribute,order))
        elif command == 'H':
            if not data:
                print("File not loaded. Please, load a file first.")
                continue
            attribute = input("Please enter the attribute you want to use for plotting: ")
            if attribute not in headers:
                print("Invalid attribute. Please try again.")
                continue
            histogram(data,attribute)
        elif command == 'E':
            print("Exiting program.")
            break
        else:
            print("Invalid command.")
Text_UI()