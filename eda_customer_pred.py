from pandas.core.indexes.period import period_range
import streamlit as st
# load dataviz package
import numpy as np

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


def run_eda_customer_pred_app():
    st.subheader("From Exploratory Data Analysis")
    df = load_data("data/appdata10.csv")
    df_encode = load_data("data/new_appdata10.csv")
    eda_df= load_data("data/appdata_for_eda.csv")
    top_screens = load_data("data/top_screens.csv")
    

    submenu = st.sidebar.selectbox("Submenu",['Descriptive','Plots'])


# descriptive structure
    if submenu == "Descriptive":
        st.subheader("Descriptive")
        st.dataframe(df)

        with st.expander("Descriptive Summary"):
            st.dataframe(df.describe())

        with st.expander("Top Screens Visited"):
            st.dataframe(top_screens)

        with st.expander("Data after prepocessing"):
            st.dataframe(df_encode)

# plot structure
    elif submenu == "Plots":
        st.subheader("Plots")
        
            
        with st.expander("Histogram of Numerical Columns"):
            fig = plt.figure(figsize=(15,15))
            plt.suptitle('Histogram of Numerical Columns', fontsize = 20)
            for i in range(1, eda_df.shape[1]+1): #columns to be plotted
                plt.subplot(3,3,i) # creating a 3 by 3 framed plot
                f = plt.gca() # clean up everthing, creats the field
                f.set_title(eda_df.columns.values[i - 1]) # namimg frames
                
                vals = np.size(eda_df.iloc[:, i - 1].unique()) #sum of unique values in each column
                
                plt.hist(eda_df.iloc[:, i - 1], bins = vals, color = '#3F5D7D') #plotting the histogram
        st.pyplot(fig)
            
    # Correlation with response variable
        with st.expander("Correlation with response variable"):
            fig = plt.figure()
            eda_df.corrwith(df.enrolled).plot.bar(figsize=(20,10),
                                      title = 'correlation with response variable',
                                      fontsize = 15, rot = 45,
                                      grid = True) #returns a numerical list of correlation between all the fields in this dataframe, with a list given as an argument
            st.pyplot(fig)

        # # Correlation Plot
        with st.expander("Heatmap"):
            corr_matrix = eda_df.corr()
            fig = plt.figure(figsize=(20,10))
            sns.heatmap(corr_matrix, annot=True)
            st.pyplot(fig)


            p4 = px.imshow(corr_matrix)
            st.plotly_chart(p4)