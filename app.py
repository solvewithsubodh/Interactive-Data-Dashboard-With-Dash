# ================= IMPORT LIBRARIES =================
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Teen Mental Health Dashboard",
    page_icon="📊",
    layout="wide"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #161A23, #0E1117);
    border-right: 1px solid #2A2A2A;
}

/* Headings */
h1, h2, h3 {
    color: white;
    font-weight: bold;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-size: 18px;
    padding: 12px;
    font-weight: bold;
}

/* Dataframe */
div[data-testid="stDataFrame"] {
    border: 1px solid #FF4B4B;
    border-radius: 12px;
    padding: 5px;
    background-color: #111111;
}

/* Download Button */
.stDownloadButton button {
    background-color: #FF4B4B;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
}

.stDownloadButton button:hover {
    background-color: #ff1f1f;
    color: white;
}

/* Smooth animation */
div[data-testid="metric-container"] {
    transition: 0.3s;
}

div[data-testid="metric-container"]:hover {
    transform: scale(1.03);
}

</style>
""", unsafe_allow_html=True)

# ================= LOAD DATASET =================
df = pd.read_csv("Teen_Mental_Health_Dataset.csv")

# ================= SIDEBAR =================
st.sidebar.markdown("## ⚡ Filter Dashboard")

selected_gender = st.sidebar.selectbox(
    "Select Gender",
    df["gender"].unique()
)

selected_age = st.sidebar.slider(
    "Select Maximum Age",
    int(df["age"].min()),
    int(df["age"].max()),
    int(df["age"].max())
)

selected_platform = st.sidebar.selectbox(
    "Select Platform",
    df["platform_usage"].unique()
)

# ================= FILTER DATA =================
filtered_df = df[
    (df["gender"] == selected_gender) &
    (df["age"] <= selected_age) &
    (df["platform_usage"] == selected_platform)
]

# ================= METRICS =================
average_stress = filtered_df["stress_level"].mean()
average_anxiety = filtered_df["anxiety_level"].mean()
average_social_media = filtered_df["daily_social_media_hours"].mean()

# ================= HEADER =================
st.markdown("""
# 📊 Social Media Impact on Teen Mental Health
###  Analytics Dashboard for Teen Mental Health & Social Media Behavior
""")

st.caption(f"Last Updated: {datetime.now().strftime('%d %B %Y | %I:%M %p')}")

st.markdown("---")

# ================= TABS =================
tab1, tab2, tab3 = st.tabs([
    "🏠 Home",
    "📈 Analytics",
    "📂 Filtered Data"
])

# =========================================================
# ================= HOME TAB =================
# =========================================================

with tab1:

    st.markdown("## 🚀 Dashboard Overview")

    col1, col2, col3 = st.columns(3)

    # Stress Card
    with col1:
        st.markdown(f"""
        <div style='
        background: linear-gradient(135deg,#ff4b4b,#b30000);
        padding:30px;
        border-radius:20px;
        text-align:center;
        box-shadow:0 0 20px rgba(255,75,75,0.3);
        '>
        <h3 style='color:white;'>Average Stress</h3>
        <h1 style='color:white;'>{round(average_stress,2)}</h1>
        </div>
        """, unsafe_allow_html=True)

    # Anxiety Card
    with col2:
        st.markdown(f"""
        <div style='
        background: linear-gradient(135deg,#3B82F6,#1E3A8A);
        padding:30px;
        border-radius:20px;
        text-align:center;
        box-shadow:0 0 20px rgba(59,130,246,0.3);
        '>
        <h3 style='color:white;'>Average Anxiety</h3>
        <h1 style='color:white;'>{round(average_anxiety,2)}</h1>
        </div>
        """, unsafe_allow_html=True)

    # Social Media Card
    with col3:
        st.markdown(f"""
        <div style='
        background: linear-gradient(135deg,#22C55E,#15803D);
        padding:30px;
        border-radius:20px;
        text-align:center;
        box-shadow:0 0 20px rgba(34,197,94,0.3);
        '>
        <h3 style='color:white;'>Social Media Hours</h3>
        <h1 style='color:white;'>{round(average_social_media,2)}</h1>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Dataset Preview
    st.markdown("## 📄 Dataset Preview")

    st.dataframe(df.head(10), use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Dataset Shape
    st.markdown("## 📊 Dataset Shape")

    col4, col5 = st.columns(2)

    with col4:
        st.success(f"Rows: {df.shape[0]}")

    with col5:
        st.info(f"Columns: {df.shape[1]}")

# =========================================================
# ================= ANALYTICS TAB =================
# =========================================================

with tab2:

    # Gender Distribution
    st.markdown("## 👨‍👩‍👧 Gender Distribution")

    fig1, ax1 = plt.subplots(figsize=(7,4))

    ax1.set_facecolor("#111111")
    fig1.patch.set_facecolor("#111111")

    sns.countplot(
        x="gender",
        data=df,
        palette="coolwarm",
        ax=ax1
    )

    ax1.tick_params(colors='white')
    ax1.set_xlabel("Gender", color='white')
    ax1.set_ylabel("Count", color='white')

    st.pyplot(fig1)

    # Stress Level Distribution
    st.markdown("## 📈 Stress Level Distribution")

    fig2, ax2 = plt.subplots(figsize=(8,4))

    ax2.set_facecolor("#111111")
    fig2.patch.set_facecolor("#111111")

    sns.histplot(
        df["stress_level"],
        bins=10,
        kde=True,
        color="red",
        ax=ax2
    )

    ax2.tick_params(colors='white')

    st.pyplot(fig2)

    # Social Media Usage
    st.markdown("## 📱 Daily Social Media Usage")

    fig3, ax3 = plt.subplots(figsize=(8,4))

    ax3.set_facecolor("#111111")
    fig3.patch.set_facecolor("#111111")

    sns.histplot(
        df["daily_social_media_hours"],
        bins=10,
        kde=True,
        color="cyan",
        ax=ax3
    )

    ax3.tick_params(colors='white')

    st.pyplot(fig3)

    # Pie Chart
    st.markdown("## 🥧 Platform Usage Share")

    platform_counts = df["platform_usage"].value_counts()

    fig4, ax4 = plt.subplots(figsize=(6,6))

    fig4.patch.set_facecolor("#111111")

    ax4.pie(
        platform_counts,
        labels=platform_counts.index,
        autopct='%1.1f%%'
    )

    st.pyplot(fig4)

# =========================================================
# ================= FILTERED DATA TAB =================
# =========================================================

with tab3:

    st.markdown("## 📂 Filtered Dataset")

    st.dataframe(filtered_df, use_container_width=True)

    # Download Button
    csv = filtered_df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="📥 Download Filtered Report",
        data=csv,
        file_name="filtered_teen_mental_health_report.csv",
        mime="text/csv"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Filtered Stress Distribution
    st.markdown("## 📈 Filtered Stress Level Distribution")

    fig5, ax5 = plt.subplots(figsize=(10,4))

    ax5.set_facecolor("#111111")
    fig5.patch.set_facecolor("#111111")

    sns.histplot(
        filtered_df["stress_level"],
        bins=10,
        kde=True,
        color="orange",
        ax=ax5
    )

    ax5.tick_params(colors='white')

    st.pyplot(fig5)

# ================= FOOTER =================
st.markdown("---")

st.markdown("""
<center>
Made with ❤️ by Subodh Mundwadkar | Department of Electronics And Communication Engineering (Advanced Communication Technology)
</center>
""", unsafe_allow_html=True)