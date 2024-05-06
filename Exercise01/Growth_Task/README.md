# Project Title: Growth Prediction Model
## Description
This project is a Python-based analytical model designed to predict economic growth based on historical data. Utilizing datasets containing variables like GDP, oil prices, and other economic indicators, this model aims to provide insights into potential growth trends. The implementation is prepared for a Kaggle environment, leveraging various Python libraries for data processing and analysis.

## Installation
To run this project, you will need a Python environment with necessary libraries installed. This project is configured for the Kaggle platform, which provides a ready-to-use Python environment with all necessary libraries pre-installed.

## Requirements
Python 3.x
Pandas
Numpy
scikit-learn
## File Structure
growth_train.csv: Training data containing historical growth data along with various economic indicators.
growth_test.csv: Test dataset used to evaluate the model's performance.
growth_meta.pdf: Metadata and additional information about the datasets used.
hdma.ipynb: Main Python notebook containing the code for data processing, model training, and evaluation.
## Data Preprocessing
- Growth Data Transformation: The growth rate data in the growth column uses commas as decimal separators. The preprocessing step converts these to standard decimal points and changes the data type to float for further analysis.
- Feature Encoding:
The categorical feature country_name along with other selected features are encoded using OneHotEncoder, which creates new binary columns for each unique category.
This transformation is applied to both training and test datasets to ensure consistency in feature representation.
## Model Setup
- Random Forest Regressor
A Random Forest Regressor is used for predicting economic growth. This model is beneficial for handling non-linear data and can automatically handle feature interactions.
- Hyperparameter Tuning
  - Grid Search CV: Implemented to find the optimal hyperparameters for the Random Forest model. The parameters tuned include:
  - n_estimators: Number of trees in the forest.
  - max_depth: Maximum number of levels in each tree.
  - min_samples_split: Minimum number of samples required to split an internal node.
  - min_samples_leaf: Minimum number of samples required to be at a leaf node.
The tuning process uses a 10-fold cross-validation and aims to minimize the mean squared error.
## Prediction and Output
Predicting Growth: Once the model is trained with optimal parameters, it is used to predict the growth rate for the unseen test dataset.
Saving Predictions: Predictions are saved to a CSV file, which includes IDs from the test data and the predicted growth rates. This file can be submitted for evaluation if used in a competitive environment like Kaggle.

## License
This project is released under the MIT License.
