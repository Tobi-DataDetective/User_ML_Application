from ipython_genutils.py3compat import with_metaclass
import streamlit as st

import pandas as pd

import joblib
import os

import numpy as np
from streamlit.proto.Radio_pb2 import Radio

attrib_info = """
#### Attribute Information:
    - Age 1.20-65
    - Sex 1. Male, 2.Female
    - Polyuria 1.Yes, 2.No.
    - Polydipsia 1.Yes, 2.No.
    - sudden weight loss 1.Yes, 2.No.
    - weakness 1.Yes, 2.No.
    - Polyphagia 1.Yes, 2.No.
    - Genital thrush 1.Yes, 2.No.
    - visual blurring 1.Yes, 2.No.
    - Itching 1.Yes, 2.No.
    - Irritability 1.Yes, 2.No.
    - delayed healing 1.Yes, 2.No.
    - partial paresis 1.Yes, 2.No.
    - muscle stiness 1.Yes, 2.No.
    - Alopecia 1.Yes, 2.No.
    - Obesity 1.Yes, 2.No.
    - Class 1.Positive, 2.Negative.

"""
label_dict = {"No":0,"Yes":1}
gender_map = {"Female":0,"Male":1}
target_label_map = {"Negative":0,"Positive":1}

def get_fvalue(val):
	feature_dict = {"No":0,"Yes":1}
	for key,value in feature_dict.items():
		if val == key:
			return value 

def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value 

# Load ML Models
@st.cache
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


def run_ml__diabetes_type2_app():
    st.subheader("ML Prediction")

    # adding the attribute information

    with st.expander("Attribute Info"):
        st.markdown(attrib_info)

    
    # Layout
    col1,col2 = st.columns(2)

    with col1:
        Pregnancies = st.number_input("Pregnancies")
        Glucose = st.number_input("Glucose")
        BloodPressure = st.number_input("BloodPressure")
        SkinThickness = st.number_input("SkinThickness")



    with col2:
        Insulin = st.number_input("Insulin")
        BMI = st.number_input("BMI")
        DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction")
        Age = st.number_input("Age")

    # input display
    with st.expander("Your Selected Options"):
	    result = {'Pregnancies':Pregnancies,
		'Glucose':Glucose,
		'BloodPressure':BloodPressure,
		'SkinThickness':SkinThickness,
		'Insulin':Insulin,
		'BMI':BMI,
		'DiabetesPedigreeFunction':DiabetesPedigreeFunction,
		'Age':Age}
	    st.write(result)

	    encoded_result = []
	    for i in result.values():
		    encoded_result.append(i)
    # st.write(encoded_result)

		
    # model usage
    # with st.expander("Prediction Result"):
    single_sample = np.array(encoded_result).reshape(1,-1)
    # st.write(single_sample)

    model = load_model("models/SVM_model_diabetes_25_Feb_2022.pkl")
    prediction = model.predict(single_sample)
    # pred_prob = model.predict_proba(single_sample)
    # st.write(prediction)
    # st.write(pred_prob)

    if prediction == 1:
        st.warning("Positive Risk {}".format(prediction[0]))
        # pred_probability_score = {"Negative DM Risk":pred_prob[0][0]*100,"Positive DM Risk":pred_prob[0][1]*100}
        # st.write(pred_probability_score)
    else:
        st.success("Negative Risk {}".format(prediction[0]))
        # pred_probability_score = {"Negative DM Risk":pred_prob[0][0]*100,"Positive DM Risk":pred_prob[0][1]*100}
        # st.write(pred_probability_score)