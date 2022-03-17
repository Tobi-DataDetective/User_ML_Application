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


def run_ml_customer_pred_app():
    st.subheader("ML Prediction")

    # adding the attribute information

    with st.expander("Attribute Info"):
        st.markdown(attrib_info)

    
    # Layout
    col1,col2 = st.columns(2)

    with col1:
        dayofweek = st.number_input("dayofweek")
        hour = st.number_input("hour")
        age = st.number_input("age")
        numscreens = st.number_input("numscreens")
        minigame = st.number_input("minigame")
        liked = st.number_input("liked")
        used_premium_feature = st.number_input("used_premium_feature")
        location = st.number_input("location")
        Institutions = st.number_input("Institutions")
        VerifyPhone = st.number_input("VerifyPhone")
        BankVerification = st.number_input("BankVerification")
        VerifyDateOfBirth = st.number_input("VerifyDateOfBirth")
        ProfilePage = st.number_input("ProfilePage")
        VerifyCountry = st.number_input("VerifyCountry")
        Cycle = st.number_input("Cycle")
        idscreen = st.number_input("idscreen")
        Splash = st.number_input("Splash")
        RewardsContainer = st.number_input("RewardsContainer")
        EditProfile = st.number_input("EditProfile")
        Finances = st.number_input("Finances")
        Alerts = st.number_input("Alerts")
        Leaderboard = st.number_input("Leaderboard")
        VerifyMobile = st.number_input("VerifyMobile")
        VerifyHousing = st.number_input("VerifyHousing")
        

    with col2:
        RewardDetail = st.number_input("RewardDetail")
        VerifyHousingAmount = st.number_input("VerifyHousingAmount")
        ProfileMaritalStatus = st.number_input("ProfileMaritalStatus")
        ProfileChildren  = st.number_input("ProfileChildren ")
        ProfileEducation = st.number_input("ProfileEducation")
        ProfileEducationMajor = st.number_input("ProfileEducationMajor")
        Rewards = st.number_input("Rewards")
        AccountView = st.number_input("AccountView")
        VerifyAnnualIncome = st.number_input("VerifyAnnualIncome")
        VerifyIncomeType = st.number_input("VerifyIncomeType")
        ProfileJobTitle = st.number_input("ProfileJobTitle")
        Login = st.number_input("Login")
        ProfileEmploymentLength = st.number_input("ProfileEmploymentLength")
        WebView = st.number_input("WebView")
        SecurityModal = st.number_input("SecurityModal")
        ResendToken = st.number_input("ResendToken")
        TransactionList = st.number_input("TransactionList")
        NetworkFailure = st.number_input("NetworkFailure")
        ListPicker = st.number_input("ListPicker")
        other = st.number_input("other")
        savingscount = st.number_input("savingscount")
        CMCount = st.number_input("CMCount")
        CCCount = st.number_input("CCCount")
        LoansCount = st.number_input("LoansCount")


    # result display
    with st.expander("Your Selected Options"):
	    result = {"dayofweek":dayofweek,
        "hour":hour,
        "age":age,
        "numscreens":numscreens,
        "minigame":minigame,
        "liked":liked,
        "used_premium_feature":used_premium_feature,
        "location":location,
        "Institutions":Institutions,
        "VerifyPhone":VerifyPhone,
        "BankVerification":BankVerification,
        "VerifyDateOfBirth":VerifyDateOfBirth,
        "ProfilePage":ProfilePage,
        "VerifyCountry":VerifyCountry,
        "Cycle":Cycle,
        "idscreen":idscreen,
        "Splash":Splash,
        "RewardsContainer":RewardsContainer,
        "EditProfile":EditProfile,
        "Finances":Finances,
        "Alerts":Alerts,
        "Leaderboard":Leaderboard,
        "VerifyMobile":VerifyMobile,
        "VerifyHousing":VerifyHousing,
        "RewardDetail":RewardDetail,
        "VerifyHousingAmount":VerifyHousingAmount,
        "ProfileMaritalStatus":ProfileMaritalStatus,
        "ProfileChildren" :ProfileChildren ,
        "ProfileEducation":ProfileEducation,
        "ProfileEducationMajor":ProfileEducationMajor,
        "Rewards":Rewards,
        "AccountView":AccountView,
        "VerifyAnnualIncome":VerifyAnnualIncome,
        "VerifyIncomeType":VerifyIncomeType,
        "ProfileJobTitle":ProfileJobTitle,
        "Login":Login,
        "ProfileEmploymentLength":ProfileEmploymentLength,
        "WebView":WebView,
        "SecurityModal":SecurityModal,
        "ResendToken":ResendToken,
        "TransactionList":TransactionList,
        "NetworkFailure":NetworkFailure,
        "ListPicker":ListPicker,
        "other":other,
        "savingscount":savingscount,
        "CMCount":CMCount,
        "CCCount":CCCount,
        "LoansCount":LoansCount}
	    st.write(result)

	    encoded_result = []
	    for i in result.values():
		    encoded_result.append(i)
    # st.write(encoded_result)

		
    # model usage
    # with st.expander("Prediction Result"):
    single_sample = np.array(encoded_result).reshape(1,-1)
    # st.write(single_sample)

    model = load_model("models/logistic_Customer_subscription_prediction_Nov_2021.pkl")
    prediction = model.predict(single_sample)
    pred_prob = model.predict_proba(single_sample)
    # st.write(prediction)
    # st.write(pred_prob)

    if prediction == 1:
        st.warning("Will Subscribe {}".format(prediction[0]))
        pred_probability_score = {"Will not subscribe":"{}%".format(round(pred_prob[0][0]*100,2)),"Will Subscribe":"{}%".format(round(pred_prob[0][1]*100,2))}
        st.write(pred_probability_score)
    else:
        st.success("Will not subscribe {}".format(prediction[0]))
        pred_probability_score = {"Will not subscribe":"{}%".format(round(pred_prob[0][0]*100,2)),"Will Subscribe":"{}%".format(round(pred_prob[0][1]*100,2))}
        st.write(pred_probability_score)


    