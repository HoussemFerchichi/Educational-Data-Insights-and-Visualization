# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Houssem Ferchichi (Student ID: 101344983) / Brett Patzer (Student ID: 101323409) / Nicole Chen (Student ID: 101343450) / Shawn Pye (Student ID: 101352512)"

# Update "" with your team (e.g. T102)
__team__ = "T-28"




#==========================================#
# Place your student_school_list function after this line
def student_school_list(file_name: str, school: str) -> list[dict[str, str]]:
    """return a list of dictionaries where each dictionary represents a student and their corresponding details excluding the school field by reading a CSV file from a given file_name and filtering students by a given school.

    Precondition: (len(file_name)) > 4 and (".csv" in file_name) and len(school) == 2
    

    >>> students = student_school_list("student-mat.csv","MS")
    >>> len(students)
    76
    >>> students[0]
    {'ID': 320, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 11, 'WinterGrade': 11}

    
    >>> students = student_school_list("student-mat.csv","GP")
    >>> len(students)
    79
    >>> students[0]
    {'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}


    >>> students = student_school_list("student-mat.csv","XX")
    >>> len(students)
    0
    >>> students
    []

    >>> student_school_list("student-mat.csv","MS")
    [{'ID': 320, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 11, 'WinterGrade': 11}, {'ID': 321, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 23, 'FallGrade': 13, 'WinterGrade': 13}, {'ID': 322, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'FallGrade': 11, 'WinterGrade': 9}, {'ID': 323, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 3, 'FallGrade': 11, 'WinterGrade': 11}, {'ID': 324, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 1, 'FallGrade': 12, 'WinterGrade': 14}, {'ID': 325, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 2, 'Absences': 0, 'FallGrade': 16, 'WinterGrade': 15}, {'ID': 326, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 3, 'FallGrade': 9, 'WinterGrade': 12}, {'ID': 327, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 5, 'Absences': 3, 'FallGrade': 14, 'WinterGrade': 15}, {'ID': 328, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 4, 'Absences': 8, 'FallGrade': 11, 'WinterGrade': 10}, {'ID': 329, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 7, 'FallGrade': 10, 'WinterGrade': 9}, {'ID': 330, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'FallGrade': 14, 'WinterGrade': 14}, {'ID': 331, 'Age': 18, 'StudyTime': 4.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}, {'ID': 332, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 14}, {'ID': 333, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 4, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 0}, {'ID': 334, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 2, 'Absences': 0, 'FallGrade': 8, 'WinterGrade': 8}, {'ID': 335, 'Age': 18, 'StudyTime': 4.0, 'Failures': 0, 'Health': 4, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 9}, {'ID': 336, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 16, 'FallGrade': 16, 'WinterGrade': 15}, {'ID': 337, 'Age': 19, 'StudyTime': 3.0, 'Failures': 1, 'Health': 5, 'Absences': 12, 'FallGrade': 14, 'WinterGrade': 13}, {'ID': 338, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 2, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 8}, {'ID': 339, 'Age': 18, 'StudyTime': 4.0, 'Failures': 0, 'Health': 1, 'Absences': 7, 'FallGrade': 16, 'WinterGrade': 15}, {'ID': 340, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 2, 'Absences': 4, 'FallGrade': 9, 'WinterGrade': 10}, {'ID': 341, 'Age': 19, 'StudyTime': 3.0, 'Failures': 1, 'Health': 3, 'Absences': 4, 'FallGrade': 11, 'WinterGrade': 12}, {'ID': 342, 'Age': 18, 'StudyTime': 2.0, 'Failures': 1, 'Health': 2, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 10}, {'ID': 343, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 11, 'FallGrade': 16, 'WinterGrade': 15}, {'ID': 344, 'Age': 17, 'StudyTime': 2.0, 'Failures': 1, 'Health': 4, 'Absences': 0, 'FallGrade': 9, 'WinterGrade': 8}, {'ID': 345, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'FallGrade': 11, 'WinterGrade': 10}, {'ID': 346, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 1, 'Absences': 7, 'FallGrade': 13, 'WinterGrade': 13}, {'ID': 347, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 9, 'FallGrade': 16, 'WinterGrade': 15}, {'ID': 348, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 10}, {'ID': 349, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 0, 'FallGrade': 13, 'WinterGrade': 15}, {'ID': 350, 'Age': 18, 'StudyTime': 1.0, 'Failures': 1, 'Health': 5, 'Absences': 10, 'FallGrade': 11, 'WinterGrade': 13}, {'ID': 351, 'Age': 19, 'StudyTime': 2.0, 'Failures': 3, 'Health': 2, 'Absences': 8, 'FallGrade': 8, 'WinterGrade': 7}, {'ID': 352, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'FallGrade': 13, 'WinterGrade': 13}, {'ID': 353, 'Age': 18, 'StudyTime': 1.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 8, 'WinterGrade': 7}, {'ID': 354, 'Age': 19, 'StudyTime': 1.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'FallGrade': 8, 'WinterGrade': 8}, {'ID': 355, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 2, 'Absences': 4, 'FallGrade': 13, 'WinterGrade': 11}, {'ID': 356, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 9}, {'ID': 357, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 4, 'FallGrade': 12, 'WinterGrade': 13}, {'ID': 358, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 12, 'WinterGrade': 12}, {'ID': 359, 'Age': 18, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'FallGrade': 10, 'WinterGrade': 10}, {'ID': 360, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 0, 'FallGrade': 18, 'WinterGrade': 16}, {'ID': 361, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 0, 'FallGrade': 13, 'WinterGrade': 13}, {'ID': 362, 'Age': 18, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 2, 'FallGrade': 13, 'WinterGrade': 12}, {'ID': 363, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 0, 'FallGrade': 11, 'WinterGrade': 11}, {'ID': 364, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 1, 'Absences': 0, 'FallGrade': 16, 'WinterGrade': 15}, {'ID': 365, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 0, 'FallGrade': 12, 'WinterGrade': 11}, {'ID': 366, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'FallGrade': 10, 'WinterGrade': 10}, {'ID': 367, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 0, 'FallGrade': 13, 'WinterGrade': 13}, {'ID': 368, 'Age': 17, 'StudyTime': 1.0, 'Failures': 1, 'Health': 1, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 6}, {'ID': 369, 'Age': 18, 'StudyTime': 1.0, 'Failures': 0, 'Health': 4, 'Absences': 0, 'FallGrade': 11, 'WinterGrade': 10}, {'ID': 370, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 10, 'FallGrade': 14, 'WinterGrade': 12}, {'ID': 371, 'Age': 19, 'StudyTime': 2.0, 'Failures': 2, 'Health': 3, 'Absences': 4, 'FallGrade': 7, 'WinterGrade': 7}, {'ID': 372, 'Age': 18, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 3, 'FallGrade': 14, 'WinterGrade': 12}, {'ID': 373, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 8, 'FallGrade': 13, 'WinterGrade': 11}, {'ID': 374, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 1, 'Absences': 14, 'FallGrade': 6, 'WinterGrade': 5}, {'ID': 375, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 1, 'Absences': 0, 'FallGrade': 19, 'WinterGrade': 18}, {'ID': 376, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 2, 'FallGrade': 8, 'WinterGrade': 8}, {'ID': 377, 'Age': 20, 'StudyTime': 3.0, 'Failures': 2, 'Health': 3, 'Absences': 4, 'FallGrade': 15, 'WinterGrade': 14}, {'ID': 378, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 2, 'Absences': 4, 'FallGrade': 8, 'WinterGrade': 9}, {'ID': 379, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 1, 'Absences': 0, 'FallGrade': 15, 'WinterGrade': 15}, {'ID': 380, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 1, 'Absences': 17, 'FallGrade': 10, 'WinterGrade': 10}, {'ID': 381, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 2, 'Absences': 4, 'FallGrade': 15, 'WinterGrade': 14}, {'ID': 382, 'Age': 18, 'StudyTime': 1.0, 'Failures': 0, 'Health': 5, 'Absences': 5, 'FallGrade': 7, 'WinterGrade': 6}, {'ID': 383, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'FallGrade': 11, 'WinterGrade': 11}, {'ID': 384, 'Age': 19, 'StudyTime': 1.0, 'Failures': 1, 'Health': 5, 'Absences': 0, 'FallGrade': 6, 'WinterGrade': 5}, {'ID': 385, 'Age': 18, 'StudyTime': 1.0, 'Failures': 1, 'Health': 3, 'Absences': 14, 'FallGrade': 6, 'WinterGrade': 5}, {'ID': 386, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 2, 'FallGrade': 10, 'WinterGrade': 9}, {'ID': 387, 'Age': 18, 'StudyTime': 1.0, 'Failures': 0, 'Health': 5, 'Absences': 7, 'FallGrade': 6, 'WinterGrade': 5}, {'ID': 388, 'Age': 19, 'StudyTime': 3.0, 'Failures': 1, 'Health': 5, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 5}, {'ID': 389, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 1, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 9}, {'ID': 390, 'Age': 18, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 0, 'FallGrade': 6, 'WinterGrade': 5}, {'ID': 391, 'Age': 20, 'StudyTime': 2.0, 'Failures': 2, 'Health': 4, 'Absences': 11, 'FallGrade': 9, 'WinterGrade': 9}, {'ID': 392, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 2, 'Absences': 3, 'FallGrade': 14, 'WinterGrade': 16}, {'ID': 393, 'Age': 21, 'StudyTime': 1.0, 'Failures': 3, 'Health': 3, 'Absences': 3, 'FallGrade': 10, 'WinterGrade': 8}, {'ID': 394, 'Age': 18, 'StudyTime': 1.0, 'Failures': 0, 'Health': 5, 'Absences': 0, 'FallGrade': 11, 'WinterGrade': 12}, {'ID': 395, 'Age': 19, 'StudyTime': 1.0, 'Failures': 0, 'Health': 5, 'Absences': 5, 'FallGrade': 8, 'WinterGrade': 9}]

    """
    # Get the index of StudyTime by searching and storing the index of first float element and exiting the loop to save memory usage and runtime (StudyTime is the only float element assuming like instructed that the data is in the correct format).
    # We implemented this method for the reason that the file can contain StudyTime value as an int so we can't convert it depending on the type it was stored in and assuming that the key could have a different name and index each time we need to fetch it dynamically.
    try:
        file = open(file_name,"r")
    except:
        print("Invalid File Name")
        return []
    studytime_index = -1
    for line in file:
        keys = line.strip().split(",")
        for item in keys:
            try:
                if (item.index(".")>-1) and str(float(item)) == str(item): # checking if the item is a float .
                    studytime_index = keys.index(item) 
                    break   # Saving the list index of the first float element and breaking out of the loop.
            except:studytime_index = -1 # Pass the Statement if we got any non float items (we're not sure if we can use Pass).
        if studytime_index != -1 : break # Breaking out of the loop for the first float found with its index saved in studytime_index.
    file.close()
    # Closing and re-opening the file to reset the pointer as we can't use seek().
    file = open(file_name,"r")
    # Initializing the filter_key and the filter_str(value) that we're only saving the students with those conditions.
    filter_key = "School"
    filter_str = str(school)
    # Going through the file and breaking after the first line which contains the header and we save it into a list to create the dictionary with the names in the list
    for line in file:
        keys = line.strip().split(",")
        break
    # Filtering and saving the students according to their school. 
    data=[]
    for line in file:
        header = {key : list for key in keys} # Creating the dictionary with the list keys assigning each key value to a new item with the key name from the list keys and making sure it reset the dictionary each loop.
        values = line.strip().split(",") # Creating a list with no white spaces that contains the list values fetched from the file.
        if values[keys.index(filter_key)]==filter_str: # Condition to check if the current line we're pointing on in the file is meeting the conditions of our filter.
            for i in range(len(values)): # Looping through the values of the list.
                if i != keys.index(filter_key): # Making sure not to save the value for the key that we're filtering to save memory.
                    # Saving the values with their correct data type if it's study time then save it as a float otherwise try to save it as an it if it failed then save it as a string
                    try:
                        if i == studytime_index :header[keys[i]]=float(values[i])
                        else : header[keys[i]]=int(values[i])
                    except : header[keys[i]]=values[i]
            header.pop(filter_key) # Removing the item that we filtered with.
            data.append(header) # Add the data saved from the dictionary into a new item into the data list
    # Closing the file and returning the filtered students
    file.close()
    return data


