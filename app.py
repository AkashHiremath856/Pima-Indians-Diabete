import streamlit as st
import EarlyClassification
import Auth
import PimaClassification
import webbrowser as wb

uname = []
# Nav
sidebar = st.sidebar.radio(
    'Welcome To.', ('HOME', 'REGISTER', 'ABOUT'))

# Register the Auth. register if sidebar is REGISTER
if sidebar == 'REGISTER':
    Auth.register()


if 'page' not in st.session_state:
    st.session_state.page = 0


def nextPage(): st.session_state.page += 1
def firstPage(): st.session_state.page = 0


ph = st.empty()

if sidebar == 'HOME':
    if st.session_state.page == 0:
        with ph.container():
            uname.append(Auth.login())

    if st.session_state.page == 1:
        with ph.container():
            st.title('Diabetes Predictions')

            try:
                st.header(f'Welcome {uname[0]}')
                category = st.radio('Select Category Of Your Choice',
                                    ('Early Stage Predictions', 'Pima Based Diabetes Predictions'))

                # Early Stage Predictions Early Stage Predictions
                if category == 'Early Stage Predictions':
                    EarlyClassification.ecpred()

                # Pima Based Diabetes Predictions
                if category == 'Pima Based Diabetes Predictions':
                    PimaClassification.pcpred()

                st.button('Log Out', on_click=firstPage)

            except:
                category = st.radio('Select Category Of Your Choice',
                                    ('Early Stage Predictions', 'Pima Based Diabetes Predictions'))

                if category == 'Early Stage Predictions':
                    EarlyClassification.ecpred()

                if category == 'Pima Based Diabetes Predictions':
                    PimaClassification.pcpred()

                st.button('Log Out', on_click=firstPage)

if sidebar == 'ABOUT':
    with st.form('about'):
        st.title('About Project')

        st.text('''
        A Diabetes Classification Machine Learning Project Involves Building A Model That
        Can Accurately Classify Whether A Patient Has Diabetes Or Not, Based On Input 
        Features Such As Age, Gender, Bmi, Blood Pressure, And Glucose Levels. 

        The Diabetes Classification Machine Learning Project Is Important For Several 
        Reasons:

        1.Early Detection: Diabetes Is A Chronic Disease That Can Lead To Serious Health 
        Complications If Not Managed Properly. Early Detection Of Diabetes Can Help 
        Patients Receive Timely Treatment And Prevent Or Delay The Onset Of Complications.

        2.Personalized Treatment: Machine Learning Models Can Help Healthcare Providers 
        Make More Informed Decisions About Patient Care By Providing Personalized 
        Treatment  Plans Based On Individual Patient Data.

        3.Cost-effective: Diabetes Is A Costly Disease, And Early Detection And Management 
        Can  Lead To Significant Cost Savings For Both Patients And Healthcare Providers.

        4.Scalability: Machine Learning Models Can Be Scaled To Analyze Large Amounts Of 
        Data Quickly And Accurately, Making Them A Valuable Tool For Population Health 
        Management.

        5.Improved Patient Outcomes: Accurate Classification Of Diabetes Using Machine 
        Learning Can Lead To Improved Patient Outcomes By Ensuring Timely Diagnosis, 
        Appropriate Treatment, And Better Disease Management.

        Overall, The Diabetes Classification Machine Learning Project Has The Potential To 
        Significantly Improve Healthcare Outcomes By Enabling Early Detection And 
        Personalized Treatment Of Diabetes, Reducing Healthcare Costs, And Improving 
        Patient Outcomes.
                ''')

        if st.form_submit_button('Report Bug'):
            wb.open(
                "https://gmail.google.com/mail/?view=cm&fs=1&to=akash.hiremath25@gmail.com.com&su=Bug%20Report")
