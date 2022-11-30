import streamlit as st
import numpy as np
st.write("""
# Multiplication of 2 given numbers""")
st.header('User Input Parameters')

num1=st.number_input('Number 1')
num2=st.number_input('Number 2')

x=num1*num2
st.header('Multiplication of both numbers is: ')
st.write(x)
