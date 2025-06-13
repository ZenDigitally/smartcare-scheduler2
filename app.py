
import streamlit as st

st.title("SmartCare Scheduler – Chatbot Appointment Demo")

st.write("👩‍⚕️ Welcome! Let's book your hospital appointment.")
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
        st.error("No slots available for that day yet.")
