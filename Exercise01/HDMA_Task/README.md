# HDMA Prediction Model
## Description
This project utilizes a machine learning model to predict loan approval outcomes based on historical loan application data. The model is built using a Random Forest classifier, a popular choice for such tasks due to its robustness and ability to handle unbalanced datasets. The implementation is designed to run in a Kaggle environment, leveraging Python's powerful libraries for data preprocessing and model training.

## Installation
### Requirements:

- Python 3.x
- Pandas
- Numpy
- scikit-learn
### Setup:

Clone the repository to your local machine or download the notebook if using Kaggle.
Ensure the dataset files are stored in the correct directory as specified in the notebook (e.g., /kaggle/input/ for Kaggle environments).
## File Structure
- hdma_train.csv - Training dataset containing historical data of loan applications with various attributes and the final approval status (deny).
- hdma_test.csv - Test dataset for which the model needs to predict the approval status.
- hdma_meta.pdf - Document describing metadata related to datasets.
- hdma.ipynb - Main Python notebook containing all the code for data processing, model training, and predictions.
## Data Preprocessing
1.  **Handling Missing Values**:
Missing values in both training and test datasets are filled using the most frequent value (mode) of each column.
2. **Feature Encoding**:
Categorical variables are converted into numerical format using one-hot encoding, which is essential for fitting machine learning models.
## Model Setup
### Random Forest Classifier
The classifier is trained on preprocessed training data using 100 trees (n_estimators=100) and a random state set for reproducibility.
### Model Evaluation
The model's performance is evaluated using 5-fold cross-validation, assessing its accuracy across different subsets of the training data.
## Prediction and Output
- Prediction: The model predicts the approval status (deny) for each entry in the test dataset.
- Output: Predictions are stored in a CSV file alongside the corresponding IDs from the test data. This file can be used for submission in a competition or for further analysis.

## License
This project is available under the MIT License.
