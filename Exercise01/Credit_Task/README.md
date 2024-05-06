# Credit Balance Prediction Project
## Project Overview
This project leverages regression models to predict customers' credit balances. It aims to estimate the balance that a customer will maintain, which can help financial institutions in tailoring credit limits and offers.

## Data
The dataset encompasses customer demographic and financial data, divided into training and testing sets. The primary files are credit_train.csv and credit_test.csv.

## Feature Processing
Significant features like income, limit, and rating are normalized and outliers are handled to enhance model performance.

## Models
This project uses a variety of regression models to predict credit balances:
### Base Models: Linear Regression, RandomForest
### Advanced Models: XGBoost
The models are evaluated and optimized through cross-validation to ensure robust predictions.

## Performance Evaluation
The effectiveness of the models is measured using the Mean Absolute Error (MAE).

## How to Use
Install all required dependencies.
Run the notebook to load data, process features, train models, and evaluate their performance.
Analyze the output to assess the prediction accuracy of the models.
