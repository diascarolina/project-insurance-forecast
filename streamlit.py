import streamlit as st
import pandas as pd

import pickle


model_file = 'model_randomforestregressor.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)


def predict(answers_dict):
    df = pd.DataFrame(answers_dict.items()).T
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df.reset_index(drop = True)
    df.region = df.region.map({'Southwest': 0, 'Southeast': 1, 'Northwest': 2, 'Northeast': 3})

    prediction = model.predict(df)
    
    return float(prediction)

# st.markdown("<h1 style='text-align: center; color: black;'>Medical Health Insurance Forecast</h1>", unsafe_allow_html = True)

# st.markdown("Welcome to **Medical Insurance Forecast**. Fill the information below and click **Predict Value** to check how much would your insurance cost.", unsafe_allow_html = True)

# st.caption("**Disclaimer**: More details can be found [here at the project repository](https://github.com/diascarolina/project-insurance-forecast).")


answers_dict = {}

answers_dict['age'] = st.slider('What is your age?', help = 'The slider can be moved using the arrow keys.', min_value = 0, max_value = 100, step = 1)

answers_dict['sex'] = 1 if st.selectbox('What is your gender?', ['Female', 'Male']) == 'Yes' else 0

answers_dict['bmi'] = st.slider('What is your BMI (Body Mass Index)?', help = 'The slider can be moved using the arrow keys.', min_value = 0.0, max_value = 100.0, step = 0.1)

answers_dict['children'] = st.slider('How many children do you have?', help = 'The slider can be moved using the arrow keys.', min_value = 0, max_value = 10, step = 1)

answers_dict['smoker'] = 1 if st.selectbox('Do you smoke?', ['Yes', 'No']) == 'Yes' else 0

answers_dict['region'] = st.selectbox('In what region do you live?', ['Southwest', 'Southeast', 'Northwest', 'Northeast'])

if st.button('Predict Value'):
    value = predict(answers_dict)
    st.write(f'Your insurance would cost {round(value, 2)} USD.')