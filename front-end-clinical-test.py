import streamlit as st
import time

# Streamlit UI

# Placeholder functions for generating clinical example and image.
# Replace these with actual generation logic.

def generate_clinical_example():
    try:
        # Your logic for generating clinical example text.
        example = "Clinical Situation: Patient with suspected ailment ConditionA... \
                Patient is a 47-year-old male \
                presenting with a 3-day history of chest pain. \
                He also reports shortness of breath \
                and occasional dizziness."
        return example
    except:
        # Fallback text in case of error.
        return "Demo Clinical Situation: This is a demo clinical situation."

def generate_image():
    try:
        # Your logic for generating image.
        # For demo, using a demo online image, replace this with your logic.
        img_url = "https://www.e7health.com/files/blogs/chest-x-ray-29.jpg"
        return img_url
    except:
        # Fallback image in case of error.
        return "https://via.placeholder.com/500"

# ========= Title ========= #

st.title("Incedental AI")

# ========= Generate Clinical Scenario ========= #

# Display generated clinical example
clinical_example = generate_clinical_example()

# --------- Static Text --------- #

# st.text(clinical_example)
# st.markdown(f"<div style='border:4px solid red; padding:10px; margin:50px;'>{clinical_example}</div>", 
#             unsafe_allow_html=True)

# --------- Animated Text --------- #

# Check if 'counter' exists in the session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Generate or fetch your clinical scenario.
clinical_scenario_parts = [clinical_example]

# Create a message container for the clinical scenario
with st.chat_message("Clinical Scenario"):
    message_placeholder = st.empty()
    full_response = ""

    # Display clinical scenario up to the current counter with typing effect
    for part in clinical_scenario_parts[:st.session_state.counter + 1]:
        for chunk in part.split():
            full_response += chunk + " "
            time.sleep(0.075)  # Adjust the delay as required
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        full_response += '\n'  # Add newline after each part
    message_placeholder.markdown(full_response)

# # ========= Generate Image ========= #

# # Display the generated clinical image
# image_url = generate_image()
# time.sleep(0.075)  # Adjust the delay as required
# st.image(image_url, caption='Generated Clinical Image', use_column_width=True)

# If 'show_image' doesn't exist in session_state, initialize with False
if 'show_image' not in st.session_state:
    st.session_state.show_image = False

# Button to show image
if not st.session_state.show_image:
    if st.button('Continue to Image'):
        st.session_state.show_image = True

# Display the image after "Continue to Image" is pressed
if st.session_state.show_image:
    st.markdown("<style>@keyframes fadeIn {from {opacity: 0;} to {opacity: 1;}}</style>", unsafe_allow_html=True)
    st.image(generate_image(), caption='Generated Clinical Image', use_column_width=True)

    # # ========= Student Answer ========= #

    # Display condition checkboxes
    conditions = ["ConditionA", "ConditionB", "ConditionC", "ConditionD", "ConditionE"]
    if 'selected_conditions' not in st.session_state:
        st.session_state.selected_conditions = []

    for condition in conditions:
        if st.checkbox(condition):
            if condition not in st.session_state.selected_conditions:
                st.session_state.selected_conditions.append(condition)
        else:
            if condition in st.session_state.selected_conditions:
                st.session_state.selected_conditions.remove(condition)

    # Display selected conditions
    st.write("Selected conditions:")
    for condition in st.session_state.selected_conditions:
        st.write(condition)

    # Display "Submit" and "New Scenario" buttons
    if st.button('Submit'):
        st.write("Submitting...")  # Placeholder, replace with actual submission logic

    if st.button('New Scenario'):
        # Reset states for a new scenario
        st.session_state.counter = 0
        st.session_state.show_image = False
        st.session_state.selected_conditions = []
        st.experimental_rerun()  # Rerun the app
    