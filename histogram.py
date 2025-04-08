# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
___author__ = "Houssem Ferchichi (Student ID: 101344983) / Brett Patzer (Student ID: 101323409) / Nicole Chen (Student ID: 101343450) / Shawn Pye (Student ID: 101352512)"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-28"

#==========================================#
# Place your script for your text_UI after this line
# You are allowed to create auxiliary functions
import matplotlib.pyplot as plt

def histogram(data, attribute):
    """Generates a histogram for the specified attribute in the given data.

    The function handles both categorical and numerical attributes:
    - For categorical attributes, it counts the frequency of each category and displays a bar chart of the counts.
    - For numerical attributes, it groups values into intervals and displays a bar chart showing the distribution of values across those intervals.

    Parameters:
    - data (list of dicts): The dataset to generate the histogram for, where each entry is a dictionary representing a row of data.
    - attribute (str): The attribute (column) to generate the histogram for. This can be either categorical (e.g., 'Gender', 'Subject') or numerical (e.g., 'Age', 'Score').

    Returns:
    - If the attribute is categorical, returns -1 after displaying the histogram.
    - If the attribute is numerical, returns the maximum value of the attribute.

    If the data is empty, a message is printed and `None` is returned.

    Example:
    - For a numerical attribute (e.g., 'Age'), the function will divide the range of ages into 10 intervals and plot a bar chart of counts within each interval.
    - For a categorical attribute (e.g., 'School'), the function will count how many entries correspond to each category and display a bar chart of the counts.
    """
    if not data:
        print("Empty data.")
        return None
    sample_value = data[0][attribute]

    if isinstance(sample_value, str):
        # Categorical attribute
        counts = {}
        for entry in data:
            key = entry[attribute]
            counts[key] = counts.get(key, 0) + 1
        
        # Plotting
        labels = list(counts.keys())
        values = list(counts.values())
        
        plt.figure(figsize=(10, 6))
        plt.bar(labels, values, color='skyblue')
        plt.title(f'Histogram of {attribute}')
        plt.xlabel(attribute)
        plt.ylabel('Count')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

        return -1

    else:
        # Numerical attribute
        values = [entry[attribute] for entry in data]
        max_val = values[0]
        for val in values[1:]:
            if val > max_val:
                max_val = val
        interval = max_val / 10
        bins = [0] * 10
        for val in values:
            index = int(val // interval)
            if index == 10:
                index = 9
            bins[index] += 1
        labels = []
        for i in range(10):
            start = round(i * interval, 2)
            end = round((i + 1) * interval, 2)
            labels.append(f"{start}-{end}")
        
        plt.figure(figsize=(12, 6))
        plt.bar(labels, bins, color='salmon')
        plt.title(f'Histogram of {attribute}')
        plt.xlabel(f'{attribute} Intervals')
        plt.ylabel('Count')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

        return max_val