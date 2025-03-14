# import pandas as pd
# from joblib import load
# model_rest = load("artifacts\model_rest.joblib")
# model_young = load("artifacts\model_young.joblib")
#
# scaler_rest = load("artifacts\scaler_rest.joblib")
# scaler_young = load("artifacts\scaler_young.joblib")
#
#
#
#
#
# def calculate_normalized_risk(medical_history):
#     risk_scores = {
#         "diabetes": 6,
#         "heart disease": 8,
#         "high blood pressure": 6,
#         "thyroid": 5,
#         "no disease": 0,
#         "none": 0
#     }
#
#     # Split the medical history into potential two parts and convert to lowercase
#     diseases = medical_history.lower().split(" & ")
#
#     # Calculate the total risk score by summing the risk scores for each part
#     total_risk_score = sum(risk_scores.get(disease, 0) for disease in diseases)
#     max_score = 14  # risk score for heart disease (8) + second max risk score (6) for diabetes
#     min_score = 0  # Since the minimum score is always 0
#
#     # Normalize the total risk score
#     normalized_risk_score = (total_risk_score - min_score) / (max_score - min_score)
#
#     return normalized_risk_score
#
#
# def preprocess_input(input_dict):
#     expected_columns = [
#         'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genetical_risk', 'normalized_risk_score',
#         'gender_Male', 'region_Northwest', 'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
#         'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight', 'smoking_status_Occasional',
#         'smoking_status_Regular', 'employment_status_Salaried', 'employment_status_Self-Employed'
#     ]
#     insurance_plan_encoding = {'Bronze': 1, 'Silver': 2, 'Gold': 3}
#     df = pd.DataFrame(0, columns=expected_columns, index=[0])
#     bmi = input_dict['BMI Category']
#
#     for key, value in input_dict.items():
#         if key == 'Gender' and value == 'Male':
#             df['gender_Male'] = 1
#         elif key == 'Region':
#             if value == 'Northwest':
#                 df['region_Northwest'] = 1
#             elif value == 'Southeast':
#                 df['region_Southeast'] = 1
#             elif value == 'Southwest':
#                 df['region_Southwest'] = 1
#         elif key == 'Marital Status' and value == 'Unmarried':
#             df['marital_status_Unmarried'] = 1
#         elif key == 'BMI Category':
#             if value == 'Obesity':
#                 df['bmi_category_Obesity'] = 1
#             elif value == 'Overweight':
#                 df['bmi_category_Overweight'] = 1
#             elif value == 'Underweight':
#                 df['bmi_category_Underweight'] = 1
#         elif key == 'Smoking Status':
#             if value == 'Occasional':
#                 df['smoking_status_Occasional'] = 1
#             elif value == 'Regular':
#                 df['smoking_status_Regular'] = 1
#             elif key == 'Employment Status':
#                 if value == 'Salaried':
#                     df['employment_status_Salaried'] = 1
#                 elif value == 'Self-Employed':
#                     df['employment_status_Self-Employed'] = 1
#             elif key == 'Insurance Plan':  # Correct key usage with case sensitivity
#                 df['insurance_plan'] = insurance_plan_encoding.get(value, 1)
#             elif key == 'Age':  # Correct key usage with case sensitivity
#                 df['age'] = value
#             elif key == 'Number of Dependants':  # Correct key usage with case sensitivity
#                 df['number_of_dependants'] = value
#             elif key == 'Income in Lakhs':  # Correct key usage with case sensitivity
#                 df['income_lakhs'] = value
#             elif key == 'Genetical Risk':
#                 df['genetical_risk'] = value
#
#         df['normalized_risk_score'] = calculate_normalized_risk(input_dict['Medical History'])
#         df = handle_scaling(input_dict['Age'], df)
#         return df
#
# def handle_scaling(age, df):
#             if age <= 25:
#                 scaler_object = scaler_young
#             else:
#                 scaler_object = scaler_rest
#
#             cols_to_scale = scaler_object['cols_to_scale']
#             scaler = scaler_object['scaler']
#
#             df['income_level'] = None
#             df[cols_to_scale] = scaler.transform(df[cols_to_scale])
#             df.drop('income_level',axis="columns",inplace=True)
#             return df
#
#
#
# def predict(input_dict):
#     input_df = preprocess_input(input_dict)
#
#     if input_dict['Age'] <=25:
#         prediction = model_young.predict(input_df)
#     else:
#         prediction = model_rest.predict(input_df)
#     return int(prediction)

