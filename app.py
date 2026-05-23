import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Teen_Mental_Health_Dataset.csv")

# Dashboard Title
st.title("Social Media Impact on Teen Mental Health")

# Create Tabs
tab1, tab2, tab3 = st.tabs([
    "Home",
    "Analytics",
    "Filtered Data"
])

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

# Platform filter
selected_platform = st.sidebar.selectbox(
    "Select Platform",
    df["platform_usage"].unique()
)

# Filtered dataframe
filtered_df = df[
    (df["gender"] == selected_gender) &
    (df["age"] <= selected_age) &
    (df["platform_usage"] == selected_platform)
]

# Dynamic Metrics
average_stress = filtered_df["stress_level"].mean()
average_anxiety = filtered_df["anxiety_level"].mean()
average_social_media = filtered_df["daily_social_media_hours"].mean()

# ---------------- HOME TAB ----------------
with tab1:

    st.subheader("Dataset Preview")
    st.write(df.head())

    st.subheader("Dataset Shape")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    st.subheader("Dynamic Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Stress Level", round(average_stress, 2))
    col2.metric("Average Anxiety Level", round(average_anxiety, 2))
    col3.metric("Average Social Media Hours", round(average_social_media, 2))

# ---------------- ANALYTICS TAB ----------------
with tab2:

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

# ---------------- FILTERED DATA TAB ----------------
with tab3:

    # Show filtered data
    st.subheader("Filtered Dataset")
    st.write(filtered_df)

    # Filtered stress chart
    st.subheader("Filtered Stress Level Distribution")

    fig4, ax4 = plt.subplots()
    sns.histplot(filtered_df["stress_level"], bins=10, kde=True, ax=ax4)

    st.pyplot(fig4)