#==========================================#
# Place your student_health_list function after this line
def student_health_list(file_name: str, health: int) -> list[dict[str, str]]:
    """return a list of dictionaries where each dictionary represents a student and their corresponding details excluding the health field by reading a CSV file from a given file_name and filtering students by a given health.

    Precondition: (len(file_name)) > 4 and (".csv" in file_name) and health >= 1 and health <=5
    

    >>> students = student_health_list("student-mat.csv",1)
    >>> len(students)
    47
    >>> students[0]
    {'School': 'GP', 'ID': 8, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'FallGrade': 6, 'WinterGrade': 5}

    
    >>> students = student_health_list("student-mat.csv",5)
    >>> len(students)
    146
    >>> students[0]
    {'School': 'GP', 'ID': 4, 'Age': 15, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 2, 'FallGrade': 15, 'WinterGrade': 14}


    >>> students = student_health_list("student-mat.csv",2)
    >>> len(students)
    45
    >>> student_health_list("student-mat.csv",2)
    [{'School': 'GP', 'ID': 11, 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 8}, {'School': 'GP', 'ID': 16, 'Age': 16, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 14, 'WinterGrade': 14}, {'School': 'GP', 'ID': 17, 'Age': 16, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 6, 'FallGrade': 13, 'WinterGrade': 14}, {'School': 'GP', 'ID': 34, 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 8, 'WinterGrade': 10}, {'School': 'GP', 'ID': 40, 'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 8, 'FallGrade': 14, 'WinterGrade': 13}, {'School': 'GP', 'ID': 48, 'Age': 16, 'StudyTime': 4.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 19, 'WinterGrade': 19}, {'School': 'GP', 'ID': 56, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 8, 'FallGrade': 8, 'WinterGrade': 9}, {'School': 'GP', 'ID': 65, 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 10}, {'School': 'MB', 'ID': 87, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 8, 'WinterGrade': 7}, {'School': 'MB', 'ID': 93, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 7, 'WinterGrade': 6}, {'School': 'MB', 'ID': 104, 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 26, 'FallGrade': 7, 'WinterGrade': 6}, {'School': 'MB', 'ID': 112, 'Age': 16, 'StudyTime': 3.0, 'Failures': 1, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 10}, {'School': 'MB', 'ID': 117, 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 2, 'FallGrade': 11, 'WinterGrade': 13}, {'School': 'MB', 'ID': 142, 'Age': 16, 'StudyTime': 1.0, 'Failures': 2, 'Absences': 8, 'FallGrade': 9, 'WinterGrade': 9}, {'School': 'CF', 'ID': 164, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 2, 'FallGrade': 10, 'WinterGrade': 10}, {'School': 'CF', 'ID': 166, 'Age': 16, 'StudyTime': 1.0, 'Failures': 1, 'Absences': 16, 'FallGrade': 12, 'WinterGrade': 11}, {'School': 'CF', 'ID': 171, 'Age': 16, 'StudyTime': 1.0, 'Failures': 2, 'Absences': 0, 'FallGrade': 6, 'WinterGrade': 5}, {'School': 'CF', 'ID': 180, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 10, 'WinterGrade': 10}, {'School': 'CF', 'ID': 191, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 10, 'FallGrade': 11, 'WinterGrade': 12}, {'School': 'CF', 'ID': 199, 'Age': 17, 'StudyTime': 1.0, 'Failures': 1, 'Absences': 24, 'FallGrade': 18, 'WinterGrade': 18}, {'School': 'CF', 'ID': 201, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 2, 'FallGrade': 16, 'WinterGrade': 16}, {'School': 'CF', 'ID': 233, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 14, 'FallGrade': 11, 'WinterGrade': 9}, {'School': 'CF', 'ID': 236, 'Age': 16, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 10, 'FallGrade': 11, 'WinterGrade': 9}, {'School': 'BD', 'ID': 240, 'Age': 18, 'StudyTime': 2.0, 'Failures': 1, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 7}, {'School': 'BD', 'ID': 247, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 12, 'WinterGrade': 12}, {'School': 'BD', 'ID': 252, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'FallGrade': 7, 'WinterGrade': 10}, {'School': 'BD', 'ID': 260, 'Age': 17, 'StudyTime': 4.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 9}, {'School': 'BD', 'ID': 261, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 21, 'FallGrade': 17, 'WinterGrade': 18}, {'School': 'BD', 'ID': 272, 'Age': 18, 'StudyTime': 4.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 15, 'WinterGrade': 14}, {'School': 'BD', 'ID': 287, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 5, 'FallGrade': 18, 'WinterGrade': 18}, {'School': 'BD', 'ID': 289, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 6, 'FallGrade': 15, 'WinterGrade': 14}, {'School': 'BD', 'ID': 290, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 9, 'FallGrade': 15, 'WinterGrade': 13}, {'School': 'BD', 'ID': 297, 'Age': 19, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 9}, {'School': 'BD', 'ID': 298, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 10, 'FallGrade': 10, 'WinterGrade': 8}, {'School': 'BD', 'ID': 312, 'Age': 19, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 20, 'FallGrade': 14, 'WinterGrade': 12}, {'School': 'MS', 'ID': 325, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 16, 'WinterGrade': 15}, {'School': 'MS', 'ID': 334, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 8, 'WinterGrade': 8}, {'School': 'MS', 'ID': 338, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 8}, {'School': 'MS', 'ID': 340, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 9, 'WinterGrade': 10}, {'School': 'MS', 'ID': 342, 'Age': 18, 'StudyTime': 2.0, 'Failures': 1, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 10}, {'School': 'MS', 'ID': 351, 'Age': 19, 'StudyTime': 2.0, 'Failures': 3, 'Absences': 8, 'FallGrade': 8, 'WinterGrade': 7}, {'School': 'MS', 'ID': 355, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 13, 'WinterGrade': 11}, {'School': 'MS', 'ID': 378, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 8, 'WinterGrade': 9}, {'School': 'MS', 'ID': 381, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 15, 'WinterGrade': 14}, {'School': 'MS', 'ID': 392, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 3, 'FallGrade': 14, 'WinterGrade': 16}]
    """
    # Get the index of StudyTime by searching and storing the index of first float element and exiting the loop to save memory usage and runtime (StudyTime is the only float element assuming like instructed that the data is in the correct format).
    # We implemented this method for the reason that the file can contain StudyTime value as an int so we can't convert it depending on the type it was stored in and assuming that the key could have a different name and index each time we need to fetch it dynamically.
    try:
        file = open(file_name,"r")
    except:
        print("Invalid File Name")
        return []
    studytime_index = -1
    for line in file:
        keys = line.strip().split(",")
        for item in keys:
            try:
                if (item.index(".")>-1) and str(float(item)) == str(item): # checking if the item is a float .
                    studytime_index = keys.index(item) 
                    break   # Saving the list index of the first float element and breaking out of the loop.
            except:studytime_index = -1 # Pass the Statement if we got any non float items (we're not sure if we can use Pass).
        if studytime_index != -1 : break # Breaking out of the loop for the first float found with its index saved in studytime_index.
    file.close()
    # Closing and re-opening the file to reset the pointer as we can't use seek().
    file = open(file_name,"r")
    # Initializing the filter_key and the filter_str(value) that we're only saving the students with those conditions.
    filter_key = "Health"
    filter_str = str(health)
    # Going through the file and breaking after the first line which contains the header and we save it into a list to create the dictionary with the names in the list
    for line in file:
        keys = line.strip().split(",")
        break
    # Filtering and saving the students according to their health. 
    data=[]
    for line in file:
        header = {key : list for key in keys} # Creating the dictionary with the list keys assigning each key value to a new item with the key name from the list keys and making sure it reset the dictionary each loop.
        values = line.strip().split(",") # Creating a list with no white spaces that contains the list values fetched from the file.
        if values[keys.index(filter_key)]==filter_str: # Condition to check if the current line we're pointing on in the file is meeting the conditions of our filter.
            for i in range(len(values)): # Looping through the values of the list.
                if i != keys.index(filter_key): # Making sure not to save the value for the key that we're filtering to save memory.
                    # Saving the values with their correct data type if it's study time then save it as a float otherwise try to save it as an it if it failed then save it as a string
                    try:
                        if i == studytime_index :header[keys[i]]=float(values[i])
                        else : header[keys[i]]=int(values[i])
                    except : header[keys[i]]=values[i]
            header.pop(filter_key) # Removing the item that we filtered with.
            data.append(header) # Add the data saved from the dictionary into a new item into the data list
    # Closing the file and returning the filtered students
    file.close()
    return data

