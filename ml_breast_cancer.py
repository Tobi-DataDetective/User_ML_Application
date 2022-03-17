from ipython_genutils.py3compat import with_metaclass
import streamlit as st

import pandas as pd

import joblib
import os

import numpy as np
from streamlit.proto.Radio_pb2 import Radio

attrib_info = """
   #####  Attribute                     Domain
   -- -----------------------------------------
    - Clump Thickness               1 - 10
    - Uniformity of Cell Size       1 - 10
    - Uniformity of Cell Shape      1 - 10
    - Marginal Adhesion             1 - 10
    - Single Epithelial Cell Size   1 - 10
    - Bare Nuclei                   1 - 10
    - Bland Chromatin               1 - 10
    - Normal Nucleoli               1 - 10
    - Mitoses                       1 - 10
    - Class:                        (2 for benign, 4 for malignant)

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
@st.cache(allow_output_mutation=True)
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


def run_ml_breast_cancer_app():
    st.subheader("ML Prediction")

    # adding the attribute information

    with st.expander("Attribute Info"):
        st.markdown(attrib_info)

    
    # Layout
    col1,col2 = st.columns(2)

    with col1:
        clump_thickness = st.number_input("clump_thickness",1,10)
        size_uniformity = st.number_input("size_uniformity",1,10)
        shape_uniformity = st.number_input("shape_uniformity",1,10)
        marginal_adhesion = st.number_input("marginal_adhesion",1,10)
        epithelial_size = st.number_input("epithelial_size",1,10)
        

    with col2:
        bare_nucleoli = st.number_input("bare_nucleoli",1,10)
        bland_chromatin = st.number_input("bland_chromatin",1,10)
        normal_nucleoli = st.number_input("normal_nucleoli",1,10)
        mitoses = st.number_input("mitoses",1,10)


    # result display
    with st.expander("Your Selected Options"):
	    result = {'clump_thickness':clump_thickness,
		'size_uniformity':size_uniformity,
		'shape_uniformity':shape_uniformity,
		'marginal_adhesion':marginal_adhesion,
		'epithelial_size':epithelial_size,
		'bare_nucleoli':bare_nucleoli,
		'bland_chromatin':bland_chromatin,
		'normal_nucleoli':normal_nucleoli,
		'mitoses':mitoses}
	    st.write(result)

	    encoded_result = []
	    for i in result.values():
		    encoded_result.append(i)
    # st.write(encoded_result)

		
    # model usage
    # with st.expander("Prediction Result"):
    single_sample = np.array(encoded_result).reshape(1,-1)
    # st.write(single_sample)

    model = load_model("models/KNN_Breast_Cancer_26_Feb_2022.pkl")
    prediction = model.predict(single_sample)
    pred_prob = model.predict_proba(single_sample)
    # st.write(prediction)
    # st.write(pred_prob)

    if prediction == 4:
        st.warning("Using KNN: Positive Risk {}".format(prediction[0]))
        pred_probability_score = {"Negative Risk":pred_prob[0][0]*100,"Positive Risk":pred_prob[0][1]*100}
        st.write(pred_probability_score)
    else:
        st.success("Using KNN: Negative Risk {}".format(prediction[0]))
        pred_probability_score = {"Negative Risk":pred_prob[0][0]*100,"Positive Risk":pred_prob[0][1]*100}
        st.write(pred_probability_score)


    model2 = load_model("models/SVC_Breast_Cancer_26_Feb_2022.pkl")
    prediction2 = model2.predict(single_sample)
    pred_prob2 = model.predict_proba(single_sample)
    # st.write(prediction)
    # st.write(pred_prob2)

    if prediction2 == 4:
        st.warning("Using SVM: Positive Risk {}".format(prediction2[0]))
        pred_prob2ability_score = {"Negative Risk":pred_prob2[0][0]*100,"Positive Risk":pred_prob2[0][1]*100}
        st.write(pred_prob2ability_score)
    else:
        st.success("Using SVM: Negative Risk {}".format(prediction2[0]))
        pred_prob2ability_score = {"Negative Risk":pred_prob2[0][0]*100,"Positive Risk":pred_prob2[0][1]*100}
        st.write(pred_prob2ability_score)