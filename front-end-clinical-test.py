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

# Check if 'scenario_complete' exists in the session state. If not, set to False
if 'scenario_complete' not in st.session_state:
    st.session_state.scenario_complete = False

# Only animate the clinical scenario if it hasn't been completed
if not st.session_state.scenario_complete:

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
                time.sleep(0.065)  # Adjust the delay as required
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            full_response += '\n'  # Add newline after each part
        message_placeholder.markdown(full_response)
        st.session_state.scenario_complete = True

else:
    # If scenario is already displayed, just display it without animation
    with st.chat_message("Clinical Scenario"):
        st.write(clinical_example)

# # ========= Generate Image ========= #

# If 'show_image' doesn't exist in session_state, initialize with False
if 'show_image' not in st.session_state:
    st.session_state.show_image = False

# Button to show image
if not st.session_state.show_image:
    if st.button('Continue to Image'):
        st.session_state.show_image = True

# Display the image after "Continue to Image" is pressed
if st.session_state.show_image:

    # Display the generated clinical image
    image_url = generate_image()
    time.sleep(0.075)  # Adjust the delay as required
    st.image(image_url, caption='Generated Clinical Image', use_column_width=True)
    
    # # ========= Student Answer ========= #

    # Insert Free Text Box, where users type in something...
    # and then Going to insert a conversational chatgpt function call here 
    # which will evaluate the response
    user_input = st.text_input("Your analysis:")

    # If the user has input something, simulate a call to ChatGPT (or your own function)
    if user_input:
        # This is a mock function to simulate a response. Replace with your actual logic or API call.
        def chat_gpt_response(user_text):
            # Dummy logic; replace with real function call
            if "ailment" in user_text.lower():
                return "It seems you've identified the ailment. Good job!"
            else:
                return "Not quite right. Try again."

        response = chat_gpt_response(user_input)
        st.write(response)
                
    if st.button('New Scenario', key='newScenarioBtn'):
        # Reset states for a new scenario
        st.session_state.counter = 0
        st.session_state.show_image = False
        st.session_state.selected_conditions = []
        st.experimental_rerun()  # Rerun the app
                

    