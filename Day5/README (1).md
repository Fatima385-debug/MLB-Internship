Student Performance Dashboard

Project Overview
This mini project builds a simple analysis notebook to explore a student performance dataset (20 students, 4 subjects: Python, Mathematics, Statistics, Machine Learning). The notebook answers a set of core questions about the class and visualizes the findings.

Folder Contents
student_performance_dashboard.ipynb`: Jupyter notebook containing the full analysis and charts
student_performance.csv: The original dataset 


Approach
- Loaded the dataset with Pandas and computed an `Average_Score` column per student across all four subjects.
- Used NumPy for subject-wise and overall averages.
- Identified the top 5 students by sorting on `Average_Score`.
- Flagged students needing improvement as those scoring below the overall class average.
- Found the subject with the highest class average using `idxmax()`.
- Visualized results with Matplotlib: bar charts, a histogram, and a pie chart.

Key Insights
- The class average across all four subjects is ~80.4 marks.
- Machine Learning has the highest subject average, while Python has the lowest suggesting Python may need more foundational reinforcement.
- The top 5 students consistently score above 89 average marks, showing strong, well-rounded performance across all subjects rather than strength in just one.
- 10 out of 20 students fall below the overall class average, showing a fairly even split between higher and lower performers.
- Students with higher attendance tend to also have higher average scores, suggesting attendance may be linked to performance.

Charts Included
- Bar chart — average marks per subject
- Bar chart — Top 5 performing students
- Histogram — distribution of average scores across the class
- Pie chart — proportion of students above vs. below the class average

What I Learned
- How to use Pandas to compute row-wise and column-wise averages (`.mean(axis=1)`, `.mean()`).
- How to use NumPy functions (`np.mean`, `np.round`) alongside Pandas for numerical summaries.
- How to identify top/bottom performers using `sort_values()` and boolean filtering.
- How to use Matplotlib to build clear, simple visualizations (bar, histogram, pie) that make patterns in the data easy to communicate.

Challenges Faced
- Deciding on a fair definition of "needs improvement" — chose the overall class average as the cutoff rather than a fixed score, since it adapts to the class's actual performance level.
