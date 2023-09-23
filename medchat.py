import config
import openai

# Get the API key from the environment variable
openai.api_key = config.OPENAI_API_KEY


class MedChat(Patient):
    
    def __init__(self):
        super().__init__()
        self.system_prompt = "You are a medical expert and examiner. You are creating scenarios to test the knowledge of medical students. Based on these scenarios the medical student will be provided with a medical image for diagnosis. A focus of this is medical training is to help students identify incidental findings in medical images."
        self.instructions_prompt = " Your response should be clear and in the format of a clinical report, but your language should be at the level of a patient describing their symptoms, avoiding clinical jargon. Your response should not explicitly state any diagnosis, or hint to a potential diagnosis. Keep your scenarios and responses concise, with a max of 2-3 sentences. End with a statement that a clinician has ordered a medical image of the relevant body part."
        self.task_prompt = self.get_task_prompt()
        self.incidental_prompt = self.get_incidental_prompt()
        self.scenario_prompt = self.task_prompt + self.incidental_prompt + self.instructions_prompt
        self.messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.scenario_prompt},
            ]
        self.scenario = self.call_scenario()
        self.primary_correct = False
        self.secondary_correct = False



    def get_task_prompt(self):
        # Differentiate between healthy and unhealthy scenarios
        if primary_morbidity == "Healthy":
            task = f"Provide a third person realistic scenario for a {self.age} year-old {self.sex} presenting with symptoms that require a {self.image} of the {self.location}, but the {self.image} is healthy."
        else:
            task = f"Provide a third person realistic scenario for a {self.age} year-old {self.sex} presenting with {self.primary_morbidity} which requires a {self.image} of the {self.location}."
        return task
    
    
    
    def get_incidental_prompt(self):
        # Add incidental findings to the scenario prompt
        if len(incidental_morbidities) > 0:
            incidental = f" Symptoms of {', '.join(self.incidental_morbidities)} should only be described if they would become apparent in a clinicians initial assessment of the primary morbidity."
        else:
            incidental = ""
        return incidental
        


    def call_scenario(self):
        # Query GPT-4 with the scenario prompt
        completion = openai.ChatCompletion.create(
            model = "gpt-4-0613",
            messages=self.messages
        )
        messages.append({"role": "assistant", "content": completion.choices[0].message.content})
        
        return completion.choices[0].message.content
    
    
    
    def student_response(self, x1, x2, user_input: str, provide_answer=False):
        user_response = x1 + user_input + x2

        self.messages.append({"role": "user", "content": user_response})
        
        # Query GPT-4 with the scenario prompt
        completion = openai.ChatCompletion.create(
            model = "gpt-4-0613",
            messages=self.messages
        )
        
        if "True" in completion.choices[0].message.content:
            self.primary_correct = True
            
        if provide_answer:
            self.primary_correct = True
            
        return completion.choices[0].message.content
    
    
    # # Psuedorder
    # self.student_response(
    #     x1 = "The student after seeing the medical image has provided what they think is the diagnosis delimited by three ticks: ```",
    #     x2 = "```. If the student correctly identified the primary morbidity. Respond with: True. Otherwise provide a hint of the correct primary morbidity by describing a list of symptoms in clinically accurate language.",
    #     user_input
    # )
    
    # self.student_response(
    #     x1 = "The student after answering incorrectly and seeing your hint responded the following delimited by three ticks: ```"
    #     x2 = "```. If the student correctly identified the primary morbidity. Respond with: True. Otherwise provide radiological features the student should be looking for." 
    #     user_input
    # )
    
    # self.student_response(
    #     x1 = "The student after answering incorrectly and seeing your hint responded the following delimited by three ticks: ```",
    #     x2 = "```. If the student correctly identified the primary morbidity. Respond with: True. Otherwise provide the primary diagnosis." 
    #     user_input,
    #     provide_answer=True
    # )