#==========================================#
# Place your student_age_list function after this line
def student_age_list(file_name: str, age: int) -> list[dict[str, str]]:
    """return a list of dictionaries where each dictionary represents a student and their corresponding details excluding the age field by reading a CSV file from a given file_name and filtering students by a given age.

    Precondition: (len(file_name)) > 4 and (".csv" in file_name) and age >= 10 and age <= 25
    

    >>> students = student_age_list("student-mat.csv",15)
    >>> len(students)
    82
    >>> students[0]
    {'School': 'GP', 'ID': 3, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}

    
    >>> students = student_age_list("student-mat.csv",17)
    >>> len(students)
    98
    >>> students[0]
    {'School': 'GP', 'ID': 2, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4, 'FallGrade': 5, 'WinterGrade': 5}


    >>> students = student_age_list("student-mat.csv",23)
    >>> len(students)
    0
    >>> students
    []

    >>> students = student_age_list("student-mat.csv",20)
    >>> len(students)
    3
    >>> students
    [{'School': 'BD', 'ID': 307, 'StudyTime': 1, 'Failures': 0, 'Health': 5, 'Absences': 0, 'FallGrade': 17, 'WinterGrade': 18}, {'School': 'MS', 'ID': 377, 'StudyTime': 3, 'Failures': 2, 'Health': 3, 'Absences': 4, 'FallGrade': 15, 'WinterGrade': 14}, {'School': 'MS', 'ID': 391, 'StudyTime': 2, 'Failures': 2, 'Health': 4, 'Absences': 11, 'FallGrade': 9, 'WinterGrade': 9}]
    """
    # Get the index of StudyTime by searching and storing the index of first float element and exiting the loop to save memory usage and runtime (StudyTime is the only float element assuming like instructed that the data is in the correct format).
    # We implemented this method for the reason that the file can contain StudyTime value as an int so we can't convert it depending on the type it was stored in and assuming that the key could have a different name and index each time we need to fetch it dynamically.
    try:
        file = open(file_name,"r")
    except:
        print("Invalid File Name")
        return []
    studytime_index = -1
    for line in file:
        keys = line.strip().split(",")
        for item in keys:
            try:
                if (item.index(".")>-1) and str(float(item)) == str(item): # checking if the item is a float .
                    studytime_index = keys.index(item) 
                    break   # Saving the list index of the first float element and breaking out of the loop.
            except:studytime_index = -1 # Pass the Statement if we got any non float items (we're not sure if we can use Pass).
        if studytime_index != -1 : break # Breaking out of the loop for the first float found with its index saved in studytime_index.
    file.close()
    # Closing and re-opening the file to reset the pointer as we can't use seek().
    file = open(file_name,"r")
    # Initializing the filter_key and the filter_str(value) that we're only saving the students with those conditions.
    filter_key = "Age"
    filter_str = str(age)
    # Going through the file and breaking after the first line which contains the header and we save it into a list to create the dictionary with the names in the list
    for line in file:
        keys = line.strip().split(",")
        break
    # Filtering and saving the students according to their age. 
    data=[]
    for line in file:
        header = {key : list for key in keys} # Creating the dictionary with the list keys assigning each key value to a new item with the key name from the list keys and making sure it reset the dictionary each loop.
        values = line.strip().split(",") # Creating a list with no white spaces that contains the list values fetched from the file.
        if values[keys.index(filter_key)]==filter_str: # Condition to check if the current line we're pointing on in the file is meeting the conditions of our filter.
            for i in range(len(values)): # Looping through the values of the list.
                if i != keys.index(filter_key): # Making sure not to save the value for the key that we're filtering to save memory.
                    # Saving the values with their correct data type if it's study time then save it as a float otherwise try to save it as an it if it failed then save it as a string
                    try:
                        if i == studytime_index :header[keys[i]]=float(values[i])
                        else : header[keys[i]]=int(values[i])
                    except : header[keys[i]]=values[i]
            header.pop(filter_key) # Removing the item that we filtered with.
            data.append(header) # Add the data saved from the dictionary into a new item into the data list
    # Closing the file and returning the filtered students
    file.close()
    return data
