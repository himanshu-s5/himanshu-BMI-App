import streamlit as st 

st.header("BMI calculator")
st.subheader("check whether you are underweight, healthy or overweight")

weight = st.number_input("Enter weight",value=None,placeholder="weight in Kg ")
measure_height = st.radio("choose height of your choice", ('cm','meter', 'feet'))
height = st.number_input(f"Height in {measure_height}",value=None,placeholder='Enter height')

if height and weight:
    if measure_height == 'cm':
        
            bmi = weight / (height/100)**2

    elif measure_height == 'meter':
        try:
            bmi = weight / (height**2)
        except:
            st.text("Enter some value")

    elif measure_height == 'feet':
        try:
            bmi = weight / (height / 3.28)**2
        except:
            st.text("Enter some value")

button = st.button('Calculate Bmi')
if button:
    try:
        st.write(f'your BMi is {bmi}')
        if bmi < 16 :
            st.error('extremly underweight')
        elif bmi > 16 and bmi < 18.5:
            st.warning('underweight')
        elif bmi > 18.5 and bmi < 24.5:
            st.success('Healthy')
        elif bmi > 24.5 and bmi < 30:
            st.warning('overweight')
        elif bmi > 30:
            st.error("extremly overweight")
    except:
        st.error('Invalid Input')