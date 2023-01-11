import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np

model = pkl.load(open('model.pkl' , 'rb'))


def main():
    st.title('Credit Card Defaulter')
    st.text("We use best of industry standards ML model and use them to ")
    st.subheader('Please enter the details of the client to know if he/she will **default** with your bank')
    
    # Create form elements
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:")
    gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])

    # Add a submit button
    if st.button('Predict'):
        # Collect input data
        input_data = [name, age, gender]
        # Run the model
        # Display the result
        st.text(input_data)


     
    col1, col2 = st.columns(2)
    col1.write("This is column 1")
    col1.header("col2 ")
    col2.write("This is column 2")
    col2.header('col3')
    
    
    tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
    tab1.write("this is tab 1")
    tab2.write("this is tab 2")
    
    
    tab1.header("this is great file app ")
    # tab2.header("this is one of the worst app ever seen ")
    a = st.sidebar.radio('Select one:', [1, 2])
    b = st.sidebar.text('oops sidebar lorem32fjkasjkajfksdkjk')
    st.sidebar.button('Right Button')
    st.text('Fixed width text')
    st.markdown('_Markdown_') # see *
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
    st.write('Most objects') # df, err, func, keras!
    st.write(['st', 'is <', 3]) # see *
    st.title('My title')
    st.header('My header')
    st.subheader('My sub')
    # st.text_area('enter the detail')
    # st.button('Click me')


    # st.checkbox('I agree')
    # st.radio('Pick one', ['cats', 'dogs'])
    # st.selectbox('Pick one', ['cats', 'dogs'])
    # st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
    # st.slider('Pick a number', 0, 100)
    # st.select_slider('Pick a size', ['S', 'M', 'L'])
    # st.text_input('First name')
    # st.number_input('Pick a number', 0, 10)
    # st.text_area('Text to translate')
    # st.date_input('Your birthday')
    # st.time_input('Meeting time')
    # st.file_uploader('Upload a CSV')
    # st.camera_input("Take a picture")
    # st.color_picker('Pick a color')

def display():
    st.title('Credit Card Defaulter')
    st.write("We use best of industry standards ML model and use them to predict whether the user will default or not we have an accuracy of over **95%** ")
    st.subheader('Please enter the details of the client to know if he/she will **default** with your bank')
    
    gender = st.radio('**Select Gender**' , ['Male' , 'Female'])
    age = st.slider('**Select Age**' , min_value= 12 , max_value=100)  
    tenure = st.slider('**Tenure served**' , min_value= 0 , max_value=70)
    phone = st.radio('**Whether customer uses phone services**' , ['Yes' , 'No'])
    mult = st.radio('**Whether customer uses multiple services**' , ['Yes' , 'No'])
    internet = st.radio('**Whether customer uses internet services**' , ['Yes' , 'No'])
    device = st.radio('**Whether customer uses device protection**' , ['Yes' , 'No'])
    tech = st.radio('**Whether customer uses tech support**' , ['Yes' , 'No'])
    tv = st.radio('**Whether customer stream TV**' , ['Yes' , 'No'])
    movie =st.radio('**Whether customer stream Movies**' , ['Yes' , 'No'])
    contract = st.radio('**Whether customer have entered contract**' , ['Yes' , 'No'])
    monthly = st.slider('**Select monthly service charges by the credit card company**', min_value=18 , max_value=120)
    yearly = st.slider('**Select yearly service charges by the credit card company**', min_value=20 , max_value=9000)
    
    
    gender = 1 if gender == 'Male' else 0
    age = 1 if age > 60 else 0 
    tenure = tenure
    phone = 1 if phone == 'Yes' else 0                
    mult = 1 if mult == 'Yes' else 0   
    internet = 1 if internet == 'Yes' else 0 
    device = 1 if device == 'Yes' else 0  
    tech = 1 if tech == 'Yes' else 0  
    tv = 1 if tv == 'Yes' else 0     
    movie = 1 if movie == 'Yes' else 0 
    contract = 1 if contract == 'Yes' else 0          
    monthly =monthly
    yearly = yearly      


    input_values = [gender , age , tenure , phone , mult  , internet , device , tech, tv ,movie , contract ,monthly , yearly]
    
    values_final = [np.array(input_values)]
    prediction = model.predict(values_final)
    output = round(prediction[0])
    
    if ( output ==0 ):
        st.error("Its likely that the person will default ")
    else:
        st.success(f"The person is expected to repay with a probality of {prediction}")


if __name__ == '__main__':
    display()
