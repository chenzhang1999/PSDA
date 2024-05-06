
# Employment Prediction Project

## Project Overview
This project utilizes machine learning techniques to analyze and predict employment status based on various features. The goal is to predict whether individuals are employed or unemployed.

## Data
The data used in this project includes multiple features, which are read from CSV files. The specific files are `employment_train.csv` and `employment_test.csv`, used for training and testing the model respectively.

## Feature Processing
- The `earnwke` feature has been processed to handle missing values and format conversions.

## Models
The project uses multiple base models and a meta model:
- **Base Models**: Random Forest, Gradient Boosting Machine, Support Vector Machine
- **Meta Model**: Logistic Regression

Models use cross-validation to predict probabilities, which are then used as new features to train the meta model.

## Performance Evaluation
The model's performance is evaluated using accuracy and recall rates.

## Installation Requirements
The project requires the following Python libraries:
```
pip install pandas numpy matplotlib seaborn scikit-learn
```

## How to Use
1. Ensure all dependencies are installed.
2. Run the script, and the model will automatically read data from CSV files, perform training and testing.
3. Check the output results.

## License
```
