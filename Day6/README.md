Student Score Prediction System
A simple machine learning project that predicts a student's Average_Score from their age, program, and attendance, using Linear Regression in scikit-learn.

Project Overview
The pipeline:
1. Loads `student_performance.csv`
2. Preprocesses the data (feature engineering, encoding, scaling)
3. Splits the data into training and testing sets
4. Trains a Linear Regression model
5. Evaluates predictions against actual scores
6. Visualizes results with an Actual vs. Predicted scatter plot

Learned About Data Preprocessing
- Raw data isn't ready for modeling. The dataset needed a target column (`Average_Score`) engineered from the four subject scores (`Python`, `Mathematics`, `Statistics`, `Machine_Learning`) before any model could be trained on it.
- Categorical data needs encoding. The `Program` column (AI/SE/DS) is text, and scikit-learn models only accept numbers. I used Label Encoding to convert it to integers. For a column with more than two unordered categories, One-Hot Encoding is often the safer choice, since Label Encoding can accidentally imply a ranking between categories that doesn't exist.
- Feature scaling matters. `Age`, `Program_Encoded`, and `Attendance` are on very different numeric scales. I applied Standardization (`StandardScaler`) so no single feature dominates the model just because its raw numbers are larger.
- Avoiding data leakage is critical. Two leakage traps I had to watch for:
  - The scaler was fit only on the training set, then just applied (`.transform()`) to the test set — never fit on test data.
  - The subject scores (`Python`, `Mathematics`, `Statistics`, `Machine_Learning`) were excluded from the features, since they were used to construct the target (`Average_Score`) including them would let the model "cheat" by seeing a near-exact answer.

Why Train-Test Splitting Is Important

Splitting the data into a training set (80%) and a testing set (20%) lets us evaluate the model on data it has never seen during training. Without this split, we'd only know how well the model memorized the training data, not how well it generalizes to new students. The test set acts as a stand-in for real-world, unseen data, giving a more honest measure of performance.

Evaluation Metrics Used

Mean Absolute Error (MAE): Average absolute difference between actual and predicted scores — how many points off predictions are, on average. 
Mean Squared Error (MSE): Average of squared differences penalizes larger errors more heavily than MAE. 
R² Score: Proportion of variance in `Average_Score` explained by the model (1.0 = perfect, 0 = no better than predicting the mean). 

Model Performance and Observations

On this dataset (20 students total: 16 training, 4 testing):
MAE: 2.53 
MSE: 13.46 
R² Score: 0.80 

Observations:
- The model explains about 80% of the variation in students' average scores, and typical predictions are off by roughly 2.5 points, a reasonably strong result for a first model.
- Looking at the model's coefficients, Attendance was by far the strongest predictor of Average_Score, while Age had a small positive effect and Program had almost no effect.
- The largest single error (about 7 points) occurred on the lowest-scoring student in the test set, suggesting the model may slightly underestimate how low scores can go for students with unusual patterns.
- With only 20 rows total and just 4 samples in the test set, these metrics are based on a very small sample and should be treated as a rough first estimate rather than a robust conclusion. 
