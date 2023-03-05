import random
import pickle
import pandas as pd
import numpy as np
import streamlit as st
import time
import warnings
warnings.filterwarnings('ignore')

df2 = pd.read_csv('DataSets/Pimadiabetes.csv')
cols = (list(df2.columns))


def pcpred():
    container_2 = st.empty()
    with container_2.form('sample'):
        st.title('Sample')
        nr = random.randint(0, df2.shape[0])
        st.table(df2.iloc[nr, :])
        st.form_submit_button('More')

    button_A = st.button('Hide')
    if button_A:
        container_2.empty()
        st.text('Show Sample')
        button_B = st.button('Show')

    with st.form('PI'):
        model2 = pickle.load(open('models/Pimadiabetes.pkl', 'rb'))
        st.title('Diagnostically Predict Whether Or Not Patient Has Diabetes')

        symoptems = []
        name = st.text_input('Name')

        for col in cols[:-1]:
            x = st.text_input(f'{col}')
            symoptems.append(x)

        if st.form_submit_button('Results'):
            try:
                x2 = np.array([symoptems])
                res = (model2.predict(x2)[0])

                headers = 'Time \t\t Inputs \t\t Result\n'
                log_time = '{} ,'.format(time.ctime())
                crit = '{} .'.format(symoptems)
                result = '{}\n'.format(res)

                with open('logs/logs.txt', 'a') as f:
                    f.write(headers)
                    f.write(log_time)
                    f.write(crit)
                    f.write(result)

                if res == 1:
                    st.write(
                        'There is a high probablility of you having Diabetes.'.upper())
                else:
                    st.write(
                        'Congrats there are no Symoptems of Diabetes \U0001f600'.upper())

                # Report
                if ('Get Report'):
                    d = {}
                    for i, c in enumerate(symoptems):
                        d['Customer Name'] = name
                        d[cols[i]] = c
                    dataf = pd.DataFrame(d, index=np.arange(1))

                    dataf.to_csv('tmp2.csv', mode='a',
                                 index=False, header=False)

                table = pd.read_csv('tmp2.csv')
                st.dataframe(table, use_container_width=True)

            except:
                st.warning('Inputs Required!')
