import config
import openai

# Get the API key from the environment variable
openai.api_key = config.OPENAI_API_KEY

# sex = "female"
# age = "1"

# location = "chest"
# image = "x-ray"
# primary_morbidity = "fracture"
# severity = "mild"
# incidental_morbidities = ["tuberculosis"]


def call_scenario(sex: str, age: str, location: str, image: str, primary_morbidity: str, incidental_morbidities: list):
    """
    Generates a medical scenario for testing the knowledge of medical students and provides a clinical report format response.

    Parameters:
    - sex (str): The gender of the patient (e.g., "male", "female").
    - age (str): The age of the patient.
    - location (str): The body part or area for which a medical image is required.
    - image (str): The type of medical image requested (e.g., "X-ray", "CT").
    - primary_morbidity (str): The primary medical condition or symptom for which the image is needed.
    - incidental_morbidities (list): A list of additional symptoms or conditions that may be present in the diagnostic image.

    Returns:
    - str: A realistic third-person medical scenario for the provided parameters, with a focus on generating a clinical report-like response.

    Example Usage:
    scenario = call_scenario("female", "45", "chest", "MRI", "shortness of breath", ["cough", "chest pain"])
    print(scenario)
    """
    
    # Overall prompt to set the context of the task
    system_prompt = "You are a medical expert and examiner. You are creating scenarios to test the knowledge of medical students. Based on these scenarios the medical student will be provided with a medical image for diagnosis. A focus of this is medical training is to help students identify incidental findings in medical images."

    # Break down of scenario prompt
    instructions_prompt = " Your response should be clear and in the format of a clinical report, but your language should be at the level of a patient describing their symptoms, avoiding clinical jargon. Your response should not explicitly state any diagnosis, or hint to a potential diagnosis. Keep your scenarios and responses concise, with a max of 2-3 sentences. End with a statement that a clinician has ordered a medical image of the relevant body part."

    # Differentiate between healthy and unhealthy scenarios
    if primary_morbidity == "healthy":
        task_prompt = f"Provide a third person realistic scenario for a {age} year-old {sex} presenting with symptoms that require a {image} of the {location}, but the {image} is healthy."
    else:
        task_prompt = f"Provide a third person realistic scenario for a {age} year-old {sex} presenting with {severity} {primary_morbidity} which requires a {image} of the {location}."

    # Add incidental findings to the scenario prompt
    if len(incidental_morbidities) > 0:
        incidental_prompt = f" Symptoms of {', '.join(incidental_morbidities)} should only be described if they would become apparent in a clinicians initial assessment of the primary morbidity."
    else:
        incidental_prompt = ""

    # Combine scenario prompt
    scenario_prompt = task_prompt + incidental_prompt + instructions_prompt

    # Query GPT-4 with the scenario prompt
    completion = openai.ChatCompletion.create(
        model = "gpt-4-0613",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": scenario_prompt},
        ]
    )
    
    return completion.choices[0].message.content
