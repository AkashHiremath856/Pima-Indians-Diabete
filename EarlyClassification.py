import pickle
import pandas as pd
import numpy as np
import streamlit as st
import time

df = pd.read_csv('DataSets/Early Classification of Diabetes.csv')

cols = (df.columns[0]).split(';')


def ecpred():
    model = pickle.load(
        open('models/Early_Classification_of_Diabetes.pkl', 'rb'))

    with st.form('ECOD'):

        st.title('Early Classification of Diabetes')
        criteria = []

        name = st.text_input('Name')
        age = st.text_input('Age')
        try:
            age = (int(float(age)))
        except:
            st.warning('Expecting a Number')
        criteria.append(age)
        gender = st.radio('Gender', ('M', 'F'))

        if gender == 'M':
            criteria.append(1)
        else:
            criteria.append(0)

        st.text('Select Symoptems')

        for col in cols[2:-1]:
            cb = st.checkbox(f'{col}'.capitalize())
            criteria.append(int(cb))

        if st.form_submit_button('Predict'):
            try:
                x = np.array(criteria, ndmin=2, dtype=float)
                res = (model.predict(x)[0])

                headers = 'Time \t\t Inputs \t\t Result\n'
                log_time = '{} ,'.format(time.ctime())
                crit = '{} .'.format(criteria)
                result = '{}\n'.format(res)

                with open('logs/logs1.txt', 'a') as f:
                    f.write(headers)
                    f.write(log_time)
                    f.write(crit)
                    f.write(result)

                if res:
                    st.info(
                        'Your Symoptems indicates Towards Having Diabetes Soon...'.upper())
                else:
                    st.info(
                        'No Symoptems indicating Towards Having Diabetes \U0001f600'.upper())

                # Report
                if ('Get Report'):
                    d = {}
                    for i, c in enumerate(criteria):
                        d['Customer Name'] = name
                        d[cols[i]] = c
                    d['Result'] = f'{bool(res)}'
                    dataf = pd.DataFrame(d, index=np.arange(1))

                    dataf.to_csv('tmp1.csv', mode='a',
                                 index=False, header=False)

                    table = pd.read_csv('tmp1.csv')
                    st.dataframe(table, use_container_width=True)

            except:
                st.warning('Inputs Required!')
