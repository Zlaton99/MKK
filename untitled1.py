# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st 

st.title("OPD fees")

pt_name = st.text_input("Pt name: ")
doctor = st.text_input("Dr.name: ")
doctor_fee= st.number_input("Dr.fees: ",0,step=1000)
clinic = st.number_input("Clinic fees: ",0,step=1000)


st.write("Patient name = ",pt_name)
st.write("Doctor: ",doctor)
st.write("Doctor fees:",doctor_fee)
st.write("Clinical fees: ",clinic)
         
st.write("Total:", int(doctor_fee + clinic))

st.subheader("Thank you")




