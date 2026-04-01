Overview

This project focuses on predicting customer churn using a machine learning model. The goal was to practice data cleaning, preprocessing, and building a classification model to identify customers who are likely to leave a service.

Dataset

The dataset used is the Telco Customer Churn dataset, which contains customer information such as demographics, account details, and service usage.

Tools & Technologies:


- Python
- Pandas
- Scikit-learn
- Matplotlib

  
Project Workflow


1. Data Cleaning
- Converted data types (e.g. TotalCharges to numeric)
- Removed missing values
- Dropped unnecessary columns
2. Data Preprocessing
- Encoded categorical variables using one-hot encoding
- Split data into training and testing sets
3. Model Building
- Trained a Logistic Regression model
- Adjusted model parameters to improve convergence
4. Evaluation
- Evaluated model performance using accuracy score
- Achieved approximately 80% accuracy

  
Key Insights


- Customers using fiber optic internet are more likely to churn
- Customers paying via electronic check show higher churn rates
- Higher monthly charges are associated with increased churn
- Certain customer groups (e.g. senior citizens) show slightly higher churn
  
What I Learned


1. How to clean and preprocess real-world data
2. How to handle categorical variables for machine learning
3. How to train and evaluate a classification model
4. How to interpret model outputs and extract business insights
   
How to Run


1. Clone the repository
2. Install required libraries:
3. pip install pandas scikit-learn matplotlib
4. Run the script: python churn_model.py

   
Future Improvements


- Use more advanced models (e.g. Random Forest, XGBoost)
- Improve evaluation using precision, recall, and F1-score
- Perform feature importance analysis
- Build a simple dashboard or interface for predictions
- Scale features using StandardScaler
