from pandas.core.indexes.period import period_range
import streamlit as st
# load dataviz package

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px

import pandas as pd


#function to load dataset
@st.cache
def load_data(data):
    df = pd.read_csv(data)
    return(df)


def run_eda_diabetes_type2_app2():
    st.subheader("From Exploratory Data Analysis")
    df = load_data("data/diabetes.csv")
    df_encode = load_data("data/diabetes_data_upload_clean.csv")
    freq_df= load_data("data/freqdist_of_age_data.csv")
    

    submenu = st.sidebar.selectbox("Submenu",['Descriptive','Plots'])


# descriptive structure
    if submenu == "Descriptive":
        st.subheader("Descriptive")
        st.dataframe(df)

        with st.expander("Descriptive Summary"):
            st.dataframe(df.describe())


# plot structure
    elif submenu == "Plots":
        st.subheader("Plots")
        
            
        with st.expander("Pair plot Visual"):
            #splitting the data into the different types of outcomes
            diabetes = df[df['Outcome']==1]
            No_diabetes = df[df['Outcome']==0]

            column_list = df.columns.tolist()
            column_choice1 = st.multiselect("Choose X-axis", column_list, default='Pregnancies')
            column_choice2 = st.multiselect("Choose Y-axis", column_list, default='Glucose')

            # plotting the visuals
            fig = plt.figure(figsize=(10,5))
            
            plt.xlabel(column_choice1)
            plt.ylabel(column_choice2)
            plt.title('Correlation Plot between {} and {}  [Green:positive, Blue: Negative]'.format(column_choice1,column_choice2))
            plt.scatter(diabetes[column_choice1], diabetes[column_choice2], color='green',marker='.')
            plt.scatter(No_diabetes[column_choice1], No_diabetes[column_choice2], color='blue', marker ='.')  
            st.pyplot(fig)
 
    # Outlier Detection
        with st.expander("Outlier Detection Plot"):
            p3 = px.box(df)
            st.plotly_chart(p3)

        # Correlation Plot
        with st.expander("Heatmap"):
            corr_matrix = df.corr()
            fig = plt.figure(figsize=(20,10))
            sns.heatmap(corr_matrix, annot=True)
            st.pyplot(fig)


            p4 = px.imshow(corr_matrix)
            st.plotly_chart(p4)