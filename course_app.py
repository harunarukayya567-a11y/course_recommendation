import pandas as pd
import joblib
import streamlit as st

model= joblib.load("course_model.pkl")
encoder = joblib.load("course_encoder.pkl")

hobby =st.text_input("enter your hobby:")
passion =st.text_input("what are your passion about:")
technical_level =st.text_input("your technical level:")
time_per_week =st.text_input("time you can spend weekly:")
goal =st.text_input("what ia your main goal:")
style =st.text_input("y our learning style:")

if st.button("Recommend"):
    sample_data = pd.DataFrame({
     "hobby":[hobby],
     "passion":[passion],
     "technical_level":[technical_level],
     "time_per_week":[time_per_week],
     "goal":[goal],
     "style":[style]    
    })
    sample_data['hobby'] = sample_data['hobby'].str.lower()
    sample_data['passion'] = sample_data['passion'].str.lower()
    sample_data['technical_level'] = sample_data['technical_level'].str.lower()
    
    converted = encoder.transform(sample_data)
    
    make_recommendation = model.predict(converted)
    
    st.success(f"Recommended product: {make_recommendation}")

    
