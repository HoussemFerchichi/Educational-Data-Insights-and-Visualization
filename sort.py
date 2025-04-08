# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Houssem Ferchichi (Student ID: 101344983) / Brett Patzer (Student ID: 101323409) / Nicole Chen (Student ID: 101343450) / Shawn Pye (Student ID: 101352512)"

# Update "" with your team (e.g. T102)
__team__ = "T-28"


#==========================================#
# Place your sort_students_age_bubble function after this line

def sort_students_age_bubble(students:list, order:str):
    """return a list of dictionnaries of students sorted by 'Age' attribute using the bubble sort algorithm either ascending or descending for a given order and list students
    Precondition:

    >>> students = []
    >>> sort_students_age_bubble(students, "D")
    Empty list.
    >>> print(students)
    []
    >>>

    >>> students =  [{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}]
    >>> sort_students_age_bubble(students, "D")
    List sorted.
    >>> print (students)
     [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]

    >>> students = [{"School":"GP"}, {"School":"MS"}]
    >>> sort_students_age_bubble(students, "A")
    List not sorted. Age key not present.
    >>> print (students)
    [{'School': 'GP'}, {'School': 'MS'}]

    """
    if not students:
        return "Empty list."
    
    if not all("Age" in student for student in students):
        return "List not sorted. Age key not present."
    
    n = len(students)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (order == "A" and students[j]["Age"] > students[j + 1]["Age"]) or (order == "D" and students[j]["Age"] < students[j + 1]["Age"]):
                students[j], students[j + 1] = students[j + 1], students[j]
    
    return "List sorted."
#==========================================#
# Place your sort_students_time_selection function after this line
def sort_students_time_selection(students:list, order:str):
    """return a list of dictionnaries of students sorted by 'StudyTime' attribute using the selection sort algorithm either ascending or descending for a given order and list students
    Precondition:

    >>> students = []
    >>> sort_students_time_selection(students, "D")
    Empty list.
    >>> print(students)
    []
    
    >>> students = [{"StudyTime":10,"School":"GP"}, {"StudyTime":19,"School":"MS"}]
    >>> sort_students_time_selection(students, "D")
    List sorted.
    >>> print (students)
    [{"StudyTime": 19, "School":"MS"}, {"StudyTime":10,"School":"GP"}]

    >>> students = [{"School":"GP"}, {"School":"MS"}]
    >>> sort_students_time_selection(students, "D")
    List not sorted. StudyTime key not present.
    >>> print (students)
    [{'School': 'GP'}, {'School': 'MS'}]

    """
    if not students:
        return "Empty list."
    
    if not all("StudyTime" in student for student in students):
        return "List not sorted. StudyTime key not present."
    
    n = len(students)
    ascending = order == "A"
    
    for i in range(n):
        extreme_idx = i
        for j in range(i + 1, n):
            if (ascending and students[j]["StudyTime"] < students[extreme_idx]["StudyTime"]) or \
               (not ascending and students[j]["StudyTime"] > students[extreme_idx]["StudyTime"]):
                extreme_idx = j
        
        students[i], students[extreme_idx] = students[extreme_idx], students[i]
    
    return "List sorted."

#==========================================#
# Place your sort_students_avg_insertion function after this line
def sort_students_avg_insertion(students:list, order:str):
    """return a list of dictionnaries of students sorted by 'AvgGrade' attribute using the insertion sort algorithm either ascending or descending for a given order and list students
    Precondition:

    >>> students = []
    >>> sort_students_avg_insertion(students, "A")
    Empty list.
    >>> print(students)
    []

    >>> students = [{"AvgGrade":7.2,"School":"GP"}, {"AvgGrade":9.1,"School":"MS"}]
    >>> sort_students_avg_insertion(students, "A")
    List sorted.
    >>> print (students)
    [{"AvgGrade": 9.1, "School":"MS"}, {"AvgGrade":7.2,"School":"GP"}]

    >>> students = [{"School":"GP"}, {"School":"MS"}]
    >>> sort_students_avg_insertion(students, "A")
    List not sorted. AvgGrade key not present.
    >>> print (students)
    [{'School': 'GP'}, {'School': 'MS'}]

    """
    if not students:
        return "Empty list."
    
    if not all("AvgGrade" in student for student in students):
        return "List not sorted. AvgGrade key not present."
    
    n = len(students)
    
    for i in range(1, n):
        key = students[i]
        j = i - 1
        
        if order == "A":
            while j >= 0 and students[j]["AvgGrade"] > key["AvgGrade"]:
                students[j + 1] = students[j]
                j -= 1
        elif order == "D":
            while j >= 0 and students[j]["AvgGrade"] < key["AvgGrade"]:
                students[j + 1] = students[j]
                j -= 1
        else:
            return "Invalid order. Use 'A' for ascending or 'D' for descending."
        
        students[j + 1] = key
    
    return "List sorted."

#==========================================#
# Place your sort_students_failures_bubble function after this line
def sort_students_failures_bubble(student_list:list, sort_order:str):
    """return a list of dictionnaries of students sorted by 'Failures' attribute using the bubble sort algorithm either ascending or descending for a given sort_order and list student_list
    Precondition:

    >>> students = []
    >>> sort_students_failures_bubble(students, "A")
    Empty list.
    >>> print(students)
    []

    >>> students = [{"Failures":19,"School":"GP"},{"Failures":10,"School":"MS"}]
    >>> sort_students_failures_bubble(students, "A")
    List sorted.
    >>> print (students)
    [{'Failures': 10, 'School': 'MS'}, {'Failures': 19, 'School': 'GP'}]

    >>> students = [{"School":"GP"}, {"School":"MS"}]
    >>> sort_students_failures_bubble(students, "A")
    List not sorted. Failures key not present.
    >>> print (students)
    [{'School': 'GP'}, {'School': 'MS'}]

    """
    if len(student_list) == 0:
        return "Empty list."
    if (sort_order != "A" and sort_order != "D"):
        return "Please Use A for ascending and D for descending"
    if 'Failures' not in student_list[0]:
        return "List not sorted. Failures key not present."
    
    for i in range(len(student_list)):
        for j in range(0, len(student_list)-i-1):
            if sort_order == "A":
                if student_list[j]['Failures'] > student_list[j+1]['Failures']:
                    student_list[j], student_list[j+1] = student_list[j+1], student_list[j]
            elif sort_order == "D":
                if student_list[j]['Failures'] < student_list[j+1]['Failures']:
                    student_list[j], student_list[j+1] = student_list[j+1], student_list[j]
    
    return "List sorted."


#==========================================#
# Place your sort function after this line
def sort(students:list, order:str, attribute:str):
    """return a list of dictionnaries of students sorted by attribute using the sort algorithms used in functions called depends on the attribute either ascending or descending for a given order and a list students and the attribute.
    Precondition:

    >>> students = []
    >>> sort(students, "D", "Age")
    Empty list.
    >>> print(students)
    []
    >>> students = [{"Failures":19,"School":"GP"},{"Failures":10,"School":"MS"}]
    >>> sort(students, "A", "Failures")
    List sorted.
    >>> print (students)
    [{'Failures': 10, 'School': 'MS'}, {'Failures': 19, 'School': 'GP'}]

    >>> students = [{"School":"GP"},{"School":"MS"}]
    >>> sort(students, "D", "School")
    Invalid input, the list cannot be sorted by School.
    >>> print (students)
    [{'School': 'GP'}, {'School': 'MS'}]

    >>> students = []
    >>> sort(students, "D", "School")
    Invalid input, the list cannot be sorted by School.
    >>> print(students)
    []

    """
    if len(attribute) == 0:
        return "Invalid input, sorting attribute is required."
    if attribute not in ["Age", "StudyTime", "AvgGrade", "Failures"]:
        return "Invalid input, the list cannot be sorted by " + str(attribute)+"."
    if len(students) == 0:
        return "Empty list."
    if len(order) != 1 or (order != "A" and order != "D"):
        return "Please Use A for ascending and D for descending"
    if attribute == "Age":
        return sort_students_age_bubble(students,order)
    elif attribute == "StudyTime":
        return sort_students_time_selection(students,order)
    elif attribute == "AgAvgGradee":
        return sort_students_avg_insertion(students,order)
    else:
        return sort_students_failures_bubble(students,order)


# Do NOT include a main script in your submission
