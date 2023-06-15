import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

uploaded_file = st.file_uploader("Upload a CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.write("Data first 5 rows",data.head())
    st.write("Data last 5 rows",data.tail())
    st.write("Rows:", data.shape[0])
    st.write("Columns:", data.shape[1])
    st.write("Size", data.size)
    st.write("Data Types" , data.dtypes)

    choice = st.selectbox("Pick one", data.columns)

    if choice:
        choice_data = data[choice]

        if choice_data.dtype in ['int64', 'float64']:
            st.write("Select Data:", choice)
            st.write("Five Number Summary:")
            st.write(choice_data.describe())

            
            st.write("Distribution Plot")
            fig, ax = plt.subplots()
            sns.histplot(choice_data, kde=True, ax=ax)
            ax.set_xlabel(choice)
            ax.set_ylabel("Count")
            st.pyplot(fig)

        elif choice_data.dtype == 'object':
            st.write("Select Data:", choice)
            st.write("Table the proportions of each category level:")
            count = choice_data.value_counts(normalize=True)
            st.write(count)

            st.subheader("Barplot")
            fig, ax = plt.subplots()
            sns.barplot(x=count.index, y=count.values, ax=ax)
            ax.set_xlabel(choice)
            ax.set_ylabel("Proportion")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
            st.pyplot(fig)