import streamlit as st
import streamlit.components.v1 as stc


from ml_customer_pred import run_ml_customer_pred_app
from eda_customer_pred import run_eda_customer_pred_app
from eda_breast_cancer import run_eda_breast_cancer_app
from ml_breast_cancer import run_ml_breast_cancer_app
from eda_diabetes_type2 import run_eda_diabetes_type2_app2
from eda import run_eda_app
from ml import run_ml_app
from ml_diabetes_type2 import run_ml__diabetes_type2_app

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Predictions App </h1>
		<h4 style="color:white;text-align:center;">by:  Tobi-DataDetective </h4>
		</div>
		"""
stc.html(html_temp)

def main():
    # st.title('Main App')
    

    tabs = st.sidebar.selectbox("Choose Prediction",['Diabetes Prediction Type 1',
                                                        'Diabetes Prediction Type 2',
                                                        'Breast Cancer Prediction',
                                                        "Customer Subscription Prediction"])
# Diabetes Prediction type 1
    if tabs == "Diabetes Prediction Type 1":
    
        menu = ["HOME","EDA","ML"]
        choice = st.sidebar.selectbox("Diabetes Prediction Type 1", menu)

        if choice == "HOME":
            # st.subheader("Home")
            st.write("""
                ### Early Stage Diabetes Risk Predictor App
                This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
                #### Data Source
                    - https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
                #### App Content
                    - EDA Section: Exploratory Data Analysis of Data
                        - Descriptive Section
                        - Plots
                    - ML Section: ML Predictor App

                """)
        elif choice == "EDA":
            run_eda_app()

        elif choice == "ML":
            run_ml_app()    
        
        pass

# Diabetes Prediction Type 2
    elif tabs == "Diabetes Prediction Type 2":
            # creating new menu widget
        # stc.html(html_temp)

        menu = ["HOME","EDA","ML"]
        choice = st.sidebar.selectbox("Diabetes Prediction Type 2", menu)

        if choice == "HOME":
            # st.subheader("Home")
            st.write("""
                ### Early Stage Diabetes Risk Predictor App
                This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
                #### Data Source
                    - https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
                #### App Content
                    - EDA Section: Exploratory Data Analysis of Data
                        - Descriptive Section
                        - Plots
                    - ML Section: ML Predictor App

                """)
        elif choice == "EDA":
            run_eda_diabetes_type2_app2()

        elif choice == "ML":
            run_ml__diabetes_type2_app()

        
        
        pass

    # Breast Cancer app
    elif tabs == "Breast Cancer Prediction":
            # creating new menu widget
        # stc.html(html_temp)

        menu = ["HOME","EDA","ML"]
        choice = st.sidebar.selectbox("Breast Cancer Prediction", menu)

        if choice == "HOME":
            # st.subheader("Home")
            st.write("""
                ### Breast Cancer Risk Predictor App
                This dataset contains the sign and symptoms data of malignant beast cancer or benign breast cancer patient.
                #### Data source
                    - https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
                #### App Content
                    - EDA Section: Exploratory Data Analysis of Data
                        - Descriptive Section
                        - Plots
                    - ML Section: ML Predictor App

                """)
        elif choice == "EDA":
            run_eda_breast_cancer_app()

        elif choice == "ML":
            run_ml_breast_cancer_app()

        
        
        pass

    # Customer subscription app
    elif tabs == "Customer Subscription Prediction":
            # creating new menu widget
        # stc.html(html_temp)

        menu = ["HOME","EDA","ML"]
        choice = st.sidebar.selectbox("Customer Subscription Prediction", menu)

        if choice == "HOME":
            # st.subheader("Home")
            st.write("""
                ### Breast Cancer Risk Predictor App
                This dataset contains the sign and symptoms data of malignant beast cancer or benign breast cancer patient.
                #### Data source
                    - https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
                #### App Content
                    - EDA Section: Exploratory Data Analysis of Data
                        - Descriptive Section
                        - Plots
                    - ML Section: ML Predictor App

                """)
        elif choice == "EDA":
            run_eda_customer_pred_app()

        elif choice == "ML":
            run_ml_customer_pred_app()

        
        
        pass
    



if __name__ == '__main__':
    main()



    
    
