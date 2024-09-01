Technologies and Tools:
Python: Core programming language used for data processing, model training, and deployment.

Pandas & NumPy: Libraries used for data manipulation and numerical operations.

Scikit-Learn: Machine learning library used for model selection, training, and evaluation.

Streamlit: Framework used for deploying the model as an interactive web application.

Joblib: Used for saving and loading the trained model and feature names.

CarDekho Project: Used Car Price Prediction
Objective:
The main goal of this project is to predict the price of used cars based on various features like age, mileage, engine size, maximum power, number of seats, fuel type, transmission type, and body type. The project involves data preprocessing, model training, evaluation, and deployment using a user-friendly interface.

Key Steps:
Data Collection and Preprocessing:

Dataset: The data was collected and stored in an Excel file (processed_data.xlsx).
Feature Engineering: Added a Car_Age feature by calculating the difference between the current year (2024) and the car's model year.
One-Hot Encoding: Applied pd.get_dummies to convert categorical variables (e.g., Fuel Type, Transmission, Body type) into a numerical format suitable for model training.
Target Variable: The Price column was selected as the target variable.
Model Training:

Model Selection: A RandomForestRegressor was chosen for its robustness and ability to handle non-linear relationships.
Hyperparameter Tuning: Used RandomizedSearchCV to optimize the model's hyperparameters, such as n_estimators, max_features, max_depth, min_samples_split, min_samples_leaf, and bootstrap.
Model Evaluation: The model was evaluated using Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R²) metrics on the test data.
Feature Names Saved: The feature names were saved using joblib to ensure consistency between the training and prediction phases.
Model Saving and Deployment:

Model Saving: The trained model was saved as a .pkl file (random_forest_model.pkl) using joblib for later use in predictions.
Streamlit Deployment: The model was deployed using Streamlit, an interactive web application framework, allowing users to input car features and get real-time price predictions.
User Interface (UI) Design:

Custom Styling: Enhanced the UI with custom background colors, header styling, and organized input fields into columns for a cleaner look.
Input Fields: Included various input fields for users to specify car details such as age, mileage, engine size, fuel type, transmission, and body type.
Prediction Output: Displayed the predicted price in a well-formatted manner after processing the user's input.
