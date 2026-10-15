# The Impact of Daily Screentime on Academic Performance - Data Analysis with Python
The aim of this project is the analysis of the relationship between total daily device usage (screen time) of students and their academic performance. Statistical analysis and visualisation techniques were used to answer the research question  **Is total daily screen time associated with academic performance of students?**

## THE DATASET
The dataset can be found on Kaggle.com (https://www.kaggle.com/datasets/aiexplorer77/gaming-vs-academic-performance/data). To reproduce the results it must be cleaned by removing all academic socres outliers above a 100.

## HOW TO RUN THE CODE
Download the dataset form Kaggle.com and save it to the same directory as the project. Make sure the name of the csv file matches the one in the code - in my case it's "Gaming_Academic_Performance_updated.csv"

## WHAT THE CODE DOES
- Splits the students into "low" and "high" screen time groups based on median device usage
- Performs statistical analysis:
  - Calculates descriptive statistics (mean and standard deviation) for both groups
  - Runs an independent t-test to determine if the difference in grades is statistically significant
  - Calculates Pearson's correlation coefficient to measure the overall relationship between screen time and grades
- Visualizes:
  - A histogram showing the distribution of daily screen time among students
  - A scatter plot displaying academic performance against total daily screen time
  - An error bar chart comparing the average grades and standard deviation of the two groups

## REQUIRED LIBRARIES
You need to have following libraries downloaded to run this code :

- pandas 
- matplotlib 
- scipy 


You can download them by putting the following command in the terminal :

```bash
pip install pandas matplotlib scipy 

