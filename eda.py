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


def run_eda_app():
    st.subheader("From Exploratory Data Analysis")
    df = load_data("data/diabetes_data_upload.csv")
    df_encode = load_data("data/diabetes_data_upload_clean.csv")
    freq_df= load_data("data/freqdist_of_age_data.csv")
    

    submenu = st.sidebar.selectbox("Submenu",['Descriptive','Plots'])


# descriptive structure
    if submenu == "Descriptive":
        st.subheader("Descriptive")
        st.dataframe(df)

        with st.expander("Descriptive Summary"):
            st.dataframe(df.describe())

        with st.expander("Class Distribution"):
            st.dataframe(df['class'].value_counts())

        with st.expander("Gender Distribution"):
            st.dataframe(df['Gender'].value_counts())    



# plot structure
    elif submenu == "Plots":
        st.subheader("Plots")
        
        col1,col2 = st.columns([2,1])

# col 1 plotting
        with col1:
            # Gender distribution
            with st.expander("Dist plot of Gender"):
                
                # fig = plt.figure()
                # sns.countplot(df['Gender'])
                # st.pyplot(fig)

                gen_df = df['Gender'].value_counts().to_frame()
                
                gen_df = gen_df.reset_index()
                gen_df.columns = ['Gender', 'Counts']
                # st.dataframe(gen_df)


                # pie chart
                p1 = px.pie(gen_df, names="Gender", values="Counts")
                st.plotly_chart(p1, use_container_width=True)

            # Class distribution
                
            with st.expander("Dist plot of Class"):
                
                fig = plt.figure()
                sns.countplot(df['class'])
                st.pyplot(fig)

               
# column 2 plotting
        with col2:
            # gender distribution
            with st.expander("Dist plot of Gender"):
                st.dataframe(gen_df)

            # class distribution
            with st.expander("Class Distribution"):
                st.dataframe(df['class'].value_counts())



        # Freq Distribution
        with st.expander("Frequency Distribution of Age"):
            # st.dataframe(freq_df)
            p2 = px.bar(freq_df, x='Age', y='count')
            st.plotly_chart(p2)

        # Outlier Detection
        with st.expander("Outlier Detection Plot"):
            # fig = plt.figure()
            # sns.boxplot(df['Age'])
            # st.pyplot(fig)

            p3 = px.box(df, x='Age', color='Gender')
            st.plotly_chart(p3)

        # Correlation Plot
        with st.expander("Correlation Plot"):
            corr_matrix = df_encode.corr()
            fig = plt.figure(figsize=(20,10))
            sns.heatmap(corr_matrix, annot=True)
            st.pyplot(fig)


            p4 = px.imshow(corr_matrix)
            st.plotly_chart(p4)