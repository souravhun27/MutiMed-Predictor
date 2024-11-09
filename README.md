# MutiMed-Predictor 
By sourav , Aeshni , Vaishnavi

Milestone 2 and 3, code files are also uploaded here


A machine learning application for predicting the likelihood of multiple diseases based on user input and medical data. This project supports risk prediction for conditions such as diabetes, heart disease, and Parkinson's disease, aiding healthcare professionals and individuals in identifying potential health risks

- **Features**

  -*Multi-Disease Prediction:* Predicts the likelihood of diseases including diabetes, heart disease, and Parkinson's disease.

  -*Feature Selection and Optimization:* Utilizes Recursive Feature Elimination (RFE) to rank features and optimize model performance.

  -*Data Imputation with Central Tendency:* Retains all features by setting default values (mean, median) for missing or less important attributes.

- **Data Collection**

The datasets for this project were sourced from Kaggle:-

  -Diabetes Dataset
  -Heart Disease Dataset
  -Parkinson's Disease Dataset

- **Data Preprocessing**

   Preprocessing steps, implemented through a dedicated script, include:-

    Handling missing values
    Feature scaling
    Encoding categorical variables



- **Data Visualization**

  Visualizations using Seaborn and Matplotlib were generated to understand the data distribution and relationships. Plots include correlation heatmaps, histograms, and box     plots to identify trends and outliers.

- **Feature Selection**

  Feature selection was performed using Recursive Feature Elimination (RFE) to rank features by their importance. The top-ranked features were retained, while the least        significant features were set to default values based on central tendency, allowing users the option to customize these values for potentially improved predictions.



- **Model Selection**

    The following models were evaluated for each disease, with the best-performing model selected:-

    -Diabetes Prediction: Logistic Regression
    -Heart Disease Prediction: SVM
    -Parkinson's Disease Prediction: SVM


- **Usage**

    - Launch the application interface.
    - Input the necessary medical data.
    - Choose the disease prediction model.
    View the prediction results and risk assessment.


