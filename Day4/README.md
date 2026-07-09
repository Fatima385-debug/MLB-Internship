Student Performance Analysis

Project Overview
This mini project analyzes a dataset of 20 students across three programs (AI, SE, DS), covering their marks in Python, Mathematics, Statistics, and Machine Learning, along with attendance. The goal was to practice core data analysis skills using NumPy and Pandas.

Folder Contents
performance_analysis.py: Main Python script that loads, analyzes, and processes the dataset
student_performance.csv: The original, unmodified dataset 
processed_analysis.csv: The cleaned/analyzed dataset with added columns (`Total_Marks`, `Average_Marks`), sorted by performance 

What the Script Does
1. Loads the dataset using Pandas (`pd.read_csv`)
2. Displays basic dataset info — shape, column names, data types, summary statistics, and missing value counts
3. Calculates the average marks per subject using NumPy (`np.mean`)
4. Computes each student's Total_Marks and Average_Marks
5. Identifies the top 5 performing students
6. Flags students scoring below the overall class average
7. Displays the total number of students
8. Saves the final analyzed dataset to a new CSV file

Key Insights
- The overall class average across all four subjects is ~80.4 marks
- Machine Learning had the highest subject average (82.6), while Python had the lowest (78.9) suggesting students may need more foundational support in Python.
- The top 5 students consistently scored above 89 average marks across all subjects, showing strong, well-rounded performance rather than excelling in just one area.
- 10 out of 20 students (50%) scored below the class average, indicating the class performance is fairly spread out rather than tightly clustered.
- There appears to be a positive relationship between attendance and average marks top performers also had the highest attendance (96–100%), while below-average students generally had lower attendance (75–87%).

What I Learned About NumPy
- NumPy makes numerical operations on arrays/columns fast and concise 
- Vectorized operations are far more efficient than writing explicit Python loops over rows.
- NumPy works seamlessly underneath Pandas every Pandas Series is backed by a NumPy array, so understanding NumPy helped me understand why Pandas operations behave the way they do 

What I Learned About Pandas
- `pd.read_csv()` and DataFrame basics: inspecting data with `.shape`, `.dtypes`, `.head()`, `.describe()`, and `.isnull().sum()` gives a fast first impression of any dataset.
- How to create new derived columns (`Total_Marks`, `Average_Marks`) by applying operations across multiple columns with `.sum(axis=1)` and `.mean(axis=1)`.
- How to filter rows conditionally (e.g., `df[df["Average_Marks"] < overall_average]`) to isolate specific groups of students.
- How to sort a DataFrame (`sort_values`) to rank students and extract the top N with `.head()`.
- How to export a processed DataFrame back to CSV with `.to_csv()`, preserving the analysis for later use.

Challenges Faced
- Deciding how to define "below average" whether to compare against each subject's average separately or against a student's overall average across all subjects. I chose the overall average per student for a simpler, single performance metric.
- Making sure Student_ID was treated as a unique identifier for counting total students rather than accidentally counting duplicate names.
Keeping the script readable and organized in clear sections (info → averages → top performers → below average → save) so it's easy to follow and reuse on other datasets.

