import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Teen_Mental_Health_Dataset.csv")

# Dashboard Title
st.title("Social Media Impact on Teen Mental Health")

# Show dataset
st.subheader("Dataset Preview")
st.write(df.head())

# Basic dataset info
st.subheader("Dataset Shape")
st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

# Gender distribution chart
st.subheader("Gender Distribution")

fig, ax = plt.subplots()
sns.countplot(x="gender", data=df, ax=ax)

st.pyplot(fig)

# Stress level chart
st.subheader("Stress Level Distribution")

fig2, ax2 = plt.subplots()
sns.histplot(df["stress_level"], bins=10, kde=True, ax=ax2)

st.pyplot(fig2)

# Social media usage
st.subheader("Daily Social Media Usage")

fig3, ax3 = plt.subplots()
sns.histplot(df["daily_social_media_hours"], bins=10, kde=True, ax=ax3)

st.pyplot(fig3)
# Sidebar filters
st.sidebar.header("Filter Data")

# Gender filter
selected_gender = st.sidebar.selectbox(
    "Select Gender",
    df["gender"].unique()
)

# Age slider
selected_age = st.sidebar.slider(
    "Select Maximum Age",
    int(df["age"].min()),
    int(df["age"].max()),
    int(df["age"].max())
)

# Filtered dataframe
filtered_df = df[
    (df["gender"] == selected_gender) &
    (df["age"] <= selected_age)
]

# Show filtered data
st.subheader("Filtered Dataset")
st.write(filtered_df)

# Filtered stress chart
st.subheader("Filtered Stress Level Distribution")

fig4, ax4 = plt.subplots()
sns.histplot(filtered_df["stress_level"], bins=10, kde=True, ax=ax4)

st.pyplot(fig4)