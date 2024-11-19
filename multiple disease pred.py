# -*- coding: utf-8 -*-
"""
Created on Saturday, Date: 01-11-24
@author: Sourav
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie animations URLs
lottie_loading = load_lottie_url("https://assets5.lottiefiles.com/private_files/lf30_editor_vxdjwohx.json")


# Custom CSS style for the page and inputs
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(36,107,128,0.6) 100%, rgba(230,96,12,0) 100%, rgba(0,212,255,1) 100%);
    }
    .card {
        background-color: #1C1C1C;
        border: 1px solid #E50914;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }
    .stTextInput > div > div > input {
        background-color: #374242;
        color: #141414;
        border: 1px solid #123536;
        border-radius: 8px;
        padding: 10px;
    }
    .stButton > button {
        background-color: #E50914;
        color: #141414;
        font-size: 16px;
        font-weight: bold;
        border: none;
        padding: 12px 24px;
        border-radius: 5px;
        transition: background-color 0.3s ease;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #B00610;
    }
    h1, h2, h3, h4 {
        color: #141414;
        font-weight: 300;
        letter-spacing: 1px;
        font-family: 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# loading the saved models
diabetes_model = pickle.load(open('D:/multiple disease prediction/saved models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('D:/multiple disease prediction/saved models/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('D:/multiple disease prediction/saved models/parkinsons_model.sav', 'rb'))


# Default ,theme and font
theme = "Dark"
font = "Trebuchet MS"

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Explore MultiMed',
                           ['Home', 'Diabetes Predictor', 'Heart Disease Predictor', 'Parkinsons Predictor', 'Health Tips', 'Settings'],
                           icons=['house', 'activity', 'heart', 'person', 'heart-pulse', 'gear'],
                           default_index=0,
                           menu_icon="cast",
                           styles={
                               "container": {"padding": "5!important", "background-color": "#080808"},
                               "icon": {"color": "white", "font-size": "22px"},
                               "nav-link": {"font-size": "15px", "text-align": "centre", "margin": "0px", "color": "white"},
                               "nav-link-selected": {"background-color": "#5672a2"},
                           })

    # Footer for contact info
    st.sidebar.markdown("---")
    st.sidebar.markdown("For support, contact:")  
    st.sidebar.markdown("📞 **contact:** +1 (123) 456-7890")
    st.sidebar.markdown("✉️ **Email:** support@example.com")
    st.sidebar.markdown("Developed by:")
    st.sidebar.markdown("Sourav | Aeshni | Vaishnavi with ❤️ ")


# Theme
if selected == 'Settings':
    st.title("Settings")
    theme = st.selectbox("Choose Theme", ["Dark","Light",  "Blue"])
    font = st.selectbox("Choose Font", ["Arial", "Roboto", "Courier New","Times New Roman","Georgia","Verdana","Tahoma","Trebuchet MS","Impact"])

#theme

if theme == "Dark":
    background = "#1C1C1C"
    text_color = "#FFFFFF"
elif theme == "Light":
    background = "#F0F2F6"
    text_color = "#000000"
elif theme == "Blue":
    background = "#1C2A48"
    text_color = "#FFFFFF"

#fonts
if font == "Arial":
    font_family = "Arial, sans-serif"
elif font == "Roboto":
    font_family = "'Roboto', sans-serif"
elif font == "Courier New":
    font_family = "'Courier New', monospace"
elif font == "Times New Roman":
    font_family = "'Times New Roman', serif"
elif font == "Georgia":
    font_family = "Georgia, serif"
elif font == "Verdana":
    font_family = "Verdana, sans-serif"
elif font == "Tahoma":
    font_family = "Tahoma, sans-serif"
elif font == "Trebuchet MS":
    font_family = "'Trebuchet MS', sans-serif"
elif font == "Impact":
    font_family = "Impact, sans-serif"


st.markdown(
    f"""
    <style>
    /* Custom background and text color */
    .stApp {{
        background-color: {background};
        color: {text_color};
        font-family: {font_family};
    }}

    /* Custom CSS for headings */
    h1, h2, h3, h4 {{
        font-family: {font_family};
        color: {text_color};
    }}
    
    /* Text Input Styling */
    .stTextInput > div > div > input {{
        background-color: #374242;
        color: #FFFFFF;
        border: 1px solid #123536;
        border-radius: 8px;
        padding: 10px;
        font-family: {font_family};
    }}

    /* Button Styling */
    .stButton > button {{
        background-color: #E50914;
        color: {text_color};
        font-size: 16px;
        font-family: {font_family};
        font-weight: bold;
        border: none;
        padding: 12px 24px;
        border-radius: 5px;
        transition: background-color 0.3s ease;
        cursor: pointer;
    }}
    .stButton > button:hover {{
        background-color: #B00610;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# Font icons
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """,
    unsafe_allow_html=True
)
# Home Page
if selected == 'Home':
    
    # Main Heading with Icon
    st.markdown(
        """
        <h1 style="text-align:center; color:#6497fa; font-size: 36px;">
            Welcome to MultiMed Predictor <i class="fa-solid fa-house-medical"></i>
        </h1>
        <p style="text-align:center; color:grey; font-size:18px;">
            Helping you understand potential health risks with advanced machine learning.
        </p>
        """,
        unsafe_allow_html=True
    )
    
    # Disease Prediction with Cards
    st.markdown(
        """
        <div style="display: flex; justify-content: space-around; gap: 20px;">
            <div style="width: 30%; padding: 20px; background-color: #000000; border-radius: 10px; text-align: center;">
                <i class="fa-sharp fa-solid fa-droplet" style="font-size: 40px; color: #ff6961;"></i>
                <h3>Diabetes Predictor</h3>
                <p>Predict your risk of diabetes with accuracy and ease.</p>
            </div>
            <div style="width: 30%; padding: 20px; background-color: #000000; border-radius: 10px; text-align: center;">
                <i class="fa-regular fa-heart" style="font-size: 40px; color: #ffb347;"></i>
                <h3>Heart Disease Predictor</h3>
                <p>Find out if you're at risk of heart disease based on key health indicators.</p>
            </div>
            <div style="width: 30%; padding: 20px; background-color: #000000; border-radius: 10px; text-align: center;">
                <i class="fas fa-brain" style="font-size: 40px; color: #77dd77;"></i>
                <h3>Parkinson's Disease Predictor</h3>
                <p>Get insights on potential Parkinson's symptoms.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <p style="text-align:center; color:#6497fa; font-size:16px;">
            Let's begin the test; please open the sidebar
        </p>
        """,
        unsafe_allow_html=True
    )

    # Footer
    st.markdown(
        """
        <hr style="margin-top: 50px;">
        <div style="text-align: center; font-size: 14px; color: grey;">
                ||  ॐ सर्वे भवन्तु सुखिनः सर्वे सन्तु निरामयाः  ||  <br>
        May all be happy, May all be free from illness<br>
        with ❤️ from developers :)
        </div>
        """,
        unsafe_allow_html=True
    )



    
    
    
    

# Diabetes Prediction Page
if selected == 'Diabetes Predictor':
    
    st.markdown(
        """
        <h1 style="text-align:center; color:#ff6961;">Diabetes Predictor <i class="fa-sharp fa-solid fa-droplet"></i></h1>
        <p style="text-align:center; color:grey; font-size:16px;">
            Understand your risk of diabetes with personalized predictions and key insights.
        </p>
        
        <div style="display: flex; justify-content: center; gap: 15px; margin-top: 20px;">
            <div style="width: 25%; padding: 10px; background-color: #3f3f3f; border-radius: 8px; text-align: center;">
                <h4 style="font-size:16px; color:#ffffff;">What is Diabetes?</h4>
                <p style="font-size:14px; color:#d3d3d3;">
                    Diabetes is a chronic disease that affects how your body turns food into energy.
                </p>
            </div>
            <div style="width: 25%; padding: 10px; background-color: #3f3f3f; border-radius: 8px; text-align: center;">
                <h4 style="font-size:16px; color:#ffffff;">Risk Factors</h4>
                <p style="font-size:14px; color:#d3d3d3;">
                    High blood sugar, family history, lifestyle factors, and age increase your risk.
                </p>
            </div>
            <div style="width: 25%; padding: 10px; background-color: #3f3f3f; border-radius: 8px; text-align: center;">
                <h4 style="font-size:16px; color:#ffffff;">Prevention Tips</h4>
                <p style="font-size:14px; color:#d3d3d3;">
                    Maintain a healthy lifestyle through diet, exercise, and regular check-ups.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <p style="text-align:center; color:#ff6961; font-size:16px;">
           Note (*): Filling in all fields is optional but recommended for more accurate results.
        </p>
        """
        ,
        unsafe_allow_html=True
    )

    # Default values
    default_skin_thickness = 20.536458
    default_insulin = 79.799479
    default_Pragnancies = 0
    
    # Getting user inputs
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age of the Person*')
        
    with col2:
        Glucose = st.text_input('Glucose Level*')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value*')
    with col1:
        BMI = st.text_input('BMI value*')
    with col2:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value*')
    with col3:
        SkinThickness = st.text_input('Skin Thickness value')
    with col1:
        Insulin = st.text_input('Insulin Level')
    with col2:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    # Use default values if inputs are empty
    SkinThickness = float(SkinThickness) if SkinThickness else default_skin_thickness
    Insulin = float(Insulin) if Insulin else default_insulin
    Pregnancies = float(Pregnancies) if Pregnancies else default_Pragnancies
  

    # Prediction and error handling
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            inputs = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), 
                      float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            diab_prediction = diabetes_model.predict([inputs])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'Likely diabetic. Seek medical advice'
            else:
                diab_diagnosis = 'No diabetes detected'
            st.success(diab_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all input fields.")
  
    
  
    
  
    
            
            
# Heart Disease Prediction Page
if selected == 'Heart Disease Predictor':
    
    st.markdown(
        """
        <h1 style="text-align:center; color:#ffb347;">Heart Disease Predictor <i class='fa-regular fa-heart'></i></h1>
        <p style="text-align:center; color:grey; font-size:16px;">
            Get insights on your heart health with our prediction model.
        </p>
        
        <div style="display: flex; justify-content: center; gap: 15px; margin-top: 20px;">
            <div style="width: 25%; padding: 10px; background-color: #3f3f3f; border-radius: 8px; text-align: center;">
                <h4 style="font-size:16px; color:#ffffff;">What is Heart Disease?</h4>
                <p style="font-size:14px; color:#d3d3d3;">
                    Heart disease encompasses conditions affecting the heart's structure and function.
                </p>
            </div>
            <div style="width: 25%; padding: 10px; background-color: #3f3f3f; border-radius: 8px; text-align: center;">
                <h4 style="font-size:16px; color:#ffffff;">Risk Factors</h4>
                <p style="font-size:14px; color:#d3d3d3;">
                    High blood pressure, cholesterol, smoking, and family history elevate your risk.
                </p>
            </div>
            <div style="width: 25%; padding: 10px; background-color: #3f3f3f; border-radius: 8px; text-align: center;">
                <h4 style="font-size:16px; color:#ffffff;">Prevention Tips</h4>
                <p style="font-size:14px; color:#d3d3d3;">
                    Adopt a heart-healthy lifestyle: balanced diet, regular exercise, and no smoking.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    
    st.markdown(
        """
        <p style="text-align:center; color:#ffb347; font-size:16px;">
        Note (*): Filling in all fields is optional but recommended for more accurate results.
        </p>
        """
        ,
        unsafe_allow_html=True
    )
      
    # Default values
    default_oldpeak = 0.8
    default_fbs = 0
    default_restecg = 1
    default_thalach = 153
    default_age = 55
    default_trestbps = 130
    default_chol = 240
    

    sex_mapping = {"Male": 1, "Female": 0}
    
    # Getting user inputs
    col1, col2, col3 = st.columns(3)
    with col1:
        slope = st.text_input('slope')
    with col2:
        sex_input = st.selectbox('Sex', options=["Male", "Female"])
        sex = sex_mapping[sex_input]
    with col3:
        cp = st.text_input('cp')
    with col1:
        ca = st.text_input('ca')
    with col2:
        thal = st.text_input('thal')
    with col3:
        exang = st.text_input('exang')
    with col1:
        restecg = st.text_input('restecg*')
    with col2:
        thalach = st.text_input('thalach*')
    with col3:
        fbs = st.text_input('fbs*')
    with col1:
        oldpeak = st.text_input('oldpeak*')
    with col2:
        age = st.text_input('Age*')
    with col3:
        trestbps = st.text_input('trestbps*')
    with col1:
        chol = st.text_input('chol*')
    
    # Use default values
    age = int(age) if age else default_age
    trestbps = int(trestbps) if trestbps else default_trestbps
    chol = int(chol) if chol else default_chol
    fbs = int(fbs) if fbs else default_fbs
    restecg = int(restecg) if restecg else default_restecg
    thalach = int(thalach) if thalach else default_thalach
    oldpeak = float(oldpeak) if oldpeak else default_oldpeak
    
    # Prediction and error handling
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            inputs = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), 
                      float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), 
                      float(ca), float(thal)]
            heart_prediction = heart_disease_model.predict([inputs])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'Heart disease risk detected.'
            else:
                heart_diagnosis = 'No heart disease detected'
            st.success(heart_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all input fields.")



# Parkinson's Prediction Page
if selected == "Parkinsons Predictor":
    
    st.markdown(
        """
        <h1 style="text-align:center; color:#77dd77;">Parkinson's Predictor <i class='fas fa-brain'></i></h1>
        <p style="text-align:center; color:grey; font-size:16px;">
            Gain insights into potential symptoms of Parkinson's disease.
        </p>
        
        <div style="display: flex; justify-content: center; gap: 15px; margin-top: 20px;">
            <div style="width: 25%; padding: 10px; background-color: #3f3f3f; border-radius: 8px; text-align: center;">
                <h4 style="font-size:16px; color:#ffffff;">What is Parkinson’s?</h4>
                <p style="font-size:14px; color:#d3d3d3;">
                    Parkinson's is a neurodegenerative disorder affecting movement control.
                </p>
            </div>
            <div style="width: 25%; padding: 10px; background-color: #3f3f3f; border-radius: 8px; text-align: center;">
                <h4 style="font-size:16px; color:#ffffff;">Risk Factors</h4>
                <p style="font-size:14px; color:#d3d3d3;">
                    Age, genetics, and environmental factors contribute to the risk of Parkinson's.
                </p>
            </div>
            <div style="width: 25%; padding: 10px; background-color: #3f3f3f; border-radius: 8px; text-align: center;">
                <h4 style="font-size:16px; color:#ffffff;">Prevention Tips</h4>
                <p style="font-size:14px; color:#d3d3d3;">
                    Regular physical activity and a balanced diet can help maintain brain health.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="text-align:center; color:#77dd77; font-size:16px;">
        Note (*): Filling in all fields is optional but recommended for more accurate results.
        </p>
        """
        ,
        unsafe_allow_html=True
    )
 
     # Default values
    default_Jitter_Abs = 0.000030
    default_RAP = 0.002500
    default_PPQ = 0.047
    default_DDP = 0.007490
    default_flo = 104.315000
    default_Jitter_percent = 0.004940
    default_APQ3 = 0.012790
    default_DFA = 0.718099
    default_DDA = 0.038360
    default_fhi = 175.829000
    
    # Getting user inputs
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Input fields for each feature
    with col1:
        fo = st.text_input('fo')
    with col2:
        Shimmer = st.text_input('Shimmer')
    with col3:
        Shimmer_dB = st.text_input('Shimmer_dB')
    with col4:
        APQ5 = st.text_input('APQ5')
    with col5:
        APQ = st.text_input('MDVP:APQ')
    with col1:
        NHR = st.text_input('NHR')
    with col2:
        HNR = st.text_input('HNR')
    with col3:
        RPDE = st.text_input('RPDE')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')
    with col3:
        Jitter_Abs = st.text_input('Jitter_Abs*')
    with col4:
        DDA = st.text_input('DDA*')
    with col5:
        RAP = st.text_input('RAP*')
    with col1:
        PPQ = st.text_input('PPQ*')
    with col2:
        DDP = st.text_input('DDP*')
    with col3:
        DFA = st.text_input('DFA*')
    with col4:
        fhi = st.text_input('fhi*')
    with col5:
        flo = st.text_input('flo*')
    with col1:
        APQ3 = st.text_input('APQ3*')
    with col2:
        Jitter_percent = st.text_input('Jitter_percent*')
        
    
    # Use default values
    Jitter_Abs = float(Jitter_Abs) if Jitter_Abs else default_Jitter_Abs
    RAP = float(RAP) if RAP else default_RAP
    PPQ = float(PPQ) if PPQ else default_PPQ
    DDP = float(DDP) if DDP else default_DDP
    flo = float(flo) if flo else default_flo
    Jitter_percent = float(Jitter_percent) if Jitter_percent else default_Jitter_percent
    APQ3 = float(APQ3) if APQ3 else default_APQ3
    DFA = float(DFA) if DFA else default_DFA
    DDA = float(DDA) if DDA else default_DDA
    fhi = float(fhi) if fhi else default_fhi
    
    # Prediction and error handling
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        try:
            inputs = [float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), 
                      float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB), 
                      float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR), 
                      float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]
            parkinsons_prediction = parkinsons_model.predict([inputs])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "Possible Parkinson’s. Follow up recommended"
            else:
                parkinsons_diagnosis = "No Parkinson’s detected"
            st.success(parkinsons_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all input fields.")




# Health Tips Page
if selected == 'Health Tips':
    # Main title with icon
    st.title("Health Tips for Wellness")
    st.markdown("""
        Here are some practical health tips for managing and preventing conditions such as **Diabetes**, **Heart Disease**, and **Parkinson's Disease**.
        Remember, small lifestyle changes can make a big difference!
    """)
    
    # CSS for custom styling
    st.markdown("""
        <style>
            .tips-section {
                background-color: #0;
                border: 1px solid #6497fa;
                border-radius: 8px;
                padding: 15px;
                margin: 10px 0;
            }
            .tips-section h3 {
                color: #6497fa;
                font-weight: bold;
            }
            .tip-icon {
                font-size: 1.2em;
                color: #6497fa;
                margin-right: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Diabetes Tips
    with st.expander(" Diabetes Management Tips"):
        st.markdown("""
        <div class="tips-section">
            <h3>Key Tips for Diabetes Management</h3>
            <ul>
                <li><span class="tip-icon">🍎</span>Eat a balanced diet with fruits, vegetables, and whole grains.</li>
                <li><span class="tip-icon">🏃‍♂️</span>Exercise regularly to help maintain healthy blood sugar levels.</li>
                <li><span class="tip-icon">💉</span>Monitor blood sugar levels regularly and consult your healthcare provider.</li>
                <li><span class="tip-icon">💧</span>Stay hydrated and limit sugary drinks.</li>
                <li><span class="tip-icon">🚭</span>Avoid smoking and limit alcohol intake to reduce risk of complications.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Heart Disease Tips
    with st.expander(" Heart Disease Prevention Tips"):
        st.markdown("""
        <div class="tips-section">
            <h3>Key Tips for Heart Health</h3>
            <ul>
                <li><span class="tip-icon">🥗</span>Eat a healthy diet rich in fiber and low in saturated fats.</li>
                <li><span class="tip-icon">🚶‍♂️</span>Engage in physical activity for at least 30 minutes most days.</li>
                <li><span class="tip-icon">📈</span>Monitor blood pressure and cholesterol levels regularly.</li>
                <li><span class="tip-icon">🧘‍♀️</span>Manage stress effectively and practice relaxation techniques.</li>
                <li><span class="tip-icon">👨‍⚕️</span>Get regular check-ups to stay informed about your heart health.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Parkinson's Disease Tips
    with st.expander(" Parkinson's Disease Management Tips"):
        st.markdown("""
        <div class="tips-section">
            <h3>Key Tips for Managing Parkinson's Disease</h3>
            <ul>
                <li><span class="tip-icon">🏃‍♀️</span>Stay active with exercises like walking, swimming, or yoga.</li>
                <li><span class="tip-icon">🥕</span>Eat a diet rich in antioxidants and fiber to support brain health.</li>
                <li><span class="tip-icon">🧩</span>Engage in mental activities such as puzzles or reading to keep your mind sharp.</li>
                <li><span class="tip-icon">🏠</span>Ensure safety at home by adding grab bars and reducing clutter.</li>
                <li><span class="tip-icon">👨‍⚕️</span>Work with your healthcare provider for a tailored management plan.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


