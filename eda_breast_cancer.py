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


def run_eda_breast_cancer_app():
    st.subheader("From Exploratory Data Analysis")
    df = load_data("data/breastCancer.csv")
    df_encode = load_data("data/breast_cancer_cleaned.csv")
    freq_df= load_data("data/freqdist_of_age_data.csv")
    

    submenu = st.sidebar.selectbox("Submenu",['Descriptive','Plots'])


# descriptive structure
    if submenu == "Descriptive":
        st.subheader("Descriptive")
        st.dataframe(df)

        with st.expander("Descriptive Summary"):
            st.dataframe(df_encode.describe())


# plot structure
    elif submenu == "Plots":
        st.subheader("Plots")
        
            
        with st.expander("Pair plot Visual"):
            #splitting the data into the different types of class
            benign = df_encode[df_encode['class']==2]
            malignant = df_encode[df_encode['class']==4]

            column_list = df_encode.columns.tolist()
            column_choice1 = st.multiselect("Choose X-axis", column_list, default='clump_thickness')
            column_choice2 = st.multiselect("Choose Y-axis", column_list, default='marginal_adhesion')

            # plotting the visuals
            fig = plt.figure(figsize=(10,5))
            
            plt.xlabel(column_choice1)
            plt.ylabel(column_choice2)
            plt.title('Correlation Plot between {} and {} \n [Green: Malignant, Blue: Benign]'.format(column_choice1,column_choice2))
            plt.scatter(benign[column_choice1], benign[column_choice2], color='green',marker='.')
            plt.scatter(malignant[column_choice1], malignant[column_choice2], color='blue', marker ='.')  
            st.pyplot(fig)
 
    # Outlier Detection
        with st.expander("Outlier Detection Plot"):
            p3 = px.box(df_encode)
            st.plotly_chart(p3)

        # Correlation Plot
        with st.expander("Heatmap"):
            corr_matrix = df_encode.corr()
            fig = plt.figure(figsize=(20,10))
            sns.heatmap(corr_matrix, annot=True)
            st.pyplot(fig)


            p4 = px.imshow(corr_matrix)
            st.plotly_chart(p4)