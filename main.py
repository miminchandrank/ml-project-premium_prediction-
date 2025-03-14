# import streamlit as st
# from prediction_helper import predict
#
# st.set_page_config(page_title="Health Insurance Cost Predictor", layout="wide")
#
# # Custom CSS for refined design
# st.markdown("""
#     <style>
#         .stTextInput>div>div>input, .stSelectbox>div>div>select {
#             border-radius: 10px;
#             padding: 8px;
#             font-size: 16px;
#         }
#         .stNumberInput>div>div>input {
#             border-radius: 10px;
#             padding: 8px;
#             font-size: 16px;
#         }
#         .stButton>button {
#             background-color: #204F79;
#             color: white;
#             border-radius: 8px;
#             padding: 10px;
#             font-size: 16px;
#         }
#     </style>
# """, unsafe_allow_html=True)
#
# st.markdown("<h1 style='text-align: center; color: #204F79;'>Health Insurance Cost Predictor</h1>", unsafe_allow_html=True)
#
# # Dictionary to store inputs
# input_dict = {}
#
# col1, col2, col3 = st.columns(3)
#
# with col1:
#     input_dict["Age"] = st.number_input("Age", min_value=18, max_value=100, value=18, step=1)
#     input_dict["Genetical Risk"] = st.number_input("Genetical Risk", min_value=0, max_value=10, value=0, step=1)
#     input_dict["Gender"] = st.selectbox("Gender", ["Male", "Female"])
#     input_dict["Smoking Status"] = st.selectbox("Smoking Status", ["Regular", "Occasional", "Non Smoker"])
#
# with col2:
#     input_dict["Number of Dependants"] = st.number_input("Number of Dependants", min_value=0, max_value=10, value=0, step=1)
#     input_dict["Insurance Plan"] = st.selectbox("Insurance Plan", ["Bronze", "Silver", "Gold"])
#     input_dict["Marital Status"] = st.selectbox("Marital Status", ["Unmarried", "Married"])
#     input_dict["Region"] = st.selectbox("Region", ["Northwest", "Northeast", "Southwest", "Southeast"])
#
# with col3:
#     input_dict["Income in Lakhs"] = st.number_input("Income in Lakhs", min_value=0, max_value=100, value=0, step=1)
#     input_dict["Employment Status"] = st.selectbox("Employment Status", ["Salaried", "Self-Employed", "Freelancer"])
#     input_dict["BMI Category"] = st.selectbox("BMI Category", ["Underweight", "Normal", "Overweight", "Obese"])
#     input_dict["Medical History"] = st.selectbox("Medical History", [
#         "No Disease", "Diabetes", "High blood pressure",
#         "Diabetes & High blood pressure", "Thyroid",
#         "Heart disease", "High blood pressure & Heart disease",
#         "Diabetes & Thyroid", "Diabetes & Heart disease"
#     ])
#
# if st.button("Predict"):
#     prediction = predict(input_dict)
#     st.success(f"Predicted Premium: {prediction}")


import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Health Insurance Cost Predictor", layout="wide")

# Custom CSS for refined design
st.markdown("""
    <style>
        .stTextInput>div>div>input, .stSelectbox>div>div>select {
            border-radius: 10px;
            padding: 8px;
            font-size: 16px;
        }
        .stNumberInput>div>div>input {
            border-radius: 10px;
            padding: 8px;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #204F79;
            color: white;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #204F79;'>Health Insurance Cost Predictor</h1>", unsafe_allow_html=True)

# Dictionary to store inputs
input_dict = {}

col1, col2, col3 = st.columns(3)

with col1:
    input_dict["Age"] = st.number_input("Age", min_value=18, max_value=100, value=18, step=1)
    input_dict["Genetical Risk"] = st.number_input("Genetical Risk", min_value=0, max_value=10, value=0, step=1)
    input_dict["Gender"] = st.selectbox("Gender", ["Male", "Female"])
    input_dict["Smoking Status"] = st.selectbox("Smoking Status", ["Regular", "Occasional", "Non Smoker"])

with col2:
    input_dict["Number of Dependants"] = st.number_input("Number of Dependants", min_value=0, max_value=10, value=0, step=1)
    input_dict["Insurance Plan"] = st.selectbox("Insurance Plan", ["Bronze", "Silver", "Gold"])
    input_dict["Marital Status"] = st.selectbox("Marital Status", ["Unmarried", "Married"])
    input_dict["Region"] = st.selectbox("Region", ["Northwest", "Northeast", "Southwest", "Southeast"])

with col3:
    input_dict["Income in Lakhs"] = st.number_input("Income in Lakhs", min_value=0, max_value=100, value=0, step=1)
    input_dict["Employment Status"] = st.selectbox("Employment Status", ["Salaried", "Self-Employed", "Freelancer"])
    input_dict["BMI Category"] = st.selectbox("BMI Category", ["Underweight", "Normal", "Overweight", "Obese"])
    input_dict["Medical History"] = st.selectbox("Medical History", [
        "No Disease", "Diabetes", "High blood pressure",
        "Diabetes & High blood pressure", "Thyroid",
        "Heart disease", "High blood pressure & Heart disease",
        "Diabetes & Thyroid", "Diabetes & Heart disease"
    ])

if st.button("Predict"):
    prediction = predict(input_dict)
    st.success(f"Predicted Premium: {prediction}")
