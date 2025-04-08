
# Educational Data Insights and Visualization

**Date:** April 8, 2025  
**Software Name:** EduInsight
**Version:** 1.0  
**Contact Information:**  
Houssem Ferchichi
Email: houssemferchichi@cmail.carleton.ca

---

## Description

This project aims to analyze and visualize student data. EduInsight provides two ways to interact for executing commands, a simple text-based user interface and automating the execution for a larger scaled goal by providing a chain of commands in a text file. EduInsight allows loading data from a CSV file, sorting the loaded data based on a selected attribute, generate histograms of a specified attribute, and perform polynomial curve fitting on a specified attribute to predict AvgGrade.

---

## Dependencies

To run EduInsight, the following are required:

- Python 3.9 or higher
- `matplotlib`
- `numpy`

Install dependencies using:

```bash
pip install matplotlib numpy
```

---

## Installation

+------------------------------------------------------------------------------+
1. Download and extract the project zip file from Brightspace.
2. Ensure all `.py` files (`batch_UI.py`, `text_UI.py`, `load_data.py`, `sort.py`, `curve_fit.py`, `histogram.py`) are in the same folder.
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
For the text-based user interface:
1. Run the software using:
```bash
python text_UI.py
```                                                  
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
For executing commands from a text file:
1. Prepare your batch command file (e.g., `commands.txt`) and place it in the same directory.
2. Run the software using:
```bash
python batch_UI.py
```
When prompted, enter the name of your command file (e.g., `commands.txt`).
+------------------------------------------------------------------------------+

---

## Usage

Please refer to the user demonstration video submitted alongside this project for detailed usage instructions.

---

## Credits

| Team Member        | Student ID   | Contribution                          |
|--------------------|--------------|----------------------------------------|
| Houssem Ferchichi  | 101344983    | Batch UI logic, command parsing        |
| Brett Patzer       | 101323409    | Sorting functionality (`sort.py`)      |
| Nicole Chen        | 101343450    | Histogram visualization (`histogram.py`) |
| Shawn Pye          | 101352512    | Curve fitting logic (`curve_fit.py`)   |

---

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
