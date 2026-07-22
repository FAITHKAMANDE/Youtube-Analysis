import streamlit as st
import pandas as pd
import joblib

# Load pipeline (preprocessing + model)
model = joblib.load("like_rate_model.pkl")
feature_names = joblib.load("feature_names.pkl")

st.title("🎬 YouTube Video Like Rate Predictor")

# Example inputs
duration = st.number_input("Video Duration (seconds)", min_value=1, value=300)
views = st.number_input("Channel Total Views", min_value=0, value=100000)
subs = st.number_input("Channel Subscribers", min_value=0, value=1000)
year = st.selectbox("Publish Year", [2022, 2023, 2024, 2025])
made_for_kids = st.selectbox("Made for Kids", ["Yes", "No"])
language = st.text_input("Default Audio Language (e.g., en, fr, es)", "en")
region = st.text_input("Region Restriction (e.g., US, KE, GB)", "US")
category_id = st.number_input("Category ID", min_value=1, value=10)


le_made_for_kids = joblib.load("made_for_kids_encoder.pkl")
input_data["made_for_kids"] = le_made_for_kids.transform(input_data["made_for_kids"].astype(str))


# Collect into DataFrame (raw form, pipeline will handle encoding)
input_data = pd.DataFrame([{
    "duration": duration,
    "channel_views": views,
    "channel_subscribers": subs,
    "published_year": year,
    "made_for_kids": made_for_kids,
    "default_audio_language": language,
    "region_restriction": region,
    "category_id": category_id
}])

# Predict
if st.button("Predict Like Rate"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Like Rate: {prediction:.4f} ({prediction*100:.2f}%)")