#==========================================#
# Place your student_failures_list function after this line
def student_failures_list(file_name: str, failures: int) -> list[dict[str, str]]:
    """return a list of dictionaries where each dictionary represents a student and their corresponding details excluding the failures field by reading a CSV file from a given file_name and filtering students by a given failures.

    Precondition: (len(file_name)) > 4 and (".csv" in file_name) and failures >= 0
    

    >>> students = student_failures_list("student-mat.csv",0)
    >>> len(students)
    312
    >>> students[0]
    {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}

    
    >>> students = student_failures_list("student-mat.csv",3)
    >>> len(students)
    16
    >>> students
    [{'School': 'GP', 'ID': 3, 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}, {'School': 'GP', 'ID': 19, 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 16, 'FallGrade': 6, 'WinterGrade': 5}, {'School': 'GP', 'ID': 79, 'Age': 17, 'StudyTime': 1.0, 'Health': 3, 'Absences': 2, 'FallGrade': 8, 'WinterGrade': 8}, {'School': 'MB', 'ID': 128, 'Age': 19, 'StudyTime': 2.0, 'Health': 5, 'Absences': 2, 'FallGrade': 7, 'WinterGrade': 8}, {'School': 'MB', 'ID': 145, 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'FallGrade': 5, 'WinterGrade': 0}, {'School': 'MB', 'ID': 147, 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 0, 'FallGrade': 6, 'WinterGrade': 7}, {'School': 'MB', 'ID': 150, 'Age': 15, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'FallGrade': 8, 'WinterGrade': 9}, {'School': 'MB', 'ID': 151, 'Age': 18, 'StudyTime': 1.0, 'Health': 4, 'Absences': 0, 'FallGrade': 6, 'WinterGrade': 5}, {'School': 'MB', 'ID': 154, 'Age': 19, 'StudyTime': 1.0, 'Health': 4, 'Absences': 0, 'FallGrade': 5, 'WinterGrade': 0}, {'School': 'MB', 'ID': 158, 'Age': 18, 'StudyTime': 1.0, 'Health': 4, 'Absences': 6, 'FallGrade': 9, 'WinterGrade': 8}, {'School': 'CF', 'ID': 165, 'Age': 17, 'StudyTime': 2.0, 'Health': 5, 'Absences': 0, 'FallGrade': 5, 'WinterGrade': 8}, {'School': 'CF', 'ID': 174, 'Age': 16, 'StudyTime': 2.0, 'Health': 3, 'Absences': 0, 'FallGrade': 8, 'WinterGrade': 7}, {'School': 'CF', 'ID': 207, 'Age': 16, 'StudyTime': 2.0, 'Health': 4, 'Absences': 5, 'FallGrade': 7, 'WinterGrade': 7}, {'School': 'BD', 'ID': 248, 'Age': 22, 'StudyTime': 1.0, 'Health': 1, 'Absences': 16, 'FallGrade': 6, 'WinterGrade': 8}, {'School': 'MS', 'ID': 351, 'Age': 19, 'StudyTime': 2.0, 'Health': 2, 'Absences': 8, 'FallGrade': 8, 'WinterGrade': 7}, {'School': 'MS', 'ID': 393, 'Age': 21, 'StudyTime': 1.0, 'Health': 3, 'Absences': 3, 'FallGrade': 10, 'WinterGrade': 8}]

    >>> students = student_failures_list("student-mat.csv",4)
    >>> len(students)
    0
    >>> students
    []
    """
    # Get the index of StudyTime by searching and storing the index of first float element and exiting the loop to save memory usage and runtime (StudyTime is the only float element assuming like instructed that the data is in the correct format).
    # We implemented this method for the reason that the file can contain StudyTime value as an int so we can't convert it depending on the type it was stored in and assuming that the key could have a different name and index each time we need to fetch it dynamically.
    try:
        file = open(file_name,"r")
    except:
        print("Invalid File Name")
        return []
    studytime_index = -1
    for line in file:
        keys = line.strip().split(",")
        for item in keys:
            try:
                if (item.index(".")>-1) and str(float(item)) == str(item): # checking if the item is a float .
                    studytime_index = keys.index(item) 
                    break   # Saving the list index of the first float element and breaking out of the loop.
            except:studytime_index = -1 # Pass the Statement if we got any non float items (we're not sure if we can use Pass).
        if studytime_index != -1 : break # Breaking out of the loop for the first float found with its index saved in studytime_index.
    file.close()
    # Closing and re-opening the file to reset the pointer as we can't use seek().
    file = open(file_name,"r")
    # Initializing the filter_key and the filter_str(value) that we're only saving the students with those conditions.
    filter_key = "Failures"
    filter_str = str(failures)
    # Going through the file and breaking after the first line which contains the header and we save it into a list to create the dictionary with the names in the list
    for line in file:
        keys = line.strip().split(",")
        break
    # Filtering and saving the students according to their failures. 
    data=[]
    for line in file:
        header = {key : list for key in keys} # Creating the dictionary with the list keys assigning each key value to a new item with the key name from the list keys and making sure it reset the dictionary each loop.
        values = line.strip().split(",") # Creating a list with no white spaces that contains the list values fetched from the file.
        if values[keys.index(filter_key)]==filter_str: # Condition to check if the current line we're pointing on in the file is meeting the conditions of our filter.
            for i in range(len(values)): # Looping through the values of the list.
                if i != keys.index(filter_key): # Making sure not to save the value for the key that we're filtering to save memory.
                    # Saving the values with their correct data type if it's study time then save it as a float otherwise try to save it as an it if it failed then save it as a string
                    try:
                        if i == studytime_index :header[keys[i]]=float(values[i])
                        else : header[keys[i]]=int(values[i])
                    except : header[keys[i]]=values[i]
            header.pop(filter_key) # Removing the item that we filtered with.
            data.append(header) # Add the data saved from the dictionary into a new item into the data list
    # Closing the file and returning the filtered students
    file.close()
    return data
