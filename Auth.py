import streamlit as st
import sqlite3
import os
import pandas as pd

conn = sqlite3.connect('Customers.db', check_same_thread=False)
c = conn.cursor()
x = ''


def create_table():
    """
     Create table if doesn't exist in the database. @return True if table was created False otherwise
    """
    c.execute(
        'CREATE TABLE IF NOT EXISTS Customers (name TEXT, email TEXT, phone TEXT, password TEXT)')


if 'page' not in st.session_state:
    st.session_state.page = 0


def nextPage(): st.session_state.page += 1


# Customer Registration Form
def register():
    """
     Register a new customer in Diabetes Predictions and log in if the password doesn't
    """
    with st.form("Customer Registration Form"):
        st.title('Diabetes Predictions')
        st.header('Customer Registration Form')
        name = st.text_input('Name')
        email = st.text_input('Email')
        phone = st.text_input('Phone')
        password = st.text_input('Enter the password', type='password')
        conpassword = st.text_input('Confirm Password', type='password')

        if password != conpassword:
            st.warning('Password Not Matching')

        if st.form_submit_button('Submit') and name and email and phone and password:
            try:
                create_table()
            except:
                c.execute('INSERT INTO Customers (name, email, phone, password) VALUES (?, ?, ?, ?)',
                          (name, email, phone, password))
                conn.commit()
                st.success('You have successfully registered')
                st.info('You can now login')
            c.execute('INSERT INTO Customers (name, email, phone, password) VALUES (?, ?, ?, ?)',
                      (name, email, phone, password))
            conn.commit()
            st.success('You have successfully registered')
            st.info('You can now login')


# Login
def login():
    """
     Login to diabetes prediction and return username if succesful. Otherwise return None. This is a function to be called from the page


     @return ( str ) username of
    """
    try:
        os.remove('tmp1.csv')
        os.remove('tmp2.csv')
    except:
        pass
    df1 = pd.DataFrame(columns=['Customer Name', 'age', 'gender', 'polyuria', 'polydipsia', 'sudden_weight_loss', 'weakness', 'polyphagia', 'genital_thrush', 'visual_blurring', 'itching', 'irritability', 'delayed_healing', 'partial_paresis', 'muscle_stiffness', 'alopecia', 'obesity', 'Result'
                                ])
    df2 = pd.DataFrame(columns=['Customer Name', 'Pregnancies', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
                                ])
    df1.to_csv('tmp1.csv', index=False)
    df2.to_csv('tmp2.csv', index=False)

    global x
    with st.form("Login Form"):
        st.title('Diabetes Predictions')
        st.header('Login Form')
        uname = st.text_input('Email')
        upass = st.text_input('Password', type='password')
        if st.form_submit_button('Login'):
            db = (dict(c.execute('select email, password from Customers')))
            if uname in list(db.keys()):
                if db[uname] == upass:
                    uname = c.execute(
                        'SELECT name FROM Customers WHERE email = ?', (uname,))
                    uname = c.fetchone()
                    st.success('Login Sucessful')
                    nextPage()
                    x = (uname[0])
                else:
                    st.warning('Check Your password')
            else:
                st.info('Register Please (Email not found)')
    return x
