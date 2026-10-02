import streamlit as st
import pandas as pd
import numpy as np
import joblib


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Sepsis Intelligence",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# BLUE + PINK DASHBOARD THEME
# =========================================================

st.markdown("""
<style>

/* ================================
   MAIN BACKGROUND
================================ */

.stApp {
    background:
        radial-gradient(
            circle at top right,
            rgba(255, 55, 150, 0.18),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #06152F 0%,
            #092B5C 55%,
            #32133F 100%
        );
}


/* ================================
   SIDEBAR
================================ */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #041126,
        #0A2148
    );
    border-right: 1px solid rgba(255,255,255,0.12);
}

section[data-testid="stSidebar"] * {
    color: #EAF4FF !important;
}


/* ================================
   TITLE
================================ */

.main-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    color: white;
    margin-top: 10px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #B9D9FF;
    font-size: 17px;
    margin-bottom: 25px;
}


/* ================================
   DASHBOARD CARDS
================================ */

.dashboard-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.13);
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 15px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.22);
}


/* ================================
   BLUE CARD
================================ */

.blue-card {
    background: linear-gradient(
        135deg,
        #1677FF,
        #0845A0
    );
    border-radius: 18px;
    padding: 22px;
    text-align: center;
    color: white;
    box-shadow: 0 8px 25px rgba(22,119,255,0.25);
}


/* ================================
   PINK CARD
================================ */

.pink-card {
    background: linear-gradient(
        135deg,
        #FF4FA3,
        #C91868
    );
    border-radius: 18px;
    padding: 22px;
    text-align: center;
    color: white;
    box-shadow: 0 8px 25px rgba(255,79,163,0.25);
}


/* ================================
   DARK CARD
================================ */

.dark-card {
    background: rgba(3,15,35,0.75);
    border-radius: 18px;
    padding: 22px;
    border: 1px solid rgba(255,255,255,0.10);
}


/* ================================
   TEXT
================================ */

h1, h2, h3 {
    color: #FFFFFF !important;
}

p {
    color: #DDEBFF;
}

label {
    color: #EAF4FF !important;
}


/* ================================
   BUTTON
================================ */

.stButton > button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #1677FF,
        #FF4FA3
    );
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-size: 16px;
    font-weight: 700;
    transition: 0.2s;
}

.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0 5px 20px rgba(255,79,163,0.30);
}


/* ================================
   METRICS
================================ */

[data-testid="stMetric"] {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 15px;
    padding: 15px;
}

[data-testid="stMetricLabel"] {
    color: #B9D9FF !important;
}

[data-testid="stMetricValue"] {
    color: white !important;
}


/* ================================
   INPUTS
================================ */

.stNumberInput input,
.stTextInput input {
    background: rgba(255,255,255,0.08);
    color: white;
    border-radius: 10px;
}


/* ================================
   DIVIDER
================================ */

hr {
    border-color: rgba(255,255,255,0.15);
}


/* ================================
   INFO BOX
================================ */

div[data-testid="stAlert"] {
    border-radius: 14px;
}


/* ================================
   FOOTER
================================ */

.footer {
    text-align: center;
    color: #8FB5E5;
    font-size: 13px;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    try:
        model = joblib.load("best_model.pkl")
        return model

    except Exception as e:

        st.error("❌ Could not load best_model.pkl")
        st.exception(e)
        return None


model = load_model()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🩺 AI SEPSIS INTELLIGENCE DASHBOARD</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Explainable • Uncertainty-Aware • Patient-Centered AI'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    "## 🩺 SEPSIS AI"
)

st.sidebar.markdown(
    "---"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👤 Patient Prediction",
        "🛡️ Data Reliability",
        "🧠 Uncertainty Analysis",
        "🚨 Alert Center",
        "ℹ️ About System"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Research Prototype\n\n"
    "AI-based sepsis risk assessment "
    "and decision-support system."
)


# =========================================================
# HOME DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    st.markdown(
        "## 🌐 AI Sepsis Decision-Support System"
    )

    st.write(
        "A patient-centered AI platform that combines "
        "sepsis prediction, uncertainty estimation, "
        "data reliability assessment and risk-based alerts."
    )

    st.divider()

    # TOP CARDS

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown(
            """
            <div class="blue-card">
                <h3>🧠 AI Prediction</h3>
                <p>Sepsis risk prediction</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            """
            <div class="pink-card">
                <h3>🔍 Explainable AI</h3>
                <p>Understand model decisions</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            """
            <div class="blue-card">
                <h3>🛡️ Reliability</h3>
                <p>Evaluate patient inputs</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:

        st.markdown(
            """
            <div class="pink-card">
                <h3>🚨 Alerts</h3>
                <p>Risk-based warning system</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader("🔄 System Workflow")

    workflow = [
        "Patient Data",
        "Data Reliability",
        "AI Prediction",
        "Risk Probability",
        "Uncertainty",
        "Explainability",
        "Risk Assessment",
        "Clinical Alert"
    ]

    cols = st.columns(4)

    for i, item in enumerate(workflow):

        with cols[i % 4]:

            st.markdown(
                f"""
                <div class="dashboard-card"
                     style="text-align:center;">
                    <h4>{item}</h4>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.divider()

    st.subheader("⭐ Project Uniqueness")

    u1, u2 = st.columns(2)

    with u1:

        st.markdown(
            """
            <div class="dark-card">

            <h3>Patient-Centered AI</h3>

            <p>
            The system does not stop at a simple
            Sepsis/No-Sepsis prediction.
            </p>

            <p>
            It evaluates risk, uncertainty,
            patient-data reliability and alerts.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with u2:

        st.markdown(
            """
            <div class="dark-card">

            <h3>Explainable Decision Support</h3>

            <p>
            The system is designed to show
            why a prediction was made and
            how reliable the prediction is.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# PATIENT PREDICTION
# =========================================================

elif page == "👤 Patient Prediction":

    st.header("👤 Patient Clinical Data")

    st.write(
        "Enter the patient's current clinical measurements."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    # -----------------------------------------------------
    # COLUMN 1
    # -----------------------------------------------------

    with col1:

        HR = st.number_input(
            "Heart Rate (HR)",
            min_value=0.0,
            value=85.0
        )

        O2Sat = st.number_input(
            "Oxygen Saturation (O2Sat)",
            min_value=0.0,
            max_value=100.0,
            value=98.0
        )

        Temp = st.number_input(
            "Temperature",
            value=37.0
        )

        SBP = st.number_input(
            "Systolic BP (SBP)",
            value=120.0
        )

    # -----------------------------------------------------
    # COLUMN 2
    # -----------------------------------------------------

    with col2:

        MAP = st.number_input(
            "Mean Arterial Pressure (MAP)",
            value=85.0
        )

        DBP = st.number_input(
            "Diastolic BP (DBP)",
            value=75.0
        )

        Resp = st.number_input(
            "Respiratory Rate",
            value=18.0
        )

        Age = st.number_input(
            "Age",
            min_value=0,
            value=45
        )

    # -----------------------------------------------------
    # COLUMN 3
    # -----------------------------------------------------

    with col3:

        Gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        ICULOS = st.number_input(
            "ICU Length of Stay",
            min_value=0,
            value=1
        )

        HospAdmTime = st.number_input(
            "Hospital Admission Time",
            value=-2.0
        )

        Glucose = st.number_input(
            "Glucose",
            value=110.0
        )

    # Gender encoding
    gender_value = 1 if Gender == "Male" else 0

    # -----------------------------------------------------
    # PATIENT DATAFRAME
    # -----------------------------------------------------

    patient_data = pd.DataFrame({

        "HR": [HR],
        "O2Sat": [O2Sat],
        "Temp": [Temp],
        "SBP": [SBP],
        "MAP": [MAP],
        "DBP": [DBP],
        "Resp": [Resp],
        "Age": [Age],
        "Gender": [gender_value],
        "ICULOS": [ICULOS],
        "HospAdmTime": [HospAdmTime],
        "Glucose": [Glucose]

    })

    st.divider()

    # -----------------------------------------------------
    # PREDICT BUTTON
    # -----------------------------------------------------

    if st.button(
        "🔍 ANALYZE SEPSIS RISK",
        type="primary"
    ):

        if model is None:

            st.error(
                "Model is not available."
            )

            st.stop()

        try:

            # =============================================
            # PREDICTION
            # =============================================

            prediction = model.predict(
                patient_data
            )[0]

            # =============================================
            # PROBABILITY
            # =============================================

            if hasattr(model, "predict_proba"):

                probability = model.predict_proba(
                    patient_data
                )[0][1]

            else:

                probability = float(prediction)

            risk_percentage = probability * 100

            # =============================================
            # RISK LEVEL
            # =============================================

            if risk_percentage >= 70:

                risk_level = "HIGH RISK"

            elif risk_percentage >= 30:

                risk_level = "MODERATE RISK"

            else:

                risk_level = "LOW RISK"


            # =============================================
            # RESULT HEADER
            # =============================================

            st.divider()

            st.header("📊 AI Prediction Result")

            r1, r2, r3 = st.columns(3)

            with r1:

                if prediction == 1:

                    st.markdown(
                        """
                        <div class="pink-card">
                            <h2>🚨 SEPSIS</h2>
                            <p>Potential risk detected</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                else:

                    st.markdown(
                        """
                        <div class="blue-card">
                            <h2>✅ NO SEPSIS</h2>
                            <p>No sepsis detected</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            with r2:

                st.metric(
                    "Sepsis Probability",
                    f"{risk_percentage:.2f}%"
                )

            with r3:

                st.metric(
                    "Risk Level",
                    risk_level
                )


            # =============================================
            # PROBABILITY BAR
            # =============================================

            st.subheader(
                "🎯 Sepsis Risk Score"
            )

            st.progress(
                min(
                    max(
                        int(risk_percentage),
                        0
                    ),
                    100
                )
            )

            st.write(
                f"Current estimated sepsis risk: "
                f"**{risk_percentage:.2f}%**"
            )


            # =============================================
            # UNCERTAINTY ANALYSIS
            # =============================================

            st.divider()

            st.header(
                "🧠 Uncertainty Analysis"
            )

            if hasattr(model, "estimators_"):

                tree_probabilities = []

                for tree in model.estimators_:

                    try:

                        tree_probability = (
                            tree.predict_proba(
                                patient_data
                            )[0][1]
                        )

                        tree_probabilities.append(
                            tree_probability
                        )

                    except Exception:
                        pass


                if len(tree_probabilities) > 0:

                    sepsis_votes = sum(
                        p >= 0.5
                        for p in tree_probabilities
                    )

                    total_trees = len(
                        tree_probabilities
                    )

                    no_sepsis_votes = (
                        total_trees -
                        sepsis_votes
                    )

                    agreement = (
                        max(
                            sepsis_votes,
                            no_sepsis_votes
                        )
                        /
                        total_trees
                    ) * 100

                    uncertainty = (
                        100 - agreement
                    )

                    uc1, uc2, uc3 = st.columns(3)

                    with uc1:

                        st.metric(
                            "Sepsis Tree Votes",
                            sepsis_votes
                        )

                    with uc2:

                        st.metric(
                            "No-Sepsis Tree Votes",
                            no_sepsis_votes
                        )

                    with uc3:

                        st.metric(
                            "Tree Agreement",
                            f"{agreement:.1f}%"
                        )

                    if uncertainty <= 10:

                        uncertainty_level = (
                            "VERY LOW UNCERTAINTY"
                        )

                    elif uncertainty <= 25:

                        uncertainty_level = (
                            "MODERATE UNCERTAINTY"
                        )

                    else:

                        uncertainty_level = (
                            "HIGH UNCERTAINTY"
                        )

                    st.info(
                        f"Uncertainty Score: "
                        f"{uncertainty:.1f}%  |  "
                        f"{uncertainty_level}"
                    )

                else:

                    st.info(
                        "Tree-level uncertainty "
                        "is not available for this model."
                    )

            else:

                st.info(
                    "Tree agreement is available "
                    "for Random Forest models."
                )


            # =============================================
            # DATA RELIABILITY
            # =============================================

            st.divider()

            st.header(
                "🛡️ Patient Data Reliability"
            )

            reliability_checks = []

            # HR
            reliability_checks.append(
                40 <= HR <= 180
            )

            # O2Sat
            reliability_checks.append(
                50 <= O2Sat <= 100
            )

            # Temperature
            reliability_checks.append(
                30 <= Temp <= 45
            )

            # SBP
            reliability_checks.append(
                40 <= SBP <= 250
            )

            # MAP
            reliability_checks.append(
                30 <= MAP <= 180
            )

            # DBP
            reliability_checks.append(
                20 <= DBP <= 150
            )

            # Resp
            reliability_checks.append(
                5 <= Resp <= 60
            )

            # Age
            reliability_checks.append(
                0 <= Age <= 120
            )

            # Glucose
            reliability_checks.append(
                20 <= Glucose <= 600
            )

            reliability_score = (
                sum(reliability_checks)
                /
                len(reliability_checks)
            ) * 100

            if reliability_score >= 90:

                reliability_status = (
                    "HIGH RELIABILITY"
                )

            elif reliability_score >= 70:

                reliability_status = (
                    "MODERATE RELIABILITY"
                )

            else:

                reliability_status = (
                    "LOW RELIABILITY"
                )

            rc1, rc2 = st.columns(2)

            with rc1:

                st.metric(
                    "Data Reliability",
                    f"{reliability_score:.1f}%"
                )

            with rc2:

                st.metric(
                    "Status",
                    reliability_status
                )


            # =============================================
            # ALERT SYSTEM
            # =============================================

            st.divider()

            st.header(
                "🚨 Clinical Alert Center"
            )

            if risk_percentage >= 70:

                st.error(
                    """
                    🚨 HIGH RISK ALERT

                    The model estimates a high sepsis risk.
                    Further clinical evaluation is recommended.
                    """
                )

            elif risk_percentage >= 30:

                st.warning(
                    """
                    ⚠️ MODERATE RISK

                    The patient shows an intermediate predicted
                    risk. Continue close monitoring.
                    """
                )

            else:

                st.success(
                    """
                    ✅ NO HIGH-RISK ALERT

                    The current predicted risk is low.
                    Continue routine monitoring.
                    """
                )


            # =============================================
            # CLINICAL REVIEW
            # =============================================

            st.divider()

            st.header(
                "👨‍⚕️ Clinical Review Recommendation"
            )

            if risk_percentage >= 70:

                st.warning(
                    "Clinical review recommended because "
                    "the predicted risk is high."
                )

            elif risk_percentage >= 30:

                st.info(
                    "Continue monitoring and consider "
                    "additional clinical assessment."
                )

            else:

                st.success(
                    "Prediction is suitable for routine "
                    "monitoring, subject to clinical judgment."
                )


            # =============================================
            # PATIENT DATA
            # =============================================

            st.divider()

            with st.expander(
                "📋 View Entered Patient Data"
            ):

                st.dataframe(
                    patient_data,
                    use_container_width=True
                )


        except Exception as e:

            st.error(
                "❌ Prediction could not be completed."
            )

            st.exception(e)


# =========================================================
# DATA RELIABILITY PAGE
# =========================================================

elif page == "🛡️ Data Reliability":

    st.header(
        "🛡️ Patient Data Reliability"
    )

    st.write(
        """
        This module checks whether entered clinical values
        fall within reasonable ranges before interpreting
        the model prediction.
        """
    )

    st.divider()

    reliability_table = pd.DataFrame({

        "Feature": [
            "Heart Rate",
            "O2 Saturation",
            "Temperature",
            "SBP",
            "MAP",
            "DBP",
            "Respiratory Rate",
            "Age",
            "Glucose"
        ],

        "Purpose": [
            "Checks cardiac measurement",
            "Checks oxygen measurement",
            "Checks temperature",
            "Checks systolic pressure",
            "Checks mean pressure",
            "Checks diastolic pressure",
            "Checks respiratory measurement",
            "Checks patient age",
            "Checks glucose measurement"
        ]

    })

    st.dataframe(
        reliability_table,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# UNCERTAINTY PAGE
# =========================================================

elif page == "🧠 Uncertainty Analysis":

    st.header(
        "🧠 Uncertainty-Aware Prediction"
    )

    st.write(
        """
        Instead of treating every prediction as equally reliable,
        the system can evaluate agreement among Random Forest
        decision trees.
        """
    )

    st.divider()

    st.markdown(
        """
        ### Why is this useful?

        A prediction supported by most trees indicates stronger
        model agreement.

        A prediction where trees disagree strongly indicates
        greater uncertainty and may require additional review.
        """
    )

    st.info(
        "Run a patient prediction to view the actual "
        "tree agreement and uncertainty score."
    )


# =========================================================
# ALERT CENTER
# =========================================================

elif page == "🚨 Alert Center":

    st.header(
        "🚨 Risk-Based Alert System"
    )

    st.write(
        """
        The system converts predicted probability into
        understandable risk categories.
        """
    )

    st.divider()

    a1, a2, a3 = st.columns(3)

    with a1:

        st.markdown(
            """
            <div class="blue-card">

            <h2>LOW</h2>

            <p>
            Routine monitoring
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with a2:

        st.markdown(
            """
            <div class="dashboard-card"
                 style="text-align:center;">

            <h2>MODERATE</h2>

            <p>
            Close monitoring
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with a3:

        st.markdown(
            """
            <div class="pink-card">

            <h2>HIGH</h2>

            <p>
            Clinical review recommended
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# ABOUT
# =========================================================

elif page == "ℹ️ About System":

    st.header(
        "ℹ️ About the Project"
    )

    st.markdown(
        """
        ## AI-Based Sepsis Prediction System

        This project is designed as an AI-based research
        prototype for early sepsis risk assessment.

        ### Core Components

        **1. Machine Learning Prediction**

        Predicts potential sepsis risk from patient
        clinical parameters.

        **2. Model Comparison**

        Multiple models can be evaluated using
        Accuracy, Precision, Recall, F1-score and ROC-AUC.

        **3. Uncertainty Awareness**

        Evaluates the confidence of Random Forest
        predictions using tree agreement.

        **4. SHAP Explainability**

        Explains which patient features influence
        the AI prediction.

        **5. Personalized Risk Trajectory**

        Tracks changes in patient risk over time.

        **6. Patient Data Reliability**

        Checks whether clinical inputs are reasonable.

        **7. Risk-Based Alerts**

        Converts prediction into actionable
        risk categories.

        **8. Clinical Review Support**

        Helps identify predictions that may
        require additional human review.
        """
    )

    st.divider()

    st.info(
        "⚠️ This is a research prototype and should not "
        "be used as a standalone medical diagnostic system."
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
    AI Sepsis Intelligence Dashboard |
    Research Prototype |
    Human Clinical Judgment Remains Essential
    </div>
    """,
    unsafe_allow_html=True
)