#==========================================#
# Place your load_data function after this line
def load_data(file_name: str, dictfilter:dict) -> list:
    """return a list of dictionaries where each dictionary represents a student and their corresponding details excluding the row that we filtered with except with the filter All which returns everything no matter by reading a CSV file from a given file_name and filtering students by a given dictfilter.
    dictfilter: dictionary containing the key and the value that we will filter the students with.

    Precondtion: (len(file_name)) > 4 and (".csv" in file_name)

    >>> students = load_data("student-mat.csv",{'Failures':0})
    >>> len(students)
    312
    >>> students[0]
    {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}


    >>> students = load_data("student-mat.csv",{'Age':15})
    >>> len(students)
    82
    >>> students[0]
    {'School': 'GP', 'ID': 3, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}


    >>> students = load_data("student-mat.csv",{'Health':3})
    >>> len(students)
    91
    >>> students[0]
    {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}


    >>> students = load_data("student-mat.csv",{'School':"MS"})
    >>> len(students)
    76
    >>> students[0]
    {'ID': 320, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 11, 'WinterGrade': 11}

    
    >>> students = load_data("student-mat.csv",{'All':999})
    >>> len(students)
    395
    >>> students[0]
    {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}


    >>> load_data("student-mat.csv",{'SCHOOL':"MS"})
    Invalid Value
    []
    >>> 
    """
    try:
        file = open(file_name,"r")
    except:
        print("Invalid File Name")
        return []
    try:
        filter_key, filter_str = list(dictfilter.items())[0]
    except:
        print("Invalid dictionary format")
        return []
    if (len(dictfilter) !=1) or (filter_key not in ['School' , 'Age', 'Health', 'Failures','All']):
        print("Invalid Value")
        return []
    studytime_index = -1
    for line in file:
        keys = line.strip().split(",")
        for item in keys:
            try:
                if (item.index(".")>-1) and str(float(item)) == str(item): # checking if the item is a float .
                    studytime_index = keys.index(item) 
                    break   # Saving the list index of the first float element and breaking out of the loop.
            except:studytime_index = -1 # Pass the Statement if we got any non float items (we're not sure if we can use Pass).
        if studytime_index != -1 : break # Breaking out of the loop for the first float found with its index saved in studytime_index.
    file.close()
    # Closing and re-opening the file to reset the pointer as we can't use seek() then getting the first line to use a the dictionary keys.
    file = open(file_name,"r")
    for line in file:
        keys = line.strip().split(",")
        break
    data=[] #the data list of students
    for line in file:
        header = {key : list for key in keys} # Creating the dictionary with the list keys assigning each key value to a new item with the key name from the list keys and making sure it reset the dictionary each loop.
        values = line.strip().split(",") # Creating a list with no white spaces that contains the list values fetched from the file.
        if filter_key=="All" or str(values[keys.index(filter_key)])==str(filter_str) : # Condition to check if the current line we're pointing on in the file is meeting the conditions of our filter.
            for i in range(len(values)): # Looping through the values of the list.
                # Saving the values with their correct data type if it's study time then save it as a float otherwise try to save it as an it if it failed then save it as a string
                try:
                    if i == studytime_index :header[keys[i]]=float(values[i])
                    else : header[keys[i]]=int(values[i])
                except : header[keys[i]]=values[i]
            if filter_key!="All":header.pop(filter_key) # Removing the item that we filtered with if the filter 'All' wasn't chosen.
            data.append(header) # Add the data saved from the dictionary into a new item to the data list
    # Closing the file and returning the filtered students
    file.close()
    return data
#==========================================#
# Place your add_average function after this line
def add_average(data: list[dict[str, str]]) -> list[dict[str, str]]:
    """return a new list with a new calculated average grade row for each student from a given list of students.
    Precondition: 
    
    >>> add_average([ {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 7.0,'Failures': 1, 'Health': 3, 'Absences': 7,'FallGrade': 5, 'WinterGrade': 6},{'School': 'MS', 'ID': 277, 'Age': 21, 'StudyTime': 8.5,'Failures': 2, 'Health': 1, 'Absences': 8,'FallGrade': 5, 'WinterGrade': 9}])
    [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 5, 'WinterGrade': 6, 'AvgGrade': 5.5}, {'School': 'MS', 'ID': 277, 'Age': 21, 'StudyTime': 8.5, 'Failures': 2, 'Health': 1, 'Absences': 8, 'FallGrade': 5, 'WinterGrade': 9, 'AvgGrade': 7.0}]
    
    >>> add_average([])
    []
    
    >>> add_average([ {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 7.0,'Failures': 1, 'Health': 3, 'Absences': 7,'FallGrade': "5", 'WinterGrade': "6"},{'School': 'MS', 'ID': 277, 'Age': 21, 'StudyTime': 8.5,'Failures': 2, 'Health': 1, 'Absences': 8,'FallGrade': "String", 'WinterGrade': "Test"}])
    [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': '5', 'WinterGrade': '6', 'AvgGrade': 5.5}, {'School': 'MS', 'ID': 277, 'Age': 21, 'StudyTime': 8.5, 'Failures': 2, 'Health': 1, 'Absences': 8, 'FallGrade': 'String', 'WinterGrade': 'Test', 'AvgGrade': 'N/A'}]
    """
    students = [dict(d) for d in data] # Deep copy the data to avoid changing it.
    try:
        for row in students:
            try:
                # Convert grades to float to handle decimal numbers too
                row["AvgGrade"] = round((int(row["WinterGrade"]) + int(row["FallGrade"])) / 2,2)
            except (ValueError, TypeError) as e:
                try:
                    print(f"Invalid Value for\n - Winter Grade: {row.get('WinterGrade', 'N/A')}\n - Fall Grade: {row.get('FallGrade', 'N/A')}\nSkipping Row ...")
                except:
                    print("FallGrade or WinterGrade row don't exist")
                row["AvgGrade"] = "N/A"
    except:
        print("List Format invalid.")
        return[]
    return students