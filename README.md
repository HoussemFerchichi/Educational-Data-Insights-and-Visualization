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
- `matplotlib v3.10` 3.10 or higher
- `numpy` v1.21.0 or higher

➔ Install/Update latest Python release using:

```bash
# For windows users make sure to enable the option 'Add Python to environment variables' after executing the installer.

https://www.python.org/downloads/

```
➔ Install/Update dependencies using:

```bash
pip install matplotlib numpy
```
________________________

## Installation

1. Download and extract the project zip file from Brightspace.  
2. Ensure all `.py` files (`batch_UI.py`, `text_UI.py`, `load_data.py`, `sort.py`, `curve_fit.py`, `histogram.py`) are in the same folder. 
3. If an IDE is used for execution just open either batch_UI.py or text_UI.py and execute the program
4. For normal usage open a new terminal or command prompt and make sure it's in the directory of the downloaded files. If not execute in the command prompt:  
```bash   
cd /path/to/EduInsight/files
```    
_________________________________________________________________________________________+ 
 

➔ For the text-based user interface:  
1. Run the software using:
```bash
python text_UI.py
```
_________________________________________________________________________________________+  

➔ For executing commands from a text file:
1. Prepare your batch command file (e.g., `commands.txt`) and place it in the same directory.
2. Run the software using:
```bash
python batch_UI.py
```
When prompted, enter the name of your command file (e.g., `commands.txt`).

---

## Usage

Please refer to the user demonstration video for detailed usage instructions.

---

## Credits

| Team Member        | Student ID   | Contribution                                                                            |
|--------------------|--------------|-----------------------------------------------------------------------------------------|
| Houssem Ferchichi  | 101344983    | User Interaction; Incorporating sorting, histogram generation, curve fitting and data loading , along with code optimization and leading the tasks and roles distribution with fixing and maintaining the code      |
| Brett Patzer       | 101323409    | Incorporating sorting, histogram generation, and curve fitting functionality            |
| Nicole Chen        | 101343450    | Incorporating sorting, histogram generation, and curve fitting functionality            |
| Shawn Pye          | 101352512    | Incorporating sorting, histogram generation, and curve fitting functionality            |

---

## License

This project is licensed under the [MIT License](https://github.com/HoussemFerchichi/Educational-Data-Insights-and-Visualization/blob/main/LICENSE).
