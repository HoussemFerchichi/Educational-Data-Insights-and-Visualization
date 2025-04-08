# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Houssem Ferchichi (Student ID: 101344983) / Brett Patzer (Student ID: 101323409) / Nicole Chen (Student ID: 101343450) / Shawn Pye (Student ID: 101352512)"

# Update "" with your team (e.g. T102)
__team__ = "T-28"


#==========================================#
# Place your script for your text_UI after this line
# You are allowed to create auxiliary functions
import numpy as np
import matplotlib.pyplot as plt

def curve_fit(data, attribute, degree):
    """return a string representing the polynomial equation in standard polynomial form to fit to a polynomial curve to the 'AvgGrade' attribute based on the given attribute and polynomial degree and data.

    Example:
    - If the attribute is 'StudyTime' and the degree is 2, the function will calculate the average 'AvgGrade' for each unique study time,
      and then fit a quadratic polynomial to these averages, returning a string like "0.1x^2 + 2.3x + 5.7".
    
    
    >>> curve_fit([{"AvgGrade":2,"Failures":5},{"AvgGrade":3,"Failures":8}], "Failures", 1)
    0.3333x+0.3333

    >>> curve_fit([{"AvgGrade":2,"Failures":5},{"AvgGrade":3,"Failures":8},{"AvgGrade":4,"Failures":9}], "Failures", 2)
    0.1667x^2-1.8333x+7.0

    >>> curve_fit([{"AvgGrade":2,"Failures":5},{"AvgGrade":3,"Failures":8},{"AvgGrade":4,"Failures":9}], "Failures", 2)
    -0.0369x^3+1.2276x^2-10.8702x+30.2692
    """
    attr_data = {}
    for record in data:
        key = record[attribute]
        if key not in attr_data:
            attr_data[key] = []
        attr_data[key].append(record["AvgGrade"])

    keys = list(attr_data.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if keys[j] < keys[i]:
                keys[i], keys[j] = keys[j], keys[i]
    
    sorted_keys = keys

    avg_grades = []
    for key in sorted_keys:
        values = attr_data[key]
        total = 0
        count = 0
        for v in values:
            total += v
            count += 1
        avg_grades.append(total / count)
    
    num_points = len(sorted_keys)
    new_degree = degree
    if degree > num_points - 1:
        new_degree = num_points - 1

    coeffs = np.polyfit(sorted_keys, avg_grades, new_degree)
    equation=""
    for i in range(len(coeffs)):
        power = new_degree - i
        coef = round(coeffs[i], 4)

        # If it's the first term, don't add a leading plus
        if i == 0:
            # Add the coefficient with its sign (whether positive or negative)
            if power == 1:
                equation += f"{coef}x"
            elif power == 0:
                equation += f"{coef}"
            else:
                equation += f"{coef}x^{power}"
        else:
            if coef > 0:
                if power == 1:
                    equation += f"+{coef}x"
                elif power == 0:
                    equation += f"+{coef}"
                else:
                    equation += f"+{coef}x^{power}"
            elif coef < 0:
                if power == 1:
                    equation += f"{coef}x"
                elif power == 0:
                    equation += f"{coef}"
                else:
                    equation += f"{coef}x^{power}"
    if equation[-1] == '+':
        equation = equation[:-1]
    return equation
