
import streamlit as st
from openai import OpenAI
import os


st.title("SmartCare Scheduler – AI Chatbot + Booking")
st.write("👩‍⚕️ Hello! I'm your AI assistant. I can help you book a hospital appointment.")

openai_api_key = st.text_input("Enter your OpenAI API key", type="password")

if openai_api_key:
    client = OpenAI(api_key=openai_api_key)

    user_prompt = st.text_area("Ask a question about your hospital visit or scheduling...")

    if st.button("Send to AI"):
        if user_prompt:
            with st.spinner("Thinking..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful healthcare assistant scheduling appointments."},
                            {"role": "user", "content": user_prompt}
                        ],
                        max_tokens=150
                    )
                    reply = response.choices[0].message.content
                    st.success(reply)
                except Exception as e:
                    st.error(f"API error: {str(e)}")


# Booking interface
st.header("Schedule Your Appointment")
language = st.selectbox("Choose your language:", ["English", "Spanish", "Finnish"])
appt_type = st.selectbox("Type of Appointment:", ["General consultation", "Follow-up", "Vaccination"])
preferred_day = st.selectbox("Preferred Day:", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
preferred_time = st.radio("Preferred Time:", ["Morning", "Afternoon"])

if st.button("Check Available Slots"):
    slots_db = {
        "Tuesday": ["14:00", "15:00", "16:00"],
        "Wednesday": ["10:00", "11:00"],
        "Friday": ["09:00", "13:00", "14:30"]
    }
    if preferred_day in slots_db:
        available = [slot for slot in slots_db[preferred_day] if preferred_time == "Afternoon" and int(slot.split(':')[0]) >= 12]
        if available:
            st.success(f"Available slots on {preferred_day} afternoon: {', '.join(available)}")
        else:
            st.warning("No available slots match your criteria.")
    else:
        st.info("No slots available for that day yet.")