import pandas as pd
from joblib import load

# Load models and scalers
model_rest = load("artifacts/model_rest.joblib")
model_young = load("artifacts/model_young.joblib")

scaler_rest = load("artifacts/scaler_rest.joblib")
scaler_young = load("artifacts/scaler_young.joblib")


def calculate_normalized_risk(medical_history):
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }

    diseases = medical_history.lower().split(" & ")
    total_risk_score = sum(risk_scores.get(disease, 0) for disease in diseases)

    max_score = 14  # Maximum possible risk (Heart disease + Diabetes)
    min_score = 0  # Minimum risk (No disease)

    # Normalize risk score
    normalized_risk_score = (total_risk_score - min_score) / (max_score - min_score)

    return normalized_risk_score


def preprocess_input(input_dict):
    expected_columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genetical_risk', 'normalized_risk_score',
        'gender_Male', 'region_Northwest', 'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
        'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight', 'smoking_status_Occasional',
        'smoking_status_Regular', 'employment_status_Salaried', 'employment_status_Self-Employed'
    ]

    insurance_plan_encoding = {'Bronze': 1, 'Silver': 2, 'Gold': 3}

    # Initialize dataframe with zero values
    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    # Encoding categorical variables
    df['age'] = input_dict['Age']
    df['number_of_dependants'] = input_dict['Number of Dependants']
    df['income_lakhs'] = input_dict['Income in Lakhs']
    df['insurance_plan'] = insurance_plan_encoding.get(input_dict['Insurance Plan'], 1)
    df['genetical_risk'] = input_dict['Genetical Risk']
    df['normalized_risk_score'] = calculate_normalized_risk(input_dict['Medical History'])

    if input_dict['Gender'] == 'Male':
        df['gender_Male'] = 1
    if input_dict['Region'] == 'Northwest':
        df['region_Northwest'] = 1
    elif input_dict['Region'] == 'Southeast':
        df['region_Southeast'] = 1
    elif input_dict['Region'] == 'Southwest':
        df['region_Southwest'] = 1
    if input_dict['Marital Status'] == 'Unmarried':
        df['marital_status_Unmarried'] = 1
    if input_dict['BMI Category'] == 'Obese':
        df['bmi_category_Obesity'] = 1
    elif input_dict['BMI Category'] == 'Overweight':
        df['bmi_category_Overweight'] = 1
    elif input_dict['BMI Category'] == 'Underweight':
        df['bmi_category_Underweight'] = 1
    if input_dict['Smoking Status'] == 'Occasional':
        df['smoking_status_Occasional'] = 1
    elif input_dict['Smoking Status'] == 'Regular':
        df['smoking_status_Regular'] = 1
    if input_dict['Employment Status'] == 'Salaried':
        df['employment_status_Salaried'] = 1
    elif input_dict['Employment Status'] == 'Self-Employed':
        df['employment_status_Self-Employed'] = 1

    # Apply feature scaling
    df = handle_scaling(input_dict['Age'], df)

    return df


def handle_scaling(age, df):
    if age <= 25:
        scaler_object = scaler_young
    else:
        scaler_object = scaler_rest

    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']

    df['income_level'] = None  # Placeholder column for scaling
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    df.drop('income_level', axis="columns", inplace=True)

    return df


def predict(input_dict):
    input_df = preprocess_input(input_dict)

    if input_dict['Age'] <= 25:
        prediction = model_young.predict(input_df)
    else:
        prediction = model_rest.predict(input_df)

    return int(prediction)
