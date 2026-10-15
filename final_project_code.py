import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt
from scipy import stats

########## LOADING THE DATA AND CLEANING ##########

df = pd.read_csv("Gaming_Academic_Performance_updated.csv")
print(df)

df = df[df['grades'] <= 100] #cleaning the data (removing all outlier grades above a 100)


########## STATISTICAL ANALYSIS ##########


#extracting the needed columns with dataframe
screen_time = df['device_usage']
grades = df['grades']

#clculating median device usage
median_screen = statistics.median(df['device_usage']) 

#filtering the data into two halves based on the median
low_screen_df = df[df['device_usage'] <= median_screen] 
high_screen_df = df[df['device_usage'] > median_screen]

#extracting 'grades' from both groups for statistical analysis
grades_low = low_screen_df['grades']
grades_high = high_screen_df['grades']



#DESCRIPTIVE STATISTICS
low_screentime_mean = statistics.mean(grades_low)
low_screentime_stdv = statistics.stdev(grades_low)
high_screentime_mean = statistics.mean(grades_high)
high_screentime_stdv = statistics.stdev(grades_high)

print(f"Average academic performance in low screen time group : {low_screentime_mean}, +/- {low_screentime_stdv}")
print(f"Average academic performance in high screen time group :{high_screentime_mean}, +/- {high_screentime_stdv}")
print()

#T-TEST
t, p = stats.ttest_ind(grades_low, grades_high, equal_var=False)

print("T-test results :")
print("t:", t)
print("P:", f"{p:.10e}")
print()

#correlation coefficient (Pearson's)
r, p_c = stats.pearsonr(df['device_usage'], df['grades'])

print("Pearson's correlation coefficient results:")
print("r:", r)
print("P:", f"{p_c:.10e}")
print()


########## PLOTTING ##########

#1ST PLOT  : HISTORGRAM
plt.hist(screen_time, bins=range(1, 15), alpha=0.6, color='purple', edgecolor='black')

plt.title('Distribution of Daily Screen Time')
plt.xlabel('Total screen time (Hours)')
plt.ylabel('Number of Students')
plt.xticks(range(0, 15))
plt.savefig('screen_time_distribution_histogram.png', dpi=1000, bbox_inches="tight")
plt.show()

#2ND PLOT : SCATTERPLOT
plt.figure(figsize=(10, 6))
plt.scatter(screen_time, grades, alpha=0.5, color='purple', s=10)

plt.title('Academic Performance Score vs. Daily Screen Time')
plt.xlabel('Total Screen Time (Hours)')
plt.ylabel('Academic Performance Score')
plt.grid(True)
plt.savefig('screen_time_grades_scatterplot.png', dpi=1000, bbox_inches="tight")
plt.show()

#3RD PLOT : ERROR BARS
x = ['Low Screen Time', 'High Screen Time']
y = [low_screentime_mean, high_screentime_mean]
error = [low_screentime_stdv, high_screentime_stdv] 
plt.errorbar(x, y, yerr=error, fmt='o', label='Mean ± Standard Deviation',color='purple')

plt.title('Average Academic Performance with Error Bars')
plt.xlabel('Screen Time Group')
plt.ylabel('Academic Performance Score') 
plt.grid(axis='y', alpha=0.8)
plt.legend()
plt.savefig('academic_performance_sd', dpi=1000,bbox_inches="tight")
plt.